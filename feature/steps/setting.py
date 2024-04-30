from appium import webdriver
from typing import Any ,Dict
from appium.options.common import AppiumOptions
from selenium import webdriver
import time
cap:dict[str,any]={
    "platformName":"android",
    "automationName":"uiautomator2",
    "platformVersion":"13",
    "deviceName":"QUPS",
    "app":"C:\\Users\\QUPS-6\\Downloads\\New folder\\google_task.apk"
}
url = 'http://127.0.0.1:4723/wd/hub'

# driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
# time.sleep(3)