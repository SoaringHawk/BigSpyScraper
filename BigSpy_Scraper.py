from selenium import webdriver
from config import email, password
import time
import urllib.request, json

driver = webdriver.Chrome('./chromedriver')

url = 'https://bigspy.com/dropship/spy/#/main/dropship/first'
class data_scraper:
	bulk_json_data = []
	
	######################## Json data parsing ###############################
	def get_json_data(bulk_product_keys):
		for key in bulk_product_keys:
			request_data = urllib.request.urlopen('https://bigspy.com/dropship/get-product?product_id={}'.format(key)).read()
			json_data = json.loads(request_data.decode('utf-8'))
			print(json_data)
			data_scraper.bulk_json_data.append(json_data)
		
	def get_prod_url(url):
		product_id = 1
		pagination = 1
		driver.get(url)
		############################ Manual login  ##################################
		#time.sleep(156)
		
		############################   Auto login  ##################################
		time.sleep(8)
		driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[5]/div[2]/a/button').click()
		driver.find_element_by_xpath('//*[@id="login-form-login"]').send_keys(email)
		time.sleep(3.26)
		driver.find_element_by_xpath('//*[@id="login-form-password"]').send_keys(password)
		
		time.sleep(150)
		driver.get(url)
		time.sleep(15)
		
		############################ Data retrieval #################################
		while pagination <= 100:
			bulk_product_keys = []
			while product_id <= 24:
				try:
					driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[4]/ul/li[{}]'.format(product_id)).click()
					time.sleep(2)
					product_keys = driver.current_url.split('key=')
					bulk_product_keys.append(product_keys[1])
					driver.back()
					time.sleep(0.5)
					product_id += 1
				except NoSuchElementException:
					driver.get(url)
					driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[4]/ul/li[{}]'.format(product_id)).click()
					time.sleep(15)
					product_keys = driver.current_url.split('key=')
					bulk_product_keys.append(product_keys[1])
					driver.back()
					time.sleep(0.5)
					product_id += 1

			data_scraper.get_json_data(bulk_product_keys)
			######## Display json data at every itaration #########
			print(data_scraper.bulk_json_data)
			product_id = 1
			pagination += 1
			try:
				driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[5]/div/div/ul/li[{}]'.format(pagination)).click()
			except NoSuchElementException:
				driver.refresh()
				driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[5]/div/div/ul/li[{}]'.format(pagination)).click()

			time.sleep(10)

		return product_keys

 



if __name__ == '__main__':
	data_scraper.get_prod_url(url)
	####### Display whole data base when loop finishes ###########
	#print(data_scraper.bulk_json_data)