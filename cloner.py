from selenium import webdriver
import os
import subprocess

class cloner:

	def __init__(self):
		self.repo_links=[]

	def scrape(self):
		driver=webdriver.Firefox()
		driver.get("https://github.com/login")
		username = driver.find_element_by_id("login_field")
		print("Enter Github Username")
		user = input()
		username.send_keys(user)

		password = driver.find_element_by_id("password")
		print("Enter Password")
		passw = input()
		password.send_keys(passw)
		driver.find_element_by_class_name("btn-primary").click()


		try:
			print("Enter OTP")
			otp = input()
			driver.find_element_by_id("otp").send_keys(otp)
			driver.find_element_by_class_name("btn-primary").click()
		except Exception as e:
			print(e)
		finally:
			print("Enter username of person whose repositories are to be cloned")
			clone = input()
			driver.get(f'https://github.com/{clone}?tab=repositories')
			repos = driver.find_element_by_id("user-repositories-list")
			li = repos.find_elements_by_class_name("col-12")

			for ind in li:
				inner = ind.find_element_by_class_name("col-10")
				h3 = inner.find_element_by_class_name("wb-break-all").text
				self.repo_links.append(f'https://github.com/{clone}/{h3}.git\n')

		driver.quit()

	def clone(self):
		os.system("pwd")
		print("Enter Directory Name")
		dir_name=input()
		temp=dir_name
		dirs=dir_name.split(" ")
		dir_name=""
		for dir_n in dirs:
			dir_name=f'{dir_name}{dir_n}\ '
		temp=temp.strip()
		dir_name=dir_name.strip()
		dir_name=dir_name[0:-1]
		try:
			if os.system(f'mkdir {dir_name}')!=0:
				raise "Error"
		except Exception as e:
			print(e)
		finally:
			os.chdir(temp)
			print("Repos will be cloned here:")
			os.system("pwd")
			for link in self.repo_links:
				com = f'git clone {link}'
				subprocess.call([com],shell=True)

cloner_obj = cloner()
cloner_obj.scrape()
cloner_obj.clone()