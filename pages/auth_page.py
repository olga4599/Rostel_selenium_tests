from pages.base import WebPage
from pages.elements import WebElement

import time, os

class AuthPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    # Поле для ввода почты
    username = WebElement(id='username')

    # Поле для ввода пароля
    password = WebElement(id='password')

    # Кнопка для входа
    btn = WebElement(id='kc-login')

    # Сообщение об ошибке при неправильном вводе данных
    error_message = WebElement(id='form-error-message')

    # Кнопка смены пароля
    forgot_password_btn = WebElement(id='forgot_password')

    # Страница восстановления пароля
    forgot_password_page = WebElement(xpath="//h1[contains(text(),'Восстановление пароля')]")

    #Страница авторизации
    auth_page = WebElement(xpath="//h1[contains(text(),'Авторизация')]")

    #Выбор авторизации через телефон
    phone_auth = WebElement(id="t-btn-tab-phone")

    #Выбор авторизации через почту
    mail_auth = WebElement(id="t-btn-tab-mail")

    #Выбор авторизации через логин
    login_auth = WebElement(id="t-btn-tab-login")

    #Выбор авторизации через лицевой счет
    ls_auth = WebElement(id="t-btn-tab-ls")

    #Ссылка на пользовательское соглашение
    user_agreement = WebElement(link_text='пользовательского соглашения')

    # Кнопка Зарегестрироваться
    register_btn = WebElement(id='kc-register')

    # Страница Регистрации
    register_page = WebElement(xpath="//h1[contains(text(),'Регистрация')]")

    # Кнопка ВК
    vk_btn = WebElement(id='oidc_vk')

    # Страница ВК
    vk_page = WebElement(xpath="//b[contains(text(),'ВКонтакте')]")

    # Кнопка Одноклассники
    ok_btn = WebElement(id="oidc_ok")

    # Страница Одноклассники
    ok_page = WebElement(xpath="//div[contains(text(),'Одноклассники')]")

    # Кнопка Mail.ru
    mail_ru_btn = WebElement(id="oidc_mail")

    # Страница Mail.ru
    mail_ru_page = WebElement(xpath="//span[contains(text(),'Мой Мир@Mail.Ru')]")

    # Кнопка Google
    google_btn = WebElement(id="oidc_google")

    # Страница Google
    google_page = WebElement(xpath="//div[contains(text(),'Войдите в аккаунт Google')]")

    # Кнопка Yandex
    yandex_btn = WebElement(id='oidc_ya')

    # Страница Yandex
    yandex_page = WebElement(xpath="//span[contains(text(),'Войдите с Яндекс ID')]")