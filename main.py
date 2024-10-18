import requests, json
from memory import Memory 
from initdb import initialize_db

QUOTE_API = 'https://zenquotes.io/api/random'
JOKE_API = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,explicit'

memory = Memory

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
initialize_db()

user = input("Please enter if you want a new quote or joke. Or enter 'done': ")
while(user != "done"):
  if(user == "quote"):
    quote = get_quote()
    count =0
    while memory.hasQuote(quote):
      quote = get_quote()
      count+=1
      if count == 10:
        print("You're about to brick your PC homie")
        break
    print(quote)
  if(user == "joke"):
    joke = get_joke()
    while memory.hasJoke(joke):
      joke = get_joke()
      count+=1
      if count == 10:
        print("You're about to brick your PC homie")
        break
    print(joke)  
  user = input("\nMake a new request: ")

memory.storeData(quote, joke)
print("Data has been saved to memory. Thank you for using the Quote & Joke Generator!")