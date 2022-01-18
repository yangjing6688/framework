from common.Utils import Utils
from bs4 import BeautifulSoup
import csv
import imaplib
import email
import re
import os


class GmailHandler:
    def __init__(self):
        self.mail = None
        self.email_sub = None
        self.email_from = None
        self.email_msg = None
        self.save_dir = os.path.dirname(__file__) + '/tools/credentials/'
        self.utils = Utils()

    def get_data_from_csv(self, filename, key='User Name'):
        """
        Get the bulk user credentials stored in csv file
        :param filename: credential dict
        :param key
        :return:
        """
        csv_data = {}
        with open(filename) as f:
            csv_reader = csv.DictReader(f)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                csv_data[row[key]] = row
                line_count += 1
        return csv_data

    def get_url_link(self, soup):
        """
        Get the url link from soup object
        :param soup:
        :return: url links
        """
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links

    def get_list_item_tags(self, soup):
        """
        :param soup:
        :return:
        """
        li = []
        items = soup.find_all('li')
        for i in items:
            li.append(i.get_text())
        return li

    def get_html_table_rows(self, soup):
        """
        Assuming html contains only one table
        Get the rows from html table
        :param soup:
        :return:
        """
        rows = []
        table = soup.find('table')
        if not table:
            self.utils.print_info("No table in html")
            return 1
        table_rows = table.find_all('tr')
        for row in table_rows:
            td = row.find_all('td')
            th = row.find_all('th')
            if th:
                row = [i.text.strip() for i in th]
            else:
                row = [i.text.strip() for i in td]
            rows.append(row)
        return rows

    def get_paragraph_from_html(self, soup):
        """
        Get the paragraph text from the html
        :return:
        """
        text_list = []
        paragraph = soup.find_all('p')
        for para in paragraph:
            text_list.append(para.get_text())
        return text_list

    def mail_initialization(self, mail_id, password):
        """
        Login to mail account and select the inbox
        :param mail_id:
        :param password:
        :return: all mail uid from inbox
        """
        # using imap module connect the gmail imap server
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(mail_id, password)

        # select the inbox
        self.mail.select('inbox')

        # Get mail uid
        result, dta = self.mail.uid('search', None, "ALL")
        inbox_mail_items = dta[0].split()
        return inbox_mail_items

    def get_raw_email(self, email_item_list, subj=None):
        """
        Get the raw emails from latest 5 emails based on the subj
        :param email_item_list: List of the emails
        :param subj: subject line of the email
        :return:
        """
        email_count = 0
        for mail in email_item_list[::-1]:
            result, email_data = self.mail.uid('fetch', mail, '(RFC822)')
            raw_email = email_data[0][1].decode("utf-8")
            self.email_msg = email.message_from_string(raw_email)

            _from = self.email_msg['From']
            _to = self.email_msg['to']
            _subj = self.email_msg['Subject']

            if not subj:
                return _subj
            self.utils.print_info("Email Subj:{}".format(_subj))
            if subj in _subj:
                self.utils.print_info("Email From:{}".format(_from))
                self.utils.print_info("Email To:{}".format(_to))
                return self.email_msg
            else:
                email_count += 1
            if email_count == 2:
                break

    def get_content_from_email_body(self, email_msg):
        """
        Download file if attachment, read the text part, html part
        :return:
        """
        file = None
        html_content = None
        plain_content = None

        for part in email_msg.walk():
            if part.get_content_type() == "multipart":
                continue
            filename = part.get_filename()
            # Download the attachment
            if filename:
                file = os.path.join(self.save_dir, filename)
                self.utils.print_info(file)
                if not os.path.isfile(file):
                    with open(file, 'wb') as fp:
                        fp.write(part.get_payload(decode=True))
            # get the html type payload
            if "html" in part.get_content_type():
                html_content = part.get_payload()
            # Get plain text type payload
            if "plain" in part.get_content_type():
                plain_content = part.get_payload()
        return file, html_content, plain_content

    def get_user_approval_url(self, mail_id, password):
        """
        Get the user approve url link
        :param mail_id:
        :param password:
        :return: url link
        """
        inbox_mail_items = self.mail_initialization(mail_id, password)
        subj = "Approve User Credential"
        email_msg = self.get_raw_email(inbox_mail_items, subj)
        if not email_msg:
            self.utils.print_info("There are no email with subj line")
            return -1

        _, _html, _ = self.get_content_from_email_body(email_msg)
        soup = BeautifulSoup(_html, 'html.parser')
        url_links = self.get_url_link(soup)
        url = url_links[0]
        rm = re.compile(r'&amp;')
        return re.sub(rm, '&', url)

    def get_url_to_set_password_for_new_user(self, mail_id, password):
        """
        Get the url link to set the new user password
        :param mail_id:
        :param password:
        :return:
        """
        inbox_mail_items = self.mail_initialization(mail_id, password)
        subj = "Welcome to ExtremeCloud IQ"
        email_msg = self.get_raw_email(inbox_mail_items, subj)
        if not email_msg:
            self.utils.print_info("There are no email with subj line")
            return -1

        _, _html, _ = self.get_content_from_email_body(email_msg)
        soup = BeautifulSoup(_html, 'html.parser')
        url_links = self.get_url_link(soup)
        url_link = url_links[-1]
        self.utils.print_info(url_link)
        return url_link

    def get_password_reset_link(self, mail_id, password):
        """
        Get the url link to set the new user password
        :param mail_id:
        :param password:
        :return:
        """
        inbox_mail_items = self.mail_initialization(mail_id, password)
        subj = "Password Reset Verification"
        email_msg = self.get_raw_email(inbox_mail_items, subj)
        if not email_msg:
            self.utils.print_info("There are no email with subj line")
            return -1

        _, _html, _ = self.get_content_from_email_body(email_msg)
        soup = BeautifulSoup(_html, 'html.parser')
        url_links = self.get_url_link(soup)
        url_link = url_links[0]
        self.utils.print_info(url_link)
        return url_link

    def get_login_credential(self, mail_id, password):
        """
        Get User Credential attachment
        :param mail_id:
        :param password:
        :return:
        """
        inbox_mail_items = self.mail_initialization(mail_id, password)
        subj = "Login Credentials"
        email_msg = self.get_raw_email(inbox_mail_items, subj)
        if not email_msg:
            self.utils.print_info("There are no email with subj line")
            return -1
        _, _html, _ = self.get_content_from_email_body(email_msg)
        soup = BeautifulSoup(_html, 'html.parser')

        li_items = self.get_list_item_tags(soup)
        self.utils.print_info(li_items)

        el1 = li_items[0]
        el2 = li_items[1]

        # Removing the special character sets from the string
        sp_char_set = ["\n", "\r", "="]
        for char_ in sp_char_set:
            el1 = re.sub(char_, '', el1)
            el2 = re.sub(char_, '', el2)

        self.utils.print_info(el1)
        self.utils.print_info(el2)
        if "Your Login" in el1 and "Your Password" in el2:
            login_id = el1.split()[-1]
            access_key = el2.split()[-1]
        else:
            access_key = el1.split()[-1]
            login_id = el2.split()[-1]

        self.utils.print_info("Access key is:{}".format(access_key))
        self.utils.print_info("Login id is:{}".format(login_id))
        return access_key, login_id

    def get_login_credential_from_attachments(self, mail_id, password):
        """
        Get bulk user credentials from attachments
        :return:
        """
        inbox_mail_items = self.mail_initialization(mail_id, password)
        subj = "Login Credentials"
        email_msg = self.get_raw_email(inbox_mail_items, subj)
        if not email_msg:
            self.utils.print_info("There are no email with subj line")
            return -1
        cred_file, _html, _ = self.get_content_from_email_body(email_msg)

        credentials = self.get_data_from_csv(cred_file)
        self.utils.print_info(credentials)
        return credentials

    def get_cloud_pin_for_wi_fi_network(self, mail_id, password):
        """
        Get WI-Fi Network authentication cloud PIN
        :param mail_id:
        :param password:
        :return:
        """
        inbox_mail_items = self.mail_initialization(mail_id, password)
        subj = "PIN for Wi-Fi Network"
        email_msg = self.get_raw_email(inbox_mail_items, subj)
        if not email_msg:
            self.utils.print_info("There are no email with subj line")
            return -1

        _, _html, _ = self.get_content_from_email_body(email_msg)
        soup = BeautifulSoup(_html, 'html.parser')
        para = self.get_paragraph_from_html(soup)
        self.utils.print_info(para)
        pin = para[1]
        self.utils.print_info("Generated PIN:{}".format(pin))
        return pin

    def get_cloud_cwp_no_pin_event_report(self, mail_id, password):
        """
        Get the CWP No pin Event report
        :param mail_id:
        :param password:
        :return:
        """
        inbox_mail_items = self.mail_initialization(mail_id, password)
        subj = "Cloud CWP PIN Events Report"
        email_msg = self.get_raw_email(inbox_mail_items, subj)
        if not email_msg:
            self.utils.print_info("There are no emil with subj line")
            return -1
        _, _html, _ = self.get_content_from_email_body(email_msg)
        soup = BeautifulSoup(_html, 'html.parser')
        para = self.get_paragraph_from_html(soup)
        self.utils.print_info(para)
        to, from_ = None, None
        for line in para:
            if re.search(r'There were no PIN authentication ', line):
                pattern = re.compile(r'\d+-\d+-\d+\W\d+:\d+')
                to_from = re.findall(pattern, line)
                from_ = to_from[0]
                to = to_from[1]
                self.utils.print_info("No PIN Auth event between {}  : {}".format(from_, to))
        return from_, to

    def get_cloud_cwp_pin_event_report(self, mail_id, password):
        """
        Get the CWP No pin Event report
        :param mail_id:
        :param password:
        :return:
        """
        data = {}
        inbox_mail_items = self.mail_initialization(mail_id, password)
        subj = "Cloud CWP PIN Events Report"
        email_msg = self.get_raw_email(inbox_mail_items, subj)
        if not email_msg:
            self.utils.print_info("There are no emil with subj line")
            return -1
        file, _html, _ = self.get_content_from_email_body(email_msg)
        soup = BeautifulSoup(_html, 'html.parser')

        # To read the table from html parser
        table_rows = self.get_html_table_rows(soup)
        self.utils.print_info(table_rows)
        data['Login Time'] = table_rows[1][0]
        data['SSID Name'] = table_rows[1][1]
        data['User Name'] = table_rows[1][2]
        data['Client Mac Address'] = table_rows[1][3]

        # To read the paragraph
        to, from_ = None, None
        para = self.get_paragraph_from_html(soup)
        self.utils.print_info(para)
        for line in para:
            if re.search(r'PIN authentication events between', line):
                pattern = re.compile(r'\d+-\d+-\d+\W\d+:\d+')
                to_from = re.findall(pattern, line)
                from_ = to_from[0]
                to = to_from[1]
                self.utils.print_info("PIN Auth event between {}  : {}".format(from_, to))
        data['from'] = from_
        data['to'] = to
        csv_data = self.get_data_from_csv(file, 'Client MAC Address')
        self.utils.print_info(data)
        return data, csv_data

    def get_email_subj(self, mail_id, password):
        """
        Get email subject line
        :param mail_id:
        :param password:
        :return:
        """
        inbox_mail_items = self.mail_initialization(mail_id, password)
        email_subj = self.get_raw_email(inbox_mail_items)
        return email_subj

    def get_sender_email_id(self, mail_id, password, subj_line):
        """
        Get the sender email id based on the subj line

        :param mail_id:  id of the email
        :param password: password of the email
        :param subj_line: subject string to get the email
        :return:
        """
        inbox_mail_items = self.mail_initialization(mail_id, password)
        email_msg = self.get_raw_email(inbox_mail_items, subj_line)
        if not email_msg:
            self.utils.print_info("There are no emil with subj line")
            return -1
        return email_msg['from']

    def get_email_reports_url_link(self, mail_id, password):
        """
        - Get the url link of email reports sent by XIQ
        :param mail_id:  mail id to get the url link
        :param password:
        :return: url link
        """
        inbox_mail_items = self.mail_initialization(mail_id, password)
        subj = "report from Extreme Networks"
        email_msg = self.get_raw_email(inbox_mail_items, subj)
        if not email_msg:
            self.utils.print_info("There are no email with subj line")
            return -1

        _, _html, _ = self.get_content_from_email_body(email_msg)
        soup = BeautifulSoup(_html, 'html.parser')
        url_links = self.get_url_link(soup)
        url = url_links[0]
        rm = re.compile(r'&amp;')
        return re.sub(rm, '&', url)