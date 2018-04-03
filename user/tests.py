import json

from django.test import TestCase
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from .models import User


class UserTest(TestCase):
    def setUp(self):
        self.user1 = {'username': 'user1', 'password': 'pass1'}
        self.user2 = {'username': 'user2', 'password': 'pass2'}
        User.objects.create(**self.user1)
        User.objects.create(**self.user2)

    def test_index(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_get(self):
        response = self.client.get('/get')
        self.assertEqual([self.user1, self.user2], json.loads(response.content.decode('utf-8')))

    def test_delete(self):
        response = self.client.get('/delete', data={'username': self.user1['username']})
        self.assertEqual('success', response.content.decode('utf-8'))
        self.assertEqual(1, User.objects.count())


class UserCreateTest(StaticLiveServerTestCase):
    def setUp(self):
        self.userdata = {'username': 'user1', 'password': 'pass1'}
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_create(self):
        # 加载 index 页面
        self.browser.get(self.live_server_url)
        # 填写用户名
        self.browser.find_element_by_id("username").send_keys(self.userdata['username'])
        # 填写密码
        self.browser.find_element_by_id('password').send_keys(self.userdata['password'])
        # 提交表单
        self.browser.find_element_by_id('submit').click()
        # 返回成功
        self.assertIn('success', self.browser.page_source)

        # 查询数据库
        user = User.objects.first()
        # 数据库里与我们创建的一致
        self.assertEqual(self.userdata['username'], user.username)
        self.assertEqual(self.userdata['password'], user.password)
