from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://tutorialsninja.com/demo/index.php?route=common/home")

print(driver.page_sourse)
