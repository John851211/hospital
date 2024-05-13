#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import sys

driver = webdriver.Chrome()
# 設定隱式等待時間為10秒
driver.implicitly_wait(1000)

URL = "https://reg.ntuh.gov.tw/WebAdministration/DoctorServiceQueryByDrID.aspx?HospCode=T0&QueryID=000793"
 
identitycard = ""
year = ""

mouth = ""

day = ""

#開啟網頁
driver.get(URL)

#視窗最大化
driver.maximize_window()

try:
    diagnosis = driver.find_element(By.ID,"DoctorServiceListInSeveralDaysInput_GridViewDoctorServiceList_ctl06_AdminTextShow")
    diagnosis.send_keys(Keys.ENTER)
    print("pass")

except:
       print("Error")


time.sleep(0.3)

try:
    button1 = driver.find_element(By.ID,"txtIuputID")
    button1.send_keys(identitycard)
except:
       print("Error")



button2 = driver.find_element(By.XPATH,"/html/body/div[1]/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/label")
button2.click()

time.sleep(0.3)
button3 = driver.find_element(By.NAME,"ddlBirthYear")
button3.send_keys(year)
time.sleep(0.3)
button4 = driver.find_element(By.NAME,"ddlBirthMonth")
button4.send_keys(mouth)
time.sleep(0.3)
button5 = driver.find_element(By.NAME,"ddlBirthDay")
button5.send_keys(day)


time.sleep(1000)
