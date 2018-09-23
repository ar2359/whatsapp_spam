#Python 2.7
from selenium import webdriver
b = webdriver.Firefox()
b.get('http://web.whatsapp.com')
raw_input()
elem = b.find_element_by_xpath('//span[contains(text(),"<Enter name of contact>")]')
elem.click()
elem1 = b.find_elements_by_class_name('input')
a=0
while a<10:
	elem1[1].send_keys('Hello')
	b.find_element_by_class_name('send-container').click()
	a=a+1