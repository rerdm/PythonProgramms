import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


class InitialisiereWebdriverSetzeZoomLevel:

    """
    With this class it is possible to create a Selenium driver instance
    without downloading the drivers form teh internet.
    The programm will do it automatically and therefore the : webdriver_manager is used
    Be sure that you have installed it properly : pip install webdriver-manager ( install via Terminal)

    You can use a Firefox ore a Chrome driver and you can set a zoom level or not.
    """

    def __init__(self):
        self.driver = None

    def get_chrome_webdriver_ohne_zoom(self):

        """
        This Method will create a chrome driver instance.
        The Zoom-Level is set to 100% (No-Zoom)
        """

        if not self.driver:
            chrome_options = Options()

            chrome_service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

            # Webdriver Window auf Maximum setzen
            self.driver.maximize_window()

        return self.driver

    def get_chrome_webdriver_mit_zoom(self):
        """
        This Method will create a chrome driver instance.
        The Zoom-Level is set to 90%
        """
        if not self.driver:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--force-device-scale-factor=0.90")

            chrome_service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            self.driver.maximize_window()

        return self.driver

    def get_firefox_webdriver_ohne_zoom(self):

        """
        This Method will create a firefox instance.
        The Zoom-Level is set to 100% (No-Zoom)
        """

        if not self.driver:
            firefox_options = FirefoxOptions()

            firefox_service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

            self.driver.maximize_window()

        return self.driver

    def get_firefox_webdriver_mit_zoom(self):
        """
        This Method will create a firefox instance.
        The Zoom-Level is set to 90%
        """
        if not self.driver:

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--force-device-scale-factor=0.90")

            chrome_service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            self.driver.maximize_window()

        return self.driver

    def close_webdriver(self):

        """
        closes the driver
        """
        if self.driver:
            self.driver.quit()
            self.driver = None


if __name__ == "__main__":

    webdriver_initialisieren = InitialisiereWebdriverSetzeZoomLevel()

    try:
        driver = webdriver_initialisieren.get_firefox_webdriver_mit_zoom()
        driver.get("https://google.de")
        time.sleep(5)

        # Dein Selenium-Code hier...

    finally:
        webdriver_initialisieren.close_webdriver()