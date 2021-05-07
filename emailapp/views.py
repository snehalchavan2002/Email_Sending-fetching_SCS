from django.shortcuts import render
from django.core.mail import send_mail
import imaplib
import email
import traceback


# Create your views here.
def index(request):
    send_mail(
        "This is a sample subject",
        "This is a test sample message",
        'chavansnehal1020@gmail.com',
        ['chavanmadhur65@gmail.com'],
        fail_silently=False)

    return render(request, "send/index.html")
#
# ORG_EMAIL = "@gmail.com"
# FROM_EMAIL = "chavansnehal1020" + ORG_EMAIL
# FROM_PWD = "Rajanirani"
# SMTP_SERVER = "imap.gmail.com"
# SMTP_PORT = 993
#
# def read_email_from_gmail():
#     try:
#         mail = imaplib.IMAP4_SSL(SMTP_SERVER)
#         mail.login(FROM_EMAIL, FROM_PWD)
#         mail.select('inbox')
#
#         data = mail.search(None, 'ALL')
#         mail_ids = data[1]
#         id_list = mail_ids[0].split()
#         first_email_id = int(id_list[0])
#         latest_email_id = int(id_list[-1])
#
#         for i in range(latest_email_id,first_email_id, -1):
#             data = mail.fetch(str(i), '(RFC822)' )
#             for response_part in data:
#                 arr = response_part[0]
#                 if isinstance(arr, tuple):
#                     msg = email.message_from_string(str(arr[1],'utf-8'))
#                     email_subject = msg['subject']
#                     email_from = msg['from']
#                     print('From : ' + email_from + '\n')
#                     print('Subject : ' + email_subject + '\n')
#
#     except Exception as e:
#         traceback.print_exc()
#         print(str(e))
#
# read_email_from_gmail()