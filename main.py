from selenium import webdriver
from pages.login_page import LoginPage
import time
import logging
import os
from datetime import datetime

# Configurar log
logging.basicConfig(filename="logs/login_log.txt", level=logging.INFO)

try:
    driver = webdriver.Chrome()
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    time.sleep(2)
    assert "inventory" in driver.current_url
    logging.info("✅ Login realizado com sucesso.")

    # Screenshot
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/login_{timestamp}.png")

except Exception as e:
    logging.error(f"❌ Erro durante o login: {e}")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"screenshots/erro_{timestamp}.png")

finally:
    driver.quit()
