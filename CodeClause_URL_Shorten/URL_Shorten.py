bitlyToken = "7aee10d43...53ef5d05714"
#API = 7aee10d43...53ef5d05714
#This part was hidden in Video Tutorial.





import requests



endpoint = "https://api-ssl.bitly.com/v4/shorten"

url = "https://www.github.com/prathmeshchaudhari05"

response = requests.post("https://api-ssl.bitly.com/v4/shorten", 
                          headers={"Authorization": "Bearer " + bitlyToken}, 
                          json={"long_url":url}
                        )

print(response.json()['link'])

