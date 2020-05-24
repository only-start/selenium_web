from  selenium  import   webdriver
import  time
import unittest
class LoginTest(unittest.TestCase):
    def  setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://49.235.92.12:8080/zentao/user-login.html")
    def tearDown(self):
        self.driver.quit()


    def get_login_success(self):
        try:
            t=self.driver.find_element_by_css_selector(".user-name").text
            print(t)
            return t
        except:
            return  ""

    def  test_1(self):
        '''这是登陆成功的案例'''

        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="account"]').send_keys("admin")
        self.driver.find_element_by_xpath('//*[@name="password"]').send_keys("Yoyo123456")
        # driver.find_element_by_css_selector('[type="password"]').send_keys("Yoyo123456")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(3)
        t = self.get_login_success()
        print(t)
        self.assertEqual(t,'admin')#断言成功截图
    def  test_2(self):
        '''这是登陆失败的案例'''

        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="account"]').send_keys("hello")
        self.driver.find_element_by_xpath('//*[@name="password"]').send_keys("123456")
        # driver.find_element_by_css_selector('[type="password"]').send_keys("Yoyo123456")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(3)
        t =self.get_login_success()
        print(t)
        self.assertEqual(1,2) #断言失败截图

    # @classmethod
    #
    # def tearDownClass(cls):
    #     cls.driver.quit()

if __name__ == "__main__":
    unittest.main()