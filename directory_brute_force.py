import requests

directory = input("Enter a url: ")
url = "http://" + directory + "/"

wl = open("wordlist.txt")
lines = wl.readlines()

def directories(url):
	for line in lines:
		req_url_main = requests.get(url+line)
		code_main = req_url_main.status_code
		url_updated = url+line
		url_updated = url_updated.replace('\n', '')
		print(url_updated + " | " + "CODE: " + str(code_main))


directories(url)
