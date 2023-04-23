import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage
from selenium.common.exceptions import TimeoutException

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome()
    pytest.driver.get('https://b2c.passport.rt.ru/auth')

    yield

    pytest.driver.quit()


def test_show_auth_page(web_browser):
    # Check auth page opens
    page = AuthPage(web_browser)
    assert pytest.driver.find_element(By.XPATH, "//h1[contains(text(),'Авторизация')]")


def test_change_auth_method(web_browser):
    page = AuthPage(web_browser)
    pytest.driver.find_element(By.ID, "t-btn-tab-phone").click()
    pytest.driver.find_element(By.ID, "t-btn-tab-mail").click()
    pytest.driver.find_element(By.ID, "t-btn-tab-login").click()
    pytest.driver.find_element(By.ID, "t-btn-tab-ls").click()
    assert WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, "t-btn-tab-phone")))
    assert WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, "t-btn-tab-mail")))
    assert WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, "t-btn-tab-login")))
    assert WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, "t-btn-tab-ls")))

def test_login_button(web_browser):
    page = AuthPage(web_browser)
    pytest.driver.find_element(By.ID, "kc-login").click()
    assert WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, "kc-login")))

def test_user_agreement(web_browser):
    page = AuthPage(web_browser)
    pytest.driver.find_element(By.LINK_TEXT, 'пользовательского соглашения').click()
    assert WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'пользовательского соглашения')))


def test_forgot_password_button(web_browser):
    page = AuthPage(web_browser)
    try:
        element = pytest.driver.find_element(By.ID, 'forgot_password')
        element.click()
    except TimeoutException:
        assert WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.ID, 'forgot_password')))

def test_vk_icon(web_browser):
    page = AuthPage(web_browser)
    try:
        element = pytest.driver.find_element(By.ID, 'oidc_vk')
        element.click()
    except TimeoutException:
        assert WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, 'oidc_vk')))

def test_ok_icon(web_browser):
    page = AuthPage(web_browser)
    try:
        element = pytest.driver.find_element(By.ID, 'oidc_ok')
        element.click()
    except TimeoutException:
        assert WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, 'oidc_ok')))

def test_mail_icon(web_browser):
    page = AuthPage(web_browser)
    try:
        element = pytest.driver.find_element(By.ID, 'oidc_mail')
        element.click()
    except TimeoutException:
        assert WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, 'oidc_mail')))

def test_google_icon(web_browser):
    page = AuthPage(web_browser)
    try:
        element = pytest.driver.find_element(By.ID, 'oidc_google')
        element.click()
    except TimeoutException:
        assert WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, 'oidc_google')))

def test_yandex_icon(web_browser):
    page = AuthPage(web_browser)
    try:
        element = pytest.driver.find_element(By.ID, 'oidc_ya')
        element.click()
    except TimeoutException:
        assert WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, 'oidc_ya')))

def test_register_button(web_browser):
    page = AuthPage(web_browser)
    try:
        element = pytest.driver.find_element(By.ID, 'kc-register')
        element.click()
    except TimeoutException:
        assert WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.ID, 'kc-register')))