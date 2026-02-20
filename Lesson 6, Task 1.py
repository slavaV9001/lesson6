from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/ajax')
print("Страница открыта")

driver.find_element(By.ID, 'ajaxButton').click()
print("Синяя кнопка успешно нажата!")

element = WebDriverWait(driver, 30).until(
EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
)
print(f"Элемент {element.text} найден и виден")

driver.quit()
print("Finish")
