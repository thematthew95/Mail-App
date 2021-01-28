import email
import imaplib

username = 'jankowalski798466@gmail.com'
password = 'Python123'

mail = imaplib.IMAP4_SSL("imap.gmail.com")

mail.login(username, password)
