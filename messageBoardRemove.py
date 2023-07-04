'''
Descripttion: 
version: 1.0.0
Author: Jiang Xinyun
Date: 2023-07-04 11:15:16
LastEditors: Jiang Xinyun
LastEditTime: 2023-07-04 11:21:34
'''
# coding=utf-8
import datetime
import logging
import os
import time
import traceback
 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
 
 
 
# 日志
def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    # Standard output handler
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(logging.Formatter('%(levelname)s - %(name)s:%(lineno)s: %(message)s'))
    log.addHandler(sh)
    return log
logger = get_logger(__file__)
 
 
def work(browser):
    #手机扫码登陆
    qq=550343586
    browser.get('https://user.qzone.qq.com/{}/infocenter?via=toolbar'.format(qq))
    # 暂停用于扫码登录的时间，可适当增加或缩短
    time.sleep(15)
    try:
        # 账号密码登录，此种方式太老了，现在还需要验证码不推荐，请使用上面的扫码登录方式
        # browser.find_element(By.ID,'switcher_plogin').click()
        # browser.find_element(By.ID,'u').clear()
        # #你的qq账号
        # browser.find_element(By.ID,'u').send_keys('你的qq账号')
        # browser.find_element(By.ID,'p').clear()
        # #你的qq密码
        # browser.find_element(By.ID,'p').send_keys('你的账号密码')
        # browser.find_element(By.ID,'login_button').click()
        # time.sleep(2)

        #打开留言板
        writeLog()
        while(True):
            browser.get('https://user.qzone.qq.com/{}/334'.format(qq))
            browser.switch_to.frame('tgb')
            #点击批量管理
            time.sleep(2)
            mouse = browser.find_element(By.ID,'btnToSet')
            ActionChains(browser).move_to_element(mouse).perform()
            time.sleep(1)
            browser.find_element(By.ID,'btnBatch').click()
            browser.find_element(By.ID,'chkSelectAll').click()
            browser.find_element(By.ID,'btnDeleteBatchBottom').click()
            time.sleep(1)
            browser.switch_to.parent_frame()
            time.sleep(2)
            browser.find_element(By.ID,'dialog_main_1').find_element(By.CLASS_NAME,'qz_dialog_layer_op').find_element(By.CLASS_NAME,'qz_dialog_layer_sub').click()
            time.sleep(2)
    except:
        print("failure2")
        print(traceback.format_exc())
        writeLog()
# 写错误日志并截图
def writeLog():
    # 组合日志文件名（当前文件名+当前时间）.比如：case_login_success_20150817192533
    basename = os.path.splitext(os.path.basename(__file__))[0]
    logFile = "log/"+basename + "-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
    logging.basicConfig(filename=logFile)
    s = traceback.format_exc()
    logging.error(s)
    browser.get_screenshot_as_file("./" + logFile + "-screenshot_error.png")
 
 
if __name__ == "__main__":
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(options=chrome_options)  # Chrome界面
    # browser = webdriver.PhantomJS()  # 无界面
    work(browser)
    browser.quit()