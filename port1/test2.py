from  selenium  import  webdriver
import  time
driver=webdriver.Firefox()

driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("武炎浩")
driver.find_element_by_id("kw").click()

time.sleep(3)
driver.back()

time.sleep(3)
driver.forward()
time.sleep(2)
driver.quit()