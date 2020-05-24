from  selenium  import  webdriver

profiles= r"C:\Users\86185\AppData\Roaming\Mozilla\Firefox\Profiles\frolqlp9.default"

files=webdriver.FirefoxProfile(profiles)
driver=webdriver.Firefox(files)
driver.get("https://www.baidu.com")