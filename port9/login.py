class  LoginZenDao():
    # def  __init__(self,driver):
    #     self.driver=driver

    def  login_user(self,driver):
        driver.get("http://49.235.92.12:8080/zentao/user-login.html")
        driver.find_element_by_xpath('//*[@id="account"]').send_keys("admin")
        driver.find_element_by_xpath('//*[@name="password"]').send_keys("Yoyo123456")
        # driver.find_element_by_css_selector('[type="password"]').send_keys("Yoyo123456")
        driver.find_element_by_xpath('//*[@id="submit"]').click()

if __name__ =='__main__':
    from  selenium  import  webdriver
    driver=webdriver.Firefox()
    l =LoginZenDao()
    l.login_user(driver)