import urllib.request

headers = {
  'Authorization': 'AS3PAWFS7OXU6UKLIZPO',
  'Content-Type': 'application/json'
}
city = "Lisbon"
data = city.encode("utf-8")
request = urllib.request.Request('https://www.eventbriteapi.com/v3/events/search/?location.address=', data, headers=headers)

response_body = urllib.request.urlopen(request).read()
print(response_body)
