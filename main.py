import requests
import validators

print("Enter a URL to scrape")

url = input()

if validators.url(url):
    content = requests.get(url)
    print(content.text)

else:
    print("Invalid URL '" + url + "'")
    print("Please try again")
