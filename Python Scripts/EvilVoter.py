import time
from selenium import webdriver


for i in range(37):
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.

    driver.get('https://unlv.co1.qualtrics.com/jfe/form/SV_bQ1uKVSca33EZkp');
    time.sleep(10) # Let the user actually see something!

    inputElement = driver.find_element_by_id("QR~QID1")
    inputElement.send_keys('Smart Stepper')

    time.sleep(10) # Let the user actually see something!
    python_button = driver.find_element_by_xpath("//*[@id=\"NextButton\"]")
    python_button.click()
    time.sleep(10) # Let the user actually see something!

    driver.close()
    time.sleep(20)
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
#driver.quit()
