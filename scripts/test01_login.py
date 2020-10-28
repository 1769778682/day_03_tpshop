"""
定义接口测试用例
使用unittest
1.导包
2.创建测试类
    2.1前置处理
    2.2后置处理
    2.3创建测试方法
"""


# 导包
import requests
import unittest
from api.login import LoginAPI


class TestLogin(unittest.TestCase):
    """登录接口测试类"""

    def setUp(self):
        self.login_api = LoginAPI()
        self.session = requests.Session()

    def tearDown(self):
        if self.session:
            self.session.close()

    def test_success(self):
        """登陆成功"""
        response = self.login_api.get_verify_code(self.session)
        self.assertEqual(200, response.status_code)
        self.assertIn('image', response.headers.get('Content-Type'))

        # response = self.login_api.login(self.session, username, password, verify_code)
        response = self.login_api.login(self.session, "13812345678", "123456", "8888")
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("status"))
        self.assertIn("登陆成功", response.json().get("msg"))

    def test_exist(self):
        """账号不存在"""
        response = self.login_api.get_verify_code(self.session)
        self.assertEqual(200, response.status_code)
        self.assertIn('image', response.headers.get('Content-Type'))

        # response = self.login_api.login(self.session, username, password, verify_code)
        response = self.login_api.login(self.session, "13812345679", "123456", "8888")
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get("status"))
        self.assertIn("账号不存在", response.json().get("msg"))

    def test_er(self):
        """密码错误"""
        response = self.login_api.get_verify_code(self.session)
        self.assertEqual(200, response.status_code)
        self.assertIn('image', response.headers.get('Content-Type'))

        # response = self.login_api.login(self.session, username, password, verify_code)
        response = self.login_api.login(self.session, "13812345678", "123457", "8888")
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, response.json().get("status"))
        self.assertIn("密码错误", response.json().get("msg"))