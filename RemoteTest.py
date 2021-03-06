
#import time
#time.sleep(60)
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test(unittest.TestCase):

   def setUp(self):
       #self.driver = webdriver.Remote(command_executor='http://hub:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX) 
       #self.driver = webdriver.Remote(command_executor='http://10.20.56.18:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)             
       self.driver=webdriver.Firefox()
       self.driver.implicitly_wait(30)        
       self.verificationErrors = []        
       self.driver.maximize_window()        
       self.driver.delete_all_cookies() 
   
   def testName(self):
       self.driver.get("http://www.termpaperwarehouse.com/")
       print self.driver.title
   
   def tearDown(self):
       self.driver.quit()

if __name__ == "__main__":
   #import sys;sys.argv = ['', 'Test.testName']
   unittest.main()
