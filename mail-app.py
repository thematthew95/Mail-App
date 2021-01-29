import email
import imaplib
import os

username = 'jankowalski798466@gmail.com'
password = 'Python123'

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

mail.select("inbox")

result, data = mail.uid('search', None, "ALL")

inbox_item_list = data[0].split()

for item in inbox_item_list:
    result2, email_data = mail.uid('fetch', item, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    subject = email_message['Subject']
    date = email_message['Date']
    for part in email_message.walk():
        if part.get_content_maintype() == "multipart":
            continue
        filename = subject + " | " + date
    save_path = os.path.join(os.getcwd(), "saved")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    with open(os.path.join(save_path, filename), 'wb') as fp:
        fp.write(part.get_payload(decode=True))

