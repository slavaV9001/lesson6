from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html'
)
print("Загрузка страницы")

img = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "award"))
)
print("Загрузка award")
images = driver.find_elements(By.TAG_NAME, "img")
third_image = images[3]
src_value = third_image.get_attribute("src")
print(src_value)

driver.quit()
print("Успешный успех!")
