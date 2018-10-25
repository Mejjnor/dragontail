from selenium_element import SeleniumElement, Locator
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class ToDoPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://todomvc.com/examples/react/#/"
    
        self.title = SeleniumElement(self.driver, Locator(By.CLASS_NAME, "header"))
        self.new_todo_input = SeleniumElement(self.driver, Locator(By.CLASS_NAME, "new-todo"))
        self.todo_list = SeleniumElement(self.driver, Locator(By.CLASS_NAME, "todo-list"))
    
    def navigate_to(self):
        self.driver.get(self.url)
        self.title.wait_for(20)
    
    def add_todo_item(self, to_do):
        self.new_todo_input.send_keys("{}\n".format(to_do))
    
    def get_todo_item_list(self):
        try:
            list_ = self.todo_list.find()
            elements = list_.find_elements_by_xpath("li")
        except NoSuchElementException:
            return {}
        todo_dict = {}
        for element in elements:
            item_id = element.get_attribute("data-reactid")
            item_name = element.text
            item_el = SeleniumElement(self.driver, Locator(By.XPATH, '//*[@data-reactid="{}"]'.format(item_id)))
            item_chkbx = SeleniumElement(self.driver, Locator(By.XPATH, '//*[@data-reactid="{}.0.0"]'.format(item_id)))
            item_dlt = SeleniumElement(self.driver, Locator(By.XPATH, '//*[@data-reactid="{}.0.2"]'.format(item_id)))
            item_dict = {"element": item_el, "checkbox": item_chkbx, "delete": item_dlt}
            todo_dict[item_name] = item_dict
        
        return todo_dict
    
    def delete_todo_item(self, item_name):
        todo_list = self.get_todo_item_list()
        if item_name not in todo_list:
            return
        
        todo_list[item_name]["element"].click()
        todo_list[item_name]["delete"].click()

    
            