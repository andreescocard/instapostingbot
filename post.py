from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import os

path = os.getcwd()
username = ""
passwd = ""
driverpth = ""
photopath = path+"\\test.jpeg" #examp "C:\\Users\\alire\\PycharmProjects\\instagrambot2\\logo.png"
phototext = ""

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
#mobile_emulation = {"deviceName": "Nexus 5"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
driver.find_element_by_name("username").send_keys(username)
time.sleep(0.5)
driver.find_element_by_name("password").send_keys(passwd)
time.sleep(0.5)
driver.find_element_by_id("loginForm").submit()
time.sleep(6)
driver.find_element_by_xpath('//button[contains(text(), "Agora não")]').click()
time.sleep(3)
driver.find_element_by_xpath('//button[contains(text(), "Cancelar")]').click()
time.sleep(4)
driver.find_element_by_xpath("//div[@role='menuitem']").click()
time.sleep(0.5)
pyautogui.write(photopath)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
driver.find_element_by_xpath('//button[contains(text(), "Avançar")]').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea').send_keys("teste")
time.sleep(2)
driver.find_element_by_xpath('//button[contains(text(), "Compartilhar")]').click()
'''

#still works 04102020 - scrolling soon
while 1:
    time.sleep(1)
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
    try:
        #remove random dialog
        driver.find_element_by_xpath('//button[contains(text(), "Agora não")]').click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
        break
    except:
        pass

driver.find_element_by_xpath("//div[@role='menuitem']").click()
time.sleep(1.5)
autoit.win_active("Open") #open can change by your os language if not open change that
time.sleep(4)
autoit.control_send("Open", "Edit1", photopath)
time.sleep(1.5)
autoit.control_send("Open", "Edit1", "{ENTER}")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea").send_keys(phototext)
time.sleep(1)
driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
time.sleep(4)
driver.close()'''