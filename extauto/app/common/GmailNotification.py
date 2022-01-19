import imaplib
import email
from common.Utils import Utils
import re


class GmailNotification:
    def __init__(self):
        self.utils = Utils()

    def get_gmail_message_subject(self, email_id, password):
        """
        Get the email subject
        :param email_id: (str) valid email id
        :param password:(str)  corresponding email id password
        """

        self.utils.print_info("Using Email ID: ", email_id)
        self.utils.print_info("Using Email PWD: ", password)

        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_id, password)
        mail.select('inbox')

        email_type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        self.utils.print_info("First Email ID: ", first_email_id)
        self.utils.print_info("Latest Email ID: ", latest_email_id)

        typ, data = mail.fetch(str(latest_email_id), '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode())
                email_subject = msg['subject']
                email_from = msg['from']
                self.utils.print_info("Email from: ", email_from)
                self.utils.print_info("*INFO* Message Subject is :", email_subject)
                return email_subject
            else:
                return -1

    def gmail_initialization(self, mail_id, password):
        """
        Initialize gmail account object for reading gmail
        :param mail_id:
        :param password: password of the email
        :return:
        """
        # using imap module connect the gmail imap server
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(mail_id, password)

        # select the inbox
        self.mail.select('inbox')

        # search all the mail mails in inbox
        typ, data = self.mail.search(None, 'ALL')
        email_ids = data[0]

        return email_ids

    def get_gmail_message_body(self, mail_id, password):
        """
        Get the email subject line and email body content
        :param mail_id:
        :param password:
        :return:
        """
        email_id = self.gmail_initialization(mail_id, password)

        id_list = email_id.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        # Fetch the email with particular id
        typ, data = self.mail.fetch(str(latest_email_id), '(RFC822)')

        msg = None
        for response in data:
            if isinstance(response, tuple):
                msg = email.message_from_string(response[1].decode())
                self.email_sub = msg['subject']
                self.email_from = msg['from']
                self.utils.print_info(self.email_sub)
                self.utils.print_info(self.email_from)
            try:
                for body in msg.get_payload():
                    self.utils.print_info("Email Body: ", body.get_payload(decode=True))
                    self.utils.print_info("Email Message Content is: ", msg.get_payload())
                    return self.email_sub, body.get_payload(decode=True), data
            except Exception as e:
                return self.email_sub, msg.get_payload(), data

    def get_url_to_set_password_for_new_user1(self, mail_id, password):
        """
        Get the url link to set the new user password
        :param mail_id: Valid email id
        :param password: Corresponding email id password
        :return:
        """
        mail_sub, mail_body, _ = self.get_gmail_message_body(mail_id, password)
        self.utils.print_info("message body: ",mail_body)
        self.utils.print_info("message sub: ",mail_sub)
        import sys, pdb;
        pdb.Pdb(stdout=sys.__stdout__).set_trace()
        if "Welcome to ExtremeCloud IQ" in mail_sub:
            url = re.search("(?P<url>https?://[^\s]+)", mail_body).group("url")
            return url


    def get_url_to_set_password_for_new_user(self, mail_id, password):
        """
        Get the url link to set the new user password
        :param mail_id: Valid email id
        :param password: Corresponding email id password
        :return:
        """
        mail_sub, mail_body, data = self.get_gmail_message_body(mail_id, password)
        self.utils.print_info("Message Subject is:", mail_sub)
        if "Welcome to ExtremeCloud IQ" in mail_sub:
            url = re.findall("(?P<url>https?://[^\s]+)", data[0][1].decode())
            rest_url = url[3].strip('"')
            self.utils.print_info(rest_url)
            return rest_url

    def verify_username_for_new_user(self, email, password):
        """
        read setup password link  from the gmail message content
        :param email_id:(str) valid email id
        :param password:(str)  corresponding email id password
        """
        msg_sbj = self.get_gmail_message_subject(email, password)
        self.utils.print_info("Message Subject is:", msg_sbj)
        if "Welcome to ExtremeCloud IQ" in msg_sbj:
            msg_body = self.get_gmail_message_body(email, password).decode()
            user = re.search("([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)", msg_body)
            username = user.group(1)
            self.utils.print_info("Setup Password URL is:", username )
            return username
        else:
            return -1
