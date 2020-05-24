from  selenium  import  webdriver
import   time


driver=webdriver.Firefox()
driver.get("http://langfang.ganji.com/")
time.sleep(2)
driver.find_element_by_link_text("租房").click()

time.sleep(2)

driver.close()
t1 = driver.title
print(t1)

# #获取当前title
# t = driver.title
# print(t)
#
# #获取当前窗口
# h =driver.current_window_handle
# print(h)
#
# #获取所有的窗口
# all=driver.window_handles
# print(all)
#
# #获取当前窗口
# now = all[-1]
# print(now)
#
# driver.switch_to_window(now)
#
# time.sleep(2)
# driver.find_element_by_link_text("大厂").click()
#
# time.sleep(2)
# driver.quit()