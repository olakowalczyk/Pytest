import pytest
from selenium.webdriver import Chrome
from pages.form_page import FormPage

@pytest.fixture
def driver():
  driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()


@pytest.fixture
def form_page(driver):
    form_page = FormPage(driver)
    form_page.load()
    yield form_page