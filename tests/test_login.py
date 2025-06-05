from selenium import webdriver
from pages.login_page import LoginPage
import pytest
import os
from datetime import datetime


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login_sucesso(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url


def test_login_falha(driver):
    login = LoginPage(driver)
    login.load()
    login.login("usuariovazio", "senhaerrada")

    try:
        assert "inventory" not in driver.current_url
    except AssertionError:
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f"screenshots/erro_{timestamp}.png")
        raise
