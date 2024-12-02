from selenium import webdriver

@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


