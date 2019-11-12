import requests
import json

# open the settings
with open( "settings.json", "r") as data:
	settings 					= json.load(data)
	telegram_bot_token 			= settings['telegram_bot_token']

def send_message(message, telegram_chat_id):
	requests.post("https://api.telegram.org/bot" + str(telegram_bot_token) + "/sendMessage?chat_id="+str(telegram_chat_id)+"&text="+message).json()

def get_updates():
	updates = requests.post("https://api.telegram.org/bot" + str(telegram_bot_token) + "/getUpdates").json()
	return updates

def send_typing(telegram_chat_id):
	requests.post("https://api.telegram.org/bot" + str(telegram_bot_token) + "/sendChatAction?chat_id="+str(telegram_chat_id)+"&action=typing").json()