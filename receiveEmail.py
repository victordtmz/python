import imaplib
import email
imap_server = "imap.flockmail.com"
account = 'victor.m@enlacellc.com'
pwd = "********"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(account, pwd)
imap.select("Inbox")
_, msgnums = imap.search(None, "ALL")
print(msgnums)
for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")
    message = email.message_from_bytes(data[0][1])
    # print(message.get("From"))
    # print(message.get("To"))
    # print(message.get("BCC"))
    # print(message.get("Date"))
    # print(message.get("Subject"))
    print("Content:")
    for part in message.walk():
        if part.get_content_type() == "text/html":
            print(part.as_string())
