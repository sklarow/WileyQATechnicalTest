from selenium.webdriver.common.by import By


class Locators:
    # --- Login Page Locators ---
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'body > main > header > nav > div.visible-lg-block > div > div > button')
    LOGIN_TEXTBOX = (By.ID, 'login-form__login')
    NEXT_BUTTON = (By.CSS_SELECTOR, '#js-modal-login-member > div > div > div.modal__footer > '
                                    'button.button-default.js-login-form-submit')
    PASSWORD_TEXTBOX = (By.ID, 'login-form__password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#js-modal-login-member > div > div > div.modal__footer > '
                                      'button.button-default.js-login-form-submit')

    # --- Main Page Page Locators ---
    LOGIN_NAME_TEXT = (By.CSS_SELECTOR, 'body > main > header > nav > '
                                        'div.navbar-collapse.no-print.header__content.js'
                                        '-sidebar-menu > ul > '
                                        'li.header__menu-item.header__menu-item--user-menu.text'
                                        '-center.js-menu-item '
                                        '> a > span')