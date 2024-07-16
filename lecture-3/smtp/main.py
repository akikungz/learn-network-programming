import smtplib

message = """
    From: akikungz <akikungz@akikungz.uk>
    To: mild-honey <mild-honey@akikungz.uk>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: SMTP HTML e-mail test

    This is an e-mail message to be sent in HTML format

    <b>This is HTML message.</b>
    <h1>This is headline.</h1>
"""

try:
    smtp = smtplib.SMTP("192.168.122.3", 25)
    smtp.sendmail("akikungz@akikungz.uk", "akikungz@akikungz.uk", message)
    print("Successfully sent email")
except Exception as e:
    print(e)
