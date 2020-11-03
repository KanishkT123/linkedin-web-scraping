from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('C:/path/to/chromedriver.exe')
driver.get('https://www.linkedin.com/')


with open("C:/path/to/username.txt", "r") as f:
    username = driver.find_element_by_name("session_key")
    usernameFromFile = f.readline()
    username.send_keys(usernameFromFile)
    sleep(0.5)

with open("C:/path/to/password.txt", "r") as f:
    passwordFromFile = f.readline()
    password = driver.find_element_by_name('session_password')
    password.send_keys(passwordFromFile)
    sleep(0.5)


sign_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
sign_in_button.click()
sleep(2)

driver.get('https://www.linkedin.com/search/results/people/')
searchBox = driver.find_element_by_class_name("search-global-typeahead__input")
searchBox.send_keys("Python developer portland")
searchBox.send_keys(Keys.RETURN)
sleep(5)

urls = driver.find_elements_by_xpath('//*[@class="search-result__result-link ember-view"]')
urls = [url.get_attribute('href') for url in urls]
res = [res.append(url) for url in urls if url not in res]

print(res)

driver.quit()
