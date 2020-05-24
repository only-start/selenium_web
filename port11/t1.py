from  selenium.webdriver.support.wait import   WebDriverWait
from  selenium.webdriver.common.by import   By
from  selenium  import  webdriver
import  time
import  unittest
class CreateBug(unittest.TestCase):

    def  setUp(self):
        self.driver=webdriver.Firefox()

        self.driver.get("http://49.235.92.12:8080/zentao/user-login.html")


    def test_create(self):


        ele1 = WebDriverWait(self.driver, 10,1).until(lambda x: x.find_element(By.ID,"account"))
        ele1.send_keys("admin")
        ele2 = WebDriverWait(self.driver, 10,1).until(lambda x: x.find_element(By.NAME,"password"))
        ele2.send_keys("Yoyo123456")
        ele3 = WebDriverWait(self.driver, 10,1).until(lambda x: x.find_element(By.ID,"submit"))
        ele3.click()
        ele4 = WebDriverWait(self.driver, 10,1).until(lambda x: x.find_element(By.LINK_TEXT,"测试"))
        ele4.click()
        ele5 = WebDriverWait(self.driver, 10,1).until(lambda x: x.find_element(By.XPATH,"html/body/header/div[2]/div/nav/ul/li[1]/a"))
        ele5.click()
        ele6 = WebDriverWait(self.driver, 10,1).until(lambda x: x.find_element(By.XPATH,"html/body/main/div/div[2]/div[3]/a[3]"))
        ele6.click()
        # ele7 = WebDriverWait(driver, 10,1).until(lambda x: x.find_element(By.XPATH,"html/body/main/div/div/div/form/table/tbody/tr[2]/td[2]/div/div[1]/ul"))
        ele7 = WebDriverWait(self.driver, 10,1).until(lambda x: x.find_element(By.CSS_SELECTOR,".chosen-choices"))
        ele7.click()
        # ele8 = WebDriverWait(driver, 10,1).until(lambda x: x.find_element(By.XPATH,"html/body/main/div/div/div/form/table/tbody/tr[2]/td[2]/div/div[1]/div/ul/li"))
        ele8 = WebDriverWait(self.driver, 10,1).until(lambda x: x.find_element(By.CSS_SELECTOR,".active-result.highlighted"))
        ele8.click()
        ele9 = WebDriverWait(self.driver, 10,1).until(lambda x: x.find_element(By.CSS_SELECTOR,"#title"))
        ele9.send_keys("一个提bug的测试用例")

        self.driver.switch_to_frame(1)
        ele10 = WebDriverWait(self.driver, 10,1).until(lambda x: x.find_element(By.CSS_SELECTOR,".article-content>p"))
        body ='''
            打开浏览器，
            发现bug，
            提交bug
        '''
        ele10.send_keys(body)

        self.driver.switch_to_default_content()
        ele10 = WebDriverWait(self.driver, 10,1).until(lambda x: x.find_element(By.CSS_SELECTOR,"#submit"))
        ele10.click()
    def  tearDown(self):
        self.driver.quit()

if  __name__ =='__main__':
    # driver=webdriver.Firefox()
    # c = CreateBug(driver)
    unittest.main()









# driver.find_element_by_link_text("测试").click()
# time.sleep(2)
# driver.find_element_by_link_text("Bug").click()
# time.sleep(2)
# driver.find_element_by_css_selector(".btn.btn-primary").click()
# time.sleep(2)