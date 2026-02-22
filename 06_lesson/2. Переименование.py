from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
driver.get('http://uitestingplayground.com/textinput')

input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")
print("Текст введен")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()
print("Кнопка нажата")

wait = WebDriverWait(driver, 15)
wait.until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

updated_text = driver.find_element(By.ID, "updatingButton").text
print(f"Текст на кнопке: {updated_text}")

driver.quit()
print("Finish")
