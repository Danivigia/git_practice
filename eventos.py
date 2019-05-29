import urllib.request

headers = {
  'Authorization': 'AS3PAWFS7OXU6UKLIZPO',
  'Content-Type': 'application/json'
}
city = "Lisbon"

request = urllib.request.Request('https://www.eventbriteapi.com/v3/events/search/?location.address=', city, headers=headers)

response_body = urllib.request.urlopen(request).read()
print(response_body)
