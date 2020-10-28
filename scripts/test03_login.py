# 导包
import requests
import unittest
from api.login import LoginAPI
from utils import Mysql
from parameterized import parameterized


def para_data():
    sql = 'select * from t_login'
    db_data = Mysql.exe_sql(sql)
    test_data = []
    # with open(sql, encoding='utf-8') as f:
    #     json_data = json.load(f)  # 加载json文件
    for i in db_data:
        username = i[2]
        password = i[3]
        verify_code = i[4]
        content_type = i[6]
        status_code = i[5]
        status = i[7]
        msg = i[8]

        test_data.append((username, password, verify_code,
                          content_type, status_code, status, msg))
        print(test_data)
    return test_data


class TestLogin03(unittest.TestCase):
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
