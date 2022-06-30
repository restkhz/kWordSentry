'''
A Int. For sleep. In sec.
Don't write this value too low.
'''
DURATION = 10

'''
Which module to use to alert. You could use:_sendMail, _serverChan or DIY.
ALARM accepts a string or a list so you could use one or all of them.
e.g ALARM='_sendMail' or ALARM=['_sendMail', '_serverChan']
'''
#ALARM='_sendMail'
ALARM='_serverChan'

'''
Alarm: MAIL's config. Take Gmail as a example,
MAIL = {
    'HOST':'smtp.gmail.com',
    'PORT':'587',
    'TLS': True,
    'SSL': False,
    'USER_ADDR':'<fake_address>@gmail.com',
    'USER_NICKNAME':'kWordSentry',
    'USER_PASS':'<u need to apply>',
    'RECV_ADDR':['<email>@meow.com'] # Must be a list.
    }
*You need to apply for 'An App password' An App password is a 16-digit passcode that gives a non-Google app or device permission to access your Google Account.
*https://support.google.com/accounts/answer/6010255?hl=en&visit_id=637896899107643254-869975220&p=less-secure-apps&rd=1#zippy=%2Cuse-an-app-password
'''
MAIL = {
    'HOST':'smtp.gmail.com',
    'PORT':'587',
    'TLS': True,
    'SSL': False,
    'USER_ADDR':'<fake_address>@gmail.com',
    'USER_NICKNAME':'kWordSentry',
    'USER_PASS':'<u need to apply>',
    'RECV_ADDR':['<email>@meow.com'] # Must be a list.
    }

'''
Alarm: ServerChan Turbo for Wechat alarm module. You need to apply a APIKEY. Please visit:
https://sct.ftqq.com/
Thanks to them.
'''
APIKEY='xxxxx'

'''
HEADER for requests lib.
'''
HEADER = {
    'Accept':'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
    } 
