from splinter.browser import Browser
import time, sys

#browser = Browser('chrome') 			# Selenium Standalone on your local machine
browser = Browser(driver_name="remote",  	# Docker Selenium Standalone
                  url='http://127.0.0.1:4444/wd/hub',
                  browser='chrome')

url = "https://www.instagram.com/accounts/login/"
fam = ['beyonce', 'cristiano', 'selenagomez', 'arianagrande', 'kimkardashian', 'therock']


def signIn():
	browser.visit(url)
	browser.find_by_name('username').fill('<username>')
	browser.find_by_name('password').fill('<password>')
	browser.find_by_text('Log In').click()
	browser.is_text_present('Not Now', wait_time=10)
	browser.find_by_text('Not Now').first.click()


def follow():
	for i in fam:
		browser.visit("https://www.instagram.com/" + i)
		browser.is_text_present('Follow', wait_time=10)
		browser.find_by_text('Follow').first.click()
		browser.is_text_present('Following', wait_time=10)

def unfollow():
	for i in fam:
		browser.visit("https://www.instagram.com/" + i)
		browser.is_text_present('Following', wait_time=10)
		browser.find_by_text('Following').first.click()
		browser.is_text_present('Unfollow', wait_time=10)
		browser.find_by_text('Unfollow').first.click()
		browser.is_text_present('Follow', wait_time=10)

def checkFams():
	for i in fam:
		browser.visit("https://www.instagram.com/" + i)

		if browser.is_text_present('Following', wait_time=3):
			browser.find_by_text('Following').first.click()
			browser.is_text_present('Unfollow', wait_time=10)
			browser.find_by_text('Unfollow').first.click()
			browser.is_text_present('Follow', wait_time=10)
	print ("Check Fams has been done !!")


signIn()
checkFams()


a=0
while True:

	follow()
	time.sleep(15)
	print (str(a+1) + "." + " Follow Cycle Over")
	unfollow()
	time.sleep(15)
	print (str(a+1) + "." + " Unfollow Cycle Over")
	a += 1

	if a == 3:  # The count of how many time you want to follow/unfollow popular people.
		browser.quit()
		print ("Follow/Unfollow loops have been done!")
		sys.exit(0)

