"""
获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
登录：http://localhost/index.php?m=Home&c=User&a=do_login
"""


# 导包


# 定义类
class LoginAPI:

    def __init__(self):
        self.url_verify = \
            'http://localhost/index.php?m=Home&c=User&a=verify'
        self.url_login = \
            'http://localhost/index.php?m=Home&c=User&a=do_login'

    def get_verify_code(self, session):
        return session.get(self.url_verify)

    def login(self, session, username, password, verify_code):
        login_data = {
            "username": username,
            "password": password,
            "verify_code": verify_code
        }
        return session.post(url=self.url_login, data=login_data)
