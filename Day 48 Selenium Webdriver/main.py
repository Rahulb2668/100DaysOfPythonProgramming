from time import sleep, time

from selenium import webdriver
from selenium.webdriver.common.by import By
URL = "https://orteil.dashnet.org/cookieclicker/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")


sleep(3)
print("Looking for language selection...")
try:
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    language_button.click()
    sleep(3) # more loading
except Exception as e:
    print("Language selection not found",e)

# Wait for everything to settle
sleep(2)
cookie = driver.find_element(By.ID, value="bigCookie")

timetocheck = 5
five_min = time() +( 60*5)
check_product_time = time() +timetocheck

while True:
    cookie.click()
    if time() > check_product_time:
        try:
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            # Find the most expensive item we can afford
            best_item = None
            for product in reversed(products):
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except Exception as e:
            print("Couldn't find cookie count or items")

        # Reset timer
        check_product_time = time() + timetocheck

    if time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except Exception as e:
            print("Couldn't get final cookie count")
        break
