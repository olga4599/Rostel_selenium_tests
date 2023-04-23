import pytest

from pages.auth_page import AuthPage
from settings import email, password, phone

# Тест на закрузку основной страницы
def test_auth_page_opens(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    assert page.auth_page.is_visible()

# Тест возможности переключения на авторизацию через телефон
def test_phone_auth_btn(web_browser):
    page = AuthPage(web_browser)
    page.phone_auth.click()
    assert page.phone_auth.is_clickable()

# Тест возможности переключения на авторизацию через почту
def test_mail_auth_btn(web_browser):
    page = AuthPage(web_browser)
    page.mail_auth.click()
    assert page.mail_auth.is_clickable()

# Тест возможности переключения на авторизацию через логин
def test_login_auth_btn(web_browser):
    page = AuthPage(web_browser)
    page.login_auth.click()
    assert page.login_auth.is_clickable()

# Тест возможности переключения на авторизацию через лицевой счет
def test_ls_auth_btn(web_browser):
    page = AuthPage(web_browser)
    page.ls_auth.click()
    assert page.ls_auth.is_clickable()

# Тест входа с корректными данными
def test_correct_login(web_browser):
    page = AuthPage(web_browser)
    page.username.send_keys(email)
    page.password.send_keys(password)
    page.btn.click()
    page.wait_page_loaded()
    assert page._web_driver.save_screenshot('login_correct.png')

# Тест входа с некорректными данными
def test_login_with_incorrect_data(web_browser):
    page = AuthPage(web_browser)
    page.username.send_keys('test111@gmail.com')
    page.password.send_keys("111")
    page.btn.click()
    page.wait_page_loaded()
    assert page.error_message.is_visible()

# Тест входа по номеру телефона
def test_auth_with_phone(web_browser):
    page = AuthPage(web_browser)
    page.phone_auth.click()
    page.username.send_keys(phone)
    page.password.send_keys(password)
    page.btn.click()
    assert page.btn.wait_to_be_clickable()

# Тест входа по электронной почте
def test_auth_with_email(web_browser):
    page = AuthPage(web_browser)
    page.mail_auth.click()
    page.username.send_keys(email)
    page.password.send_keys(password)
    page.btn.click()
    assert page.btn.wait_to_be_clickable()

# Тест входа по логину
def test_auth_with_login(web_browser):
    page = AuthPage(web_browser)
    page.login_auth.click()
    page.username.send_keys('test')
    page.password.send_keys(password)
    page.btn.click()
    assert page.btn.wait_to_be_clickable()

# Тест кнопки восстановления пароля
def test_forgot_password(web_browser):
    page = AuthPage(web_browser)
    page.forgot_password_btn.click()
    page.wait_page_loaded()
    assert page.forgot_password_page.is_presented()

# Тест кнопки Пользовательского соглашения
def test_user_agreement(web_browser):
    page = AuthPage(web_browser)
    page.user_agreement.click()
    assert page.user_agreement.is_clickable()

# Тест кнопки Зарегестрироваться
def test_register_btn(web_browser):
    page = AuthPage(web_browser)
    page.register_btn.click()
    page.wait_page_loaded()
    assert page.register_page.is_presented()

# Тест кнопки соц.сетей ВК
def test_vk_btn(web_browser):
    page = AuthPage(web_browser)
    page.vk_btn.click()
    page.wait_page_loaded()
    assert page.vk_page.is_presented()

# Тест кнопки соц.сетей Одноклассники
def test_ok_btn(web_browser):
    page = AuthPage(web_browser)
    page.ok_btn.click()
    page.wait_page_loaded()
    assert page.ok_page.is_presented()

# Тест кнопки соц.сетей Майл ру
def test_mail_ru_btn(web_browser):
    page = AuthPage(web_browser)
    page.mail_ru_btn.click()
    page.wait_page_loaded()
    assert page.mail_ru_page.is_presented()

# Тест кнопки соц.сетей Google
def test_google_btn(web_browser):
    page = AuthPage(web_browser)
    page.google_btn.click()
    page.wait_page_loaded()
    assert page.google_page.is_presented()

# Тест кнопки соц.сетей Яндекс
def test_yandex_btn(web_browser):
    page = AuthPage(web_browser)
    page.yandex_btn.click()
    page.wait_page_loaded()
    assert page.yandex_page.is_presented()