#confirm
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button").click()
time.sleep(1)
print(Alert(driver).text)
time.sleep(1)
Alert(driver).dismiss()
print(driver.find_element(By.XPATH, "//*[@id='result']").text)
time.sleep(1)

#prompt
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
time.sleep(1)
print(Alert(driver).send_keys("JAI SHREE MAHAKAL"))
Alert(driver).accept()
time.sleep(1)
print(driver.find_element(By.XPATH, "//*[@id='result']").text)
time.sleep(1)

driver.close()