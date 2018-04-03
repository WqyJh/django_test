# Django 中的单元测试和集成测试示例

Django 中编写单元测试需要继承 `django.test.TestCase`, 并编写 `testXXX()` 测试方法，使用 `self.client` 访问页面，断言返回值。

Django 中编写集成测试需要继承 `django.contrib.staticfiles.testing.StaticLiveServerTestCase`, 并创建一个 selenium 的 WebDriver, 在 `testXXX()` 方法中使用 selenium 访问、操作页面，断言返回值。

## Dependency

Python 3.5.4rc1

```bash
pip install Django selenium
```

## Run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py test
```