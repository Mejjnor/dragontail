import os
import unittest
from unittest.case import TestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from todo_page import ToDoPage


class TestClusterPage(TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.todo_page = ToDoPage(self.driver)
    
    def test_add_todo(self):
        item_name = "Do Me!!"
        self.todo_page.navigate_to()
        
        self.todo_page.add_todo_item(item_name)
        
        assert item_name in self.todo_page.get_todo_item_list()
        
    def test_delete_todo(self):
        item_name = "Do Me!!"
        self.todo_page.navigate_to()
        
        self.todo_page.add_todo_item(item_name)
        assert item_name in self.todo_page.get_todo_item_list()
        
        self.todo_page.delete_todo_item(item_name)
        assert item_name not in self.todo_page.get_todo_item_list()
        
    def tearDown(self):
        self.driver.close()
        


if __name__ == '__main__':
    unittest.main()