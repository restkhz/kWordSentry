import logging
import smtplib
from config import MAIL
from email.mime.text import MIMEText

def alert(url):
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(name)s - %(message)s')
    sendmail(url)

def makeMsg(url,recv):
    msg = '''
Hello:
    
kWordSentry found a page might be changed:
{0}
    
kWordSentry
    '''.format(url)
    mail = MIMEText(msg,'plain','utf-8')
    mail['From']='''"{0}" <{1}>'''.format(MAIL['USER_NICKNAME'], MAIL['USER_ADDR'])
    mail['To']=recv
    mail['Subject']='[kWordSentry] Page changes'
    logging.debug(mail.as_string())
    return mail

def sendmail(url):
    for recv in MAIL['RECV_ADDR']:
        logging.info("Sending mail to %s" % (recv,))
        try:
            mail = makeMsg(url, recv)
            if MAIL['SSL']:
                s = smtplib.SMTP_SSL(MAIL['HOST'], MAIL['PORT'])
            else:
                s = smtplib.SMTP(MAIL['HOST'], MAIL['PORT'])
                if MAIL['TLS']:
                    s.starttls()
            s.login(MAIL['USER_ADDR'], MAIL['USER_PASS'])
            s.sendmail(MAIL['USER_ADDR'], recv, mail.as_string())
            s.quit()
        except Exception as e:
            logging.warning("Error: %s" % (e,))
    logging.info('Done.')

def test():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(name)s - %(message)s')
    sendmail('http://<test-parameter>')
    
if __name__ == "__main__":
    print('TESTING...')
    test() 
