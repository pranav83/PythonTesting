from selenium import webdriver

driver = webdriver.Ie(executable_path="C:\\Users\\prana\\PycharmProjects\\untitled1\\IEDriverServer.exe")
driver.maximize_window()
driver.get("https://indiancouture.co.za/")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//button[contains(text(),'Dismiss')]").click()
driver.quit()
