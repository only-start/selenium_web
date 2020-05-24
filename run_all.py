import  unittest
from  common  import   HTMLTestRunner
path="D:\ports\\port7"
ruler="t*.py"


discover = unittest.defaultTestLoader.discover(start_dir=path,pattern=ruler)
print(discover)

reportpath=r'D:\ports\re' + 'result.html'

fp =open(reportpath,'wb')

runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                  title="这是一个简单的测试用例报告",
                                  description="这是一个登陆禅道成功和失败的用例")

runner.run(discover)