from  selenium  import  webdriver

import  unittest

from  port9.login import  LoginZenDao

class   LoginCase(unittest.TestCase):

    def  setUp(self):
        self.driver=webdriver.Firefox()

        self.zendao =LoginZenDao.login_user()

    def  test1(self):
        self.zendao(self.driver)




if  __name__ == '__main__':
    unittest.main()