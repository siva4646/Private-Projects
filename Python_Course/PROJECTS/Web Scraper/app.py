from urllib.request import urlopen


url = 'https://google.com'
page = urlopen(url)
print(page)