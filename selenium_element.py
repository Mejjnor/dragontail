from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException
import time


class Locator(object):
    def __init__(self, by_, identifier_):
        self.by = by_
        self.identifier = identifier_

class SeleniumElement(object):    
    def __init__(self, driver_, locator_):
        self.driver = driver_
        self.locator = locator_
    
    def find(self):
        return self.driver.find_element(self.locator.by,
                                        self.locator.identifier)
    
    def wait_for(self, timeout):
        '''
        @param timeout: time to wait in seconds
        '''
        end_time = datetime.now() + timedelta(seconds=timeout)
        while datetime.now() < end_time:
            try:
                self.find()
                break
            except NoSuchElementException:
                time.sleep(0.05)
    
    def click(self):
        self.find().click()
    
    def send_keys(self, text):
        self.find().send_keys(text)
    
    def get_text(self):
        return self.find().text
    
    
