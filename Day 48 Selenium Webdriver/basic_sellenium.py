from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Add these to look more like a real human
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=chrome_options)

# This script hides the 'navigator.webdriver' property
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

URL = "https://www.amazon.ae/Samsung-Processor-Quantum-Security-QA65Q7FAAUXZN/dp/B0F63CGXY4/"

try:
    driver.get(URL)

    # Give the page a second to load the elements
    time.sleep(3)

    price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
    price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

    print(f"Price: {price_dollar.text}.{price_cents.text}")

except Exception as e:
    print(f"Error: Could not find elements. Amazon likely blocked the request. {e}")

finally:
    driver.quit() # Keep open to see what happened if it failed
    pass