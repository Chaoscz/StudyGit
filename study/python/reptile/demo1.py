import urllib


response = urllib.request.urlopen('http://localhost:8080/ibms')
print response.read()
