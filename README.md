# kWordSentry

这是一个可以定时监听网页关键词消失并通知你的脚本。你可以用它来通过邮件或者微信提醒你抢票抢货。



## 功能

可以处理多个URL，通过正则分析关键词，若关键词无法匹配就会给你发送消息。

![kWordSentry](https://raw.githubusercontent.com/restkhz/blogImages/main/img/20220623231237.png "kWordSentry")

可以定义为邮件提示或者是微信提示。当然你也可以自己编写模块。

## TODO

1. 只支持HTTP GET，没去做POST。
2. Cookie只能到headers里去设置，但是那是全局的。还不太方便监听特定一个需要登录的URL。

3. I/O密集，还没有多线程。没有测试过上百条URL的时候会怎么样。当然大概也用不着，以后再说吧。

4. 由于只关注什么不见了，无法判断页面是否增加了什么。虽然办法想好了用xpath之类的但是加进去以后就是另一个东西了。想想csrf_token之类的，看来还得选择区域。头大。
5. 没有像样的UI，添加监听内容不方便。

还需要再思考正则是否必要。使用正则表达式解析HTML不是一个好的选择（如果你知道这是克苏鲁之道）与此同时我不想用xpath让它太麻烦。

## 配置与使用

主要是`config.py`和`urllist.py`

`config.py`

```python
'''
休眠时间，整形数据。单位为秒。
'''
DURATION = 600

'''
使用的提示器是什么，可以是_sendMail也可以是_serverChan，或者你也可以用list表示多种消息提示。
比如ALARM='_sendMail' 或者 ALARM=['_sendMail', '_serverChan']
'''
#ALARM='_sendMail'
ALARM='_serverChan'

'''
邮件提示器配置，这里是gmail的模板。
如果你是国内邮箱如QQ，163等用户，你需要开放SMTP授权，然后会有SMTP独立的密码。自己去查“xx邮箱 smtp”。教程很多，几分钟搞定。
MAIL = {
    'HOST':'smtp.gmail.com',
    'PORT':'587',
    'TLS': True,	# 如果是587端口，通常是支持TLS的，这里是True。
    'SSL': False,	# 如果端口是465，这里改成True。SMTP over SSL。
    'USER_ADDR':'<fake_address>@gmail.com', # 发信人的邮箱账号，登陆用。
    'USER_NICKNAME':'kWordSentry', # 你自己的昵称，无所谓的。
    'USER_PASS':'<u need to apply>', # 申请到的SMTP密码
    'RECV_ADDR':['<email>@meow.com'] # Must be a list.必须是列表，可以给多人发送。
    }
*Gmail你需要有二次验证后申请应用独立密码，使用应用独立密码在这里登录。
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
Server酱提示器，可以给微信发送消息。
访问https://sct.ftqq.com/申请APIKEY，很快的。
感谢他们。
'''
APIKEY='xxxxx'

'''
HEADER for requests lib.
给requests库用的头文件，简单模仿一下浏览器。
能用就别改了。
'''
HEADER = {
    'Accept':'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
    } 


```

`urllist.py`

例如我想监听我的博客有没有删除一句话`我比较喜欢使用requests库`

```python
urllist = {
    'https://blog.restkhz.com/post/kwordsentry':'我比较喜欢使用requests库'
    #'https://blog.restkhz.com/post/kwordsentry':'<p>.*request.*</p>' 你也可以使用正则像这样
    }
```

例如我想监听`https://www.jellycat.com/eu/amuseable-coffeetogo-bag-a4cofb/`是否有货，我们只需要关注HTML是否还存在More on the way。

```python
urllist = {
    'https://www.jellycat.com/eu/amuseable-coffeetogo-bag-a4cofb/':'More on the way'
    }
```

如果一切都准备好了，那么启动就好：

```
python kWordSentry.py
```

