from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin 
import time


try:

	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	# говорим Selenium проверять в течение 12 секунд
	price = WebDriverWait(browser, 12).until(
	        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
	    )
	button = browser.find_element_by_id("book")
	button.click()
	
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text 
	y = str(log(abs(12*sin(int(x)))))

	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)
	button = browser.find_element_by_id("solve")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()