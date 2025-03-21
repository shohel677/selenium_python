from selenium import webdriver


class DriverMaster:
    driver = None

    @staticmethod
    def browser_init(browser_name: str) -> webdriver.Chrome | webdriver.Firefox | webdriver.Edge:
        """Initializes the browser driver based on the given browser name."""

        if "chrome" in browser_name:
            options = webdriver.ChromeOptions()
            if browser_name == "chromeheadless":
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")
                driver = webdriver.Chrome(options=options)
            else:
                options.add_experimental_option("detach", True)
                driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            driver = webdriver.Firefox()
        elif browser_name == "edge":
            driver = webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        return driver
