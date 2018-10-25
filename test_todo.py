import os
import unittest
from unittest.case import TestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from todo_page import ToDoPage
import logging
import time


class TestClusterPage(TestCase):
    def setUp(self):
        logging.basicConfig(filename="execution_{}.log".format(time.time()),
                            level=logging.DEBUG)
        self.driver = WebDriver()
        self.todo_page = ToDoPage(self.driver)
    
    def test_add_todo(self):
        item_name = "Do Me!!"
        logging.info("Opening ToDo page")
        self.todo_page.navigate_to()
        
        logging.info("Adding a new ToDo item")
        self.todo_page.add_todo_item(item_name)
        
        logging.info("Verifying item appears in ToDo list")
        assert item_name in self.todo_page.get_todo_item_list(),\
                    'ToDo item "{}" not found in ToDo list'.format(item_name)
        
    def test_delete_todo(self):
        item_name = "Do Me!!"
        logging.info("Opening ToDo page")
        self.todo_page.navigate_to()
        
        logging.info("Adding a new ToDo item")
        self.todo_page.add_todo_item(item_name)
        logging.info("Verifying item appears in ToDo list")
        assert item_name in self.todo_page.get_todo_item_list()
        
        logging.info('Deleting previously added item ("{}")'.format(item_name))
        self.todo_page.delete_todo_item(item_name)
        logging.info("Verifying item no longer appears in ToDo list")
        assert item_name not in self.todo_page.get_todo_item_list()
        
    def tearDown(self):
        self.driver.close()
        


if __name__ == '__main__':
    unittest.main()