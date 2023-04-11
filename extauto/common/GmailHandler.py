from extauto.common.Utils import Utils
from bs4 import BeautifulSoup
import csv
import imaplib
import email
import re
import os
import time
from robot.libraries.BuiltIn import BuiltIn


class GmailHandler:
    def __init__(self):
        self.mail = None
        self.email_sub = None
        self.email_from = None
        self.email_msg = None
        self.save_dir = os.path.dirname(__file__) + '/tools/credentials/'
        self.utils = Utils()
        self.builtin = BuiltIn()

    def _get_data_from_csv(self, filename, key='User Name'):
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

    def _get_url_link(self, soup):
        """
        Get the url link from soup object
        :param soup:
        :return: url links
        """
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links

    def _get_list_item_tags(self, soup):
        """
        :param soup:
        :return:
        """
        li = []
        items = soup.find_all('li')
        for i in items:
            li.append(i.get_text())
        return li

    def _get_html_table_rows(self, soup):
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
            return False
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

    def _get_paragraph_from_html(self, soup):
        """
        Get the paragraph text from the html
        :return:
        """
        text_list = []
        paragraph = soup.find_all('p')
        for para in paragraph:
            text_list.append(para.get_text())
        return text_list

    def _mail_initialization(self, mail_id, password, folder):
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
        self.mail.select(folder)
        # Get mail uid
        result, dta = self.mail.uid('search', None, "ALL")
        inbox_mail_items = dta[0].split()
        return inbox_mail_items

    def _get_raw_email(self, email_item_list, subj=None):
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
            if email_count == 1:
                break

    def _get_raw_email_from_folder(self, mail_id, password, subj, mail_trash='True'):
        """
        - This method will check the emails with subject line in inbox folder and spam folder
        - If email exists return the raw email else return -1

        :param mail_id: The mail id
        :param password: The mail password
        :param subj:  The mail subject to look for
        :param mail_trash: trash the mail if mail trash is true
        :return: None, if nothing is found, otherwise it will return the email message that was found
        """

        device_selected = 0
        counter = 0
        while device_selected == 0:
            if counter > 10:
                break
            else:
                counter = counter + 1
            self.utils.print_info(f'Getting the email, counter: {counter}')
            self.utils.print_info(f"Check the subject line: {subj} email in inbox folder")
            inbox_mail_items = self._mail_initialization(mail_id, password, 'inbox')
            email_msg = self._get_raw_email(inbox_mail_items, subj)
            if email_msg:
                if mail_trash == 'True':
                    self._move_email_to_trash()
                return email_msg

            self.utils.print_info(f"Check the subj line:{subj} email in spam folder")
            inbox_mail_items = self._mail_initialization(mail_id, password, '[Gmail]/Spam')
            email_msg = self._get_raw_email(inbox_mail_items, subj)
            if email_msg:
                if mail_trash == 'True':
                    self._move_email_to_trash()
                return email_msg
            self.utils.print_info(f'Email was not found, sleep for 5 seconds and try again, counter: {counter}')
            time.sleep(5)

        # No email was found, so return None
        self.builtin.fail(f"There are no email with subject line {subj}  in inbox/spam folder")
        return None

    def _get_content_from_email_body(self, email_msg):
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

    def _move_email_to_trash(self):
        self.mail.store('1:*', '+X-GM-LABELS', '\\Trash')
        self.mail.expunge()

    def get_user_approval_url(self, mail_id, password, mail_trash='True'):
        """
        - Get the user approve url link
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get User Approval Url  ${EMAIL_ID}   ${PASSWORD}``

        :param mail_id:  email id to open
        :param password: email id password
        :param mail_trash: trash the mail if mail trash is true
        :return: url link
        """
        if email_msg := self._get_raw_email_from_folder(mail_id, password, "Approve User Credential"):
            _, _html, _ = self._get_content_from_email_body(email_msg)
            soup = BeautifulSoup(_html, 'html.parser')
            url_links = self._get_url_link(soup)
            url = url_links[0]
            rm = re.compile(r'&amp;')
            if mail_trash == 'True':
                self._move_email_to_trash()
            return re.sub(rm, '&', url)

    def get_sponsor_action_url(self, mail_id, password, sponsor_action):
        """
        - Get the sponsor action url link
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Sponsor Action Url  ${EMAIL_ID}   ${PASSWORD}  ${SPONSOR_ACTION}``

        :param mail_id:  email id to open
        :param password: email id password
        :param sponsor_action: 'permit' or 'deny' action by sponsor
        :param mail_trash: trash the mail if mail trash is true
        :return: url link
        """
        if email_msg := self._get_raw_email_from_folder(mail_id, password, "Requesting Access"):
            re.sub(r'\n', '', str(email_msg))
            _, _html, _ = self._get_content_from_email_body(email_msg)
            soup = BeautifulSoup(_html, 'html.parser')
            url_links = self._get_url_link(soup)
            if(sponsor_action == 'permit'):
                url = url_links[0]
            else:
                url = url_links[1]
            rm = re.compile(r'&amp;')
            return re.sub(rm, '&', url)

    def get_sponsor_action_login_credential(self, mail_id, password, emailto, passcode_length):
        """
        - Get the user credential from email
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Sponsor Action Login Credential  ${EMAIL_ID}   ${PASSWORD} ${EMAIL_TO}  ${SPONSOR_ACTION}``

        :param mail_id:  email id to open
        :param password: email id password
        :param emailto: email is sent to 'sponsor' or 'user'
        :param passcode_length: passcode length length=4 for OTP and 8 for Passcode
        :return: passcode
        """
        if(emailto == 'sponsor'):
            emailsubj = "Internet Access for"
            if passcode_length == 4:
                pattern = re.compile(r'''Passcode:\s(.{4})''')
            else:
                pattern = re.compile(r'''Passcode:\s(.{8})''')
        else:
            emailsubj = "your internet access code"
            if passcode_length == 4:
                pattern = re.compile(r'''passcode is\s(.{4})''')
            else:
                pattern = re.compile(r'''passcode is\s(.{8})''')
        if email_msg := self._get_raw_email_from_folder(mail_id, password, emailsubj):
            re.sub(r'\n', '', str(email_msg))
            _, _html, _ = self._get_content_from_email_body(email_msg)
            soup = BeautifulSoup(_html, 'html.parser')
            password = re.findall(pattern, str(soup.text))
            return password[0]

    def get_url_to_set_password_for_new_user(self, mail_id, password, mail_trash='True'):
        """
        - Get the url link to set the new user password
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Url To Set Password For New User  ${MAIL_ID}  ${PASSWORD}``

        :param mail_id: email id to open
        :param password: email id password
        :param mail_trash: trash the mail if mail trash is true
        :return: url link
        """
        if email_msg := self._get_raw_email_from_folder(mail_id, password, "Welcome to ExtremeCloud IQ"):
            _, _html, _ = self._get_content_from_email_body(email_msg)
            soup = BeautifulSoup(_html, 'html.parser')
            url_links = self._get_url_link(soup)
            url_link = url_links[-1]
            self.utils.print_info(url_link)
            if mail_trash == 'True':
                self._move_email_to_trash()
            return url_link

    def get_password_reset_link(self, mail_id, password, mail_trash='True'):
        """
        - Get the url link to set the new user password
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Password Reset Link  ${MAIL_ID}  ${PASSWORD}``

        :param mail_id:  email id to open
        :param password: email id password
        :param mail_trash: trash the mail if mail trash is true
        :return: reset url link
        """
        if email_msg := self._get_raw_email_from_folder(mail_id, password, "Password Reset Verification"):
            _, _html, _ = self._get_content_from_email_body(email_msg)
            soup = BeautifulSoup(_html, 'html.parser')
            url_links = self._get_url_link(soup)
            url_link = url_links[0]
            self.utils.print_info(url_link)
            if mail_trash == 'True':
                self._move_email_to_trash()
            return url_link

    def get_password_setup_link(self, mail_id, password, msg, mail_trash='True'):
        """
        - Get the url link to set the new user password
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Password Setup Link  ${MAIL_ID}  ${PASSWORD}    ${MSG}``

        :param mail_id:  email id to open
        :param password: email id password
        :param msg:  subject line of email id to search from gmail
        :param mail_trash: trash the mail if mail trash is true
        :return: reset url link
        """
        if email_msg := self._get_raw_email_from_folder(mail_id, password, msg):
            _, _html, _ = self._get_content_from_email_body(email_msg)
            soup = BeautifulSoup(_html, 'html.parser')
            url_links = self._get_url_link(soup)
            url_link = url_links[1]
            self.utils.print_info(url_link)
            if mail_trash == 'True':
                self._move_email_to_trash()
            return url_link

    def get_login_credential(self, mail_id, password, mail_trash='True'):
        """
        - Get User Credential sent to email
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Login Credential  ${MAIL_ID}  ${PASSWORD}``

        :param mail_id: email id to open
        :param password: email id password
        :param mail_trash: trash the mail if mail trash is true
        :return: access_key, login id
        """
        if email_msg := self._get_raw_email_from_folder(mail_id, password, "Login Credentials"):
            _, _html, _ = self._get_content_from_email_body(email_msg)
            soup = BeautifulSoup(_html, 'html.parser')

            li_items = self._get_list_item_tags(soup)
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
            if mail_trash == 'True':
                self._move_email_to_trash()
            return access_key, login_id

    def get_login_credential_from_attachments(self, mail_id, password, mail_trash='True'):
        """
        - Get bulk user credentials from attachments
        - It will read the latest two emails
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Login Credentials From Attachments  ${MAIL_ID}  ${PASSWORD}``

        :param mail_id: email id to open
        :param password: email id password
        :param mail_trash: trash the mail if mail trash is true
        :return: credentials dict
        """
        self.utils.print_info("Using Mail ID: ", mail_id, " Password: ", password)
        if email_msg := self._get_raw_email_from_folder(mail_id, password, "Login Credentials", mail_trash):
            try:
                cred_file, _html, _ = self._get_content_from_email_body(email_msg)
                if cred_file != None:
                    credentials = self._get_data_from_csv(cred_file)
                else:
                    # Fail this test because the file was not found
                    self.builtin.fail(f'Failed to read in the attactment file from the email!\nEmail: {_html}\nCredentials file: {cred_file}')
                self.utils.print_info(credentials)
                return credentials
            except Exception as e:
                self.builtin.fail(f"Failure to get the credentials from attachment or html email with exception: {e}")
        else:
            self.print_error('Failed to find the email using the subject: Login Credentials' )

    def get_cloud_pin_for_wi_fi_network(self, mail_id, password, mail_trash='True'):
        """
        - Get WI-Fi Network access cloud PIN
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Cloud Pin For Wi Fi Network    ${MAIL_ID}  ${PASSWORD}``

        :param mail_id: email id to open
        :param password: email id password
        :param mail_trash: trash the mail if mail trash is true
        :return: cloud pin
        """
        if email_msg := self._get_raw_email_from_folder(mail_id, password, "PIN for Wi-Fi Network"):
            _, _html, _ = self._get_content_from_email_body(email_msg)
            soup = BeautifulSoup(_html, 'html.parser')
            para = self._get_paragraph_from_html(soup)
            self.utils.print_info(para)
            pin = para[1]
            self.utils.print_info("Generated PIN:{}".format(pin))
            if mail_trash == 'True':
                self._move_email_to_trash()
            return pin

    def get_cloud_cwp_no_pin_event_report(self, mail_id, password, mail_trash='True'):
        """
        - Get the CWP No pin Event report
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Cloud Cwp No Pin Event Report  ${MAIL_ID}  ${PASSWORD}``

        :param mail_id: email id to open
        :param password: email id password
        :param mail_trash: trash the mail if mail trash is true
        :return: event report from and to time
        """
        if email_msg := self._get_raw_email_from_folder(mail_id, password, "Cloud CWP PIN Events Report"):
            _, _html, _ = self._get_content_from_email_body(email_msg)
            soup = BeautifulSoup(_html, 'html.parser')
            para = self._get_paragraph_from_html(soup)
            self.utils.print_info(para)
            to, from_ = None, None
            for line in para:
                if re.search(r'There were no PIN authentication ', line):
                    pattern = re.compile(r'\d+-\d+-\d+\W\d+:\d+')
                    to_from = re.findall(pattern, line)
                    from_ = to_from[0]
                    to = to_from[1]
                    self.utils.print_info("No PIN Auth event between {}  : {}".format(from_, to))
            if mail_trash == 'True':
                self._move_email_to_trash()
            return from_, to

    def get_cloud_cwp_pin_event_report(self, mail_id, password, mail_trash='True'):
        """
        - Get the CWP pin Event report csv and table data
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Cloud Cwp Pin Event Report   ${MAIL_ID}  ${PASSWORD}``

        :param mail_id: email id to get event reports
        :param password: email id password
        :param mail_trash: trash the mail if mail trash is true
        :return: event report table data and csv data
        """
        data = {}
        if email_msg := self._get_raw_email_from_folder(mail_id, password, "Cloud CWP PIN Events Report"):
            file, _html, _ = self._get_content_from_email_body(email_msg)
            soup = BeautifulSoup(_html, 'html.parser')

            # To read the table from html parser
            if not self._get_html_table_rows(soup):
                self.builtin.fail("No event report present in the mail body")
                return -1

            table_rows = self._get_html_table_rows(soup)
            self.utils.print_info(table_rows)
            data['Login Time'] = table_rows[1][0]
            data['SSID Name'] = table_rows[1][1]
            data['User Name'] = table_rows[1][2]
            data['Client Mac Address'] = table_rows[1][3]

            # To read the paragraph
            to, from_ = None, None
            para = self._get_paragraph_from_html(soup)
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
            csv_data = self._get_data_from_csv(file, 'Client MAC Address')
            self.utils.print_info(data)
            if mail_trash == 'True':
                self._move_email_to_trash()
            return data, csv_data

    def get_email_subj(self, mail_id, password):
        """
        - Get email subject line
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Email Subj   ${MAIL_ID}  ${PASSWORD}``

        :param mail_id: email id
        :param password: email id password
        :return: email subj line
        """
        inbox_mail_items = self._mail_initialization(mail_id, password, 'inbox')
        email_subj = self._get_raw_email(inbox_mail_items)
        return email_subj

    def get_sender_email_id(self, mail_id, password, subj_line, mail_trash='True'):
        """
        - Get the sender email id based on the subj line
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Sender Email Id  ${MAIL_ID}  ${PASSWORD}  ${SUBJ_LINE}``

        :param mail_id:  id of the email
        :param password: password of the email
        :param subj_line: subject string to get the email
        :param mail_trash: trash the mail if mail trash is true
        :return: sender email id
        """
        if email_msg := self._get_raw_email_from_folder(mail_id, password, subj_line):
            if mail_trash == 'True':
                self._move_email_to_trash()
            return email_msg['from']

    def get_email_reports_url_link(self, mail_id, password, mail_trash='True'):
        """
        - Get the url link of email reports sent by XIQ
        - It will read the latest two emails
        - Keyword Usage:
         - ``Get Email Reports Url Link    ${MAIL_ID}  ${PASSWORD}``

        :param mail_id:  mail id to get the url link
        :param password: mail id password
        :param mail_trash: trash the mail if mail trash is true
        :return: url link
        """
        if email_msg := self._get_raw_email_from_folder(mail_id, password, "report from Extreme Networks"):
            _, _html, _ = self._get_content_from_email_body(email_msg)
            soup = BeautifulSoup(_html, 'html.parser')
            url_links = self._get_url_link(soup)
            url = url_links[0]
            rm = re.compile(r'&amp;')
            if mail_trash == 'True':
                self._move_email_to_trash()
            return re.sub(rm, '&', url)
