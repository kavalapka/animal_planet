from django.test import TestCase
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from animal_app.models import Animal


class AnimalViewTests(TestCase):
    def test_animal_list_view(self):
        response = self.client.get('/animal/')
        self.assertEqual(response.status_code, 200)


class AnimalDetailView(TestCase):
    def test_animal_detail_view(self):
        new_animal = Animal.objects.create(name='test', number='1', owner_id='1')
        response = self.client.get('/animal/{}/'.format(new_animal.id))
        self.assertEqual(response.status_code, 200)


class UsersSeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(UsersSeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(UsersSeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('http://127.0.0.1:8000/admin/')
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('test')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        red = self.client.get(self.selenium.current_url)
        self.assertEqual(red.status_code, 302)
