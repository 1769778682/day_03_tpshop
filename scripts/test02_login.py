# 导包
import requests
import unittest
import app
from api.login import LoginAPI
import json
from parameterized import parameterized


def para_data():
    file = app.BASE_DIR + '/data/login.json'
    test_data = []
    with open(file, encoding='utf-8') as f:
        json_data = json.load(f)  # 加载json文件
        for i in json_data:
            username = i.get('username')
            password = i.get('password')
            verify_code = i.get('verify_code')
            content_type = i.get('content_type')
            status_code = i.get('status_code')
            status = i.get('status')
            msg = i.get('msg')
            test_data.append((username, password, verify_code,
                              content_type, status_code, status, msg))
            print(test_data)
    return test_data


class TestLogin02(unittest.TestCase):
    """登录接口测试类"""

    def setUp(self):
        self.login_api = LoginAPI()
        self.session = requests.Session()

    def tearDown(self):
        if self.session:
            self.session.close()

    @parameterized.expand(para_data())
    def test_login(self, username, password, verify_code,
                   content_type, status_code, status, msg):
        """登陆成功"""

        # 发送获取验证码情求
        response = self.login_api.get_verify_code(self.session)
        # 断言获取验证码
        self.assertEqual(200, response.status_code)
        self.assertIn(content_type, response.headers.get('Content-Type'))

        # 发送登陆请求
        response = self.login_api.login(self.session, username, password, verify_code)
        # response = self.login_api.login(self.session, "13812345678", "123456", "8888")
        # 断言登录
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status, response.json().get("status"))
        self.assertIn(msg, response.json().get("msg"))
