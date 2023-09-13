import re
import numpy as np
import time
import logging
import sys

import requests
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import NameSpace
logging.basicConfig(level=logging.INFO)


def waitingTime(wt = 1):
    return time.sleep(0.2*wt)

def inturrupt():
    sys.exit(1)

class PostingManagment():
    def __init__(self, elements, cssid):
        self.web        = elements[0]
        self.portal     = elements[1]
        self.loginPage  = elements[2]
        self.account    = elements[3]
        self.pswrd      = elements[4]
        self.homePage   = elements[5]

        self.loginNicknameCssId = cssid[0]
        self.loginPswrdCssId    = cssid[1]
        self.loginSubmitCssId   = cssid[2]
        self.checkLoginCssId    = cssid[3]
        self.inputHolder        = cssid[4]
        self.logoutCssId        = cssid[5]


    def login(self):
        try:
            logging.info("Connecting {}...".format(self.web))
            self.browser = webdriver.Safari()  # open the browser
            # browser = webdriver.Chrome()#need to download chrome driver
            self.browser.get(self.loginPage)
        except Exception as e:
            logging.info(e, "Cannot connect plurk.")
            self.quitBrowser()
            inturrupt()
        try:
            logging.info("Login...")
            self.browser.find_element_by_id(self.loginNicknameCssId).send_keys(self.account)
            waitingTime()
            self.browser.find_element_by_id(self.loginPswrdCssId).send_keys(self.pswrd)
            waitingTime(0.5)
            self.browser.find_element_by_id(self.loginSubmitCssId).send_keys(Keys.ENTER)
        except Exception as e:
            logging.info(e, "Cannot login.")
            self.quitBrowser()
            inturrupt()

    def idCheck(self):
        print("Checking login result...")
        waitingTime(5)
        titleCheck = self.browser.find_element_by_css_selector(self.checkLoginCssId)
        #logging.info("title = %s" % titleCheck)
        print(titleCheck.text)
        if (titleCheck.text == self.account):
            logging.info("Login successfully!")
        else:
            self.quitBrowser()
            logging.info("Wrong account or password.")

    def quitBrowser(self):
        waitingTime(10)
        self.browser.quit()

    def post(self):
        try:
            self.browser.find_element_by_id(self.inputHolder).send_keys(NameSpace.POST_CONTENT)
            waitingTime()
            self.browser.find_element_by_css_selector('div[class="click submit_img q_says"]').send_keys(Keys.ENTER)
        except Exception as e:
            logging.info(e, "Cannot post.")
            self.quitBrowser()
            inturrupt()

    def logout(self):
        try:
            logging.info("logout")
            #self.browser.find_element_by_css_selector(self.checkLoginCssId).click()
            waitingTime(5)
            a = self.browser.find_element_by_link_text(self.logoutCssId)
            print(a.text)
            a.click()
        except Exception as e:
            logging.info(e, "Cannot logout.")
            self.quitBrowser()
            inturrupt()



if __name__ == '__main__':
    plurk = PostingManagment(NameSpace.PLURK_ELEMENTS, NameSpace.PLURK_CSSID)
    plurk.login()
    waitingTime(5)
    plurk.idCheck()
    waitingTime()
    # plurk.post()
    waitingTime(5)
    plurk.logout()
    waitingTime(5)
    plurk.quitBrowser()
