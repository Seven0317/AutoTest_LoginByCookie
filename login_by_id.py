# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/4/22 22:04


import os
import time
import yaml
from selenium import webdriver


def login_by_id():
    """ Login by ID & PWD
        Store cookie before the login in cookie_before.yaml
        Store cookie after login in cookie_after.yaml
    """

    url = "https://www.jianshu.com/sign_in"
    login_id = "YOUR ID"
    login_pwd = "YOUR PWD"

    # Get current directory path of id_login.py
    dirPath = os.path.split(os.path.realpath(__file__))[0]
    # Create file path for storing cookie
    yamlPath1 = os.path.join(dirPath, "cookie_before.yaml")
    yamlPath2 = os.path.join(dirPath, "cookie_after.yaml")

    # Launch the browser of Firefox and open the url page
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    time.sleep(2)

    # Get cookies before login the personal page
    cookie_before = driver.get_cookies()
    # Store cookie before into cookie_before.yaml
    with open(yamlPath1, 'w', encoding='utf-8') as fw:
        yaml.dump(cookie_before, fw)

    # Login personal page with ID & PWD
    driver.find_element_by_id("session_email_or_mobile_number").clear()
    driver.find_element_by_id("session_email_or_mobile_number").send_keys(login_id)

    driver.find_element_by_id("session_password").clear()
    driver.find_element_by_id("session_password").send_keys(login_pwd)

    driver.find_element_by_id("sign-in-form-submit-btn").click()

    # Enough time sleep for interaction before login successfully and stable
    time.sleep(30)

    # Get cookies after login the personal page
    cookie_after = driver.get_cookies()
    # Store cookie after into cookie_before.yaml
    with open(yamlPath2, 'w', encoding='utf-8') as fw:
        yaml.dump(cookie_after, fw)

    # Exit from the page and close the browser
    driver.quit()


if __name__ == "__main__":
    login_by_id()
