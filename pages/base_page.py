
class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """This method opens a browser by the provided link"""
        self.driver.get(self.url)
