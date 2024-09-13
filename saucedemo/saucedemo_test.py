# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")


driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)").click()
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
driver.find_element(By.ID,"checkout").click()
driver.find_element(By.ID,"first-name").send_keys("Ayanloye")
driver.find_element(By.ID,"last-name").send_keys("Segun")
driver.find_element(By.ID,"postal-code").send_keys("102345")
driver.find_element(By.ID,"continue").click()
driver.find_element(By.ID,"finish").click()
driver.find_element(By.ID,"back-to-products").click()
driver.find_element(By.ID,"react-burger-menu-btn").click()
driver.find_element(By.ID,"logout_sidebar_link").click()
time.sleep(2)
