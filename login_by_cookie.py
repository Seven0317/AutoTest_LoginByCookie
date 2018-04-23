# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/4/22 22:06

import os
import time
import yaml
from selenium import webdriver


def login_by_cookie():
    """Login with cookies
    """

    url = "https://www.jianshu.com/sign_in"
    dirPath = os.path.split(os.path.realpath(__file__))[0]
    cookie_path = os.path.join(dirPath, "cookie_after.yaml")
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)

    # Delete all cookies
    driver.delete_all_cookies()
    # Read and load cookies from cookie_after.yaml
    with open(cookie_path, "r", encoding="utf-8") as fr:
        cookies = yaml.load(fr)
    # Add cookie needed and add add key 'expiry' to the cookies for this webpage if lacking of expire time
    for cookie in cookies:
        for k in ('name', 'value', 'domain', 'path', 'expire'):
            if k not in list(cookie.keys()):
                if k == 'expire':
                    t = time.time()
                    cookie[k] = int(t)
        driver.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path', 'expire') if k in cookie})
    # Need refresh the website
    driver.refresh()
    time.sleep(5)
    # logout the webPage
    driver.quit()


if __name__ == "__main__":
    login_by_cookie()
