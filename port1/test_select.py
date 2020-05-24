#coding:utf-8
from  selenium  import  webdriver

from  selenium.webdriver.common.action_chains import    ActionChains
import  time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

driver.implicitly_wait(10)

mouse = driver.find_element_by_id("s-usersetting-top")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()


driver.find_element_by_id("nr_3").click()

driver.find_element_by_link_text("保存设置").click()
time.sleep(3)

t = driver.switch_to_alert()
t.accept()

#登陆禅道javascript: $('#account').val('admin') $([name="password"]).val('Yoyo123456') $('#submit').click()
