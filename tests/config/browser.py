import pytest
from selenium.webdriver import Chrome

@pytest.fixture
def driver():
  driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

