import requests, json

QUOTE_API = 'https://zenquotes.io/api/random'
JOKE_API = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,explicit'

def get_quote():
  response = requests.get(QUOTE_API)
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\r\n - " + json_data[0]['a']
  return quote

def get_joke():
  response = requests.get(JOKE_API)
  json_data = json.loads(response.text)
  try:
    joke = json_data['joke']
    return joke
  except:
    setup = json_data['setup']
    delivery = json_data['delivery']
  return setup + "\n" + delivery

quote = get_quote()
joke = get_joke()
print(quote + "\n" + joke + "\n")


user = input("Please enter if you want a new quote or joke. Or enter 'done': ")
while(user != "done"):
  if(user == "quote"):
    quote = get_quote()
    print(quote)
  if(user == "joke"):
    joke = get_joke()
    print(joke)  
  user = input("\nMake a new request: ")
