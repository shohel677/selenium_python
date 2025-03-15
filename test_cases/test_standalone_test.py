from selenium import webdriver
from selenium.webdriver.common.by import By


def standalone_test():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.NAME, "password").send_keys("secret_sauce")

    driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
    driver.find_element(By.CSS_SELECTOR, "a[id='item_0_title_link']").click()

    driver.find_element(By.XPATH,"//button[@name='add-to-cart']").click()
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Mr.")
    driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("X")
    driver.find_element(By.XPATH,"//input[@placeholder='Zip/Postal Code']").send_keys("1206")
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    driver.find_element(By.XPATH, "//button[text()='Finish']").click()
    thank_you_text = driver.find_element(By.TAG_NAME, "h2").text
    driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Reset App").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
