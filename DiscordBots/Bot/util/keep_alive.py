# Python Script to keep bot online forever.

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return 'I\'m alive!'

def run():
  app.run(host='localhost', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
  print('Keep Alive Progress started.')
