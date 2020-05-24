from  selenium  import  webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import  time
driver=webdriver.Firefox()

driver.get("https://mail.126.com/")
time.sleep(2)

# name = driver.find_elements_by_tag_name("iframe")[0]
# driver.switch_to.frame(name)
driver.switch_to.frame(3)
# frame = driver.find_elements_by_tag_name("iframe")[0]
#
#
# driver.switch_to.frame(frame)
driver.find_element_by_name("email").send_keys("nihao")
time.sleep(2)

driver.title