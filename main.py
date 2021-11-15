from pyrogram import Client, filters

app=Client(session_name='myapp', api_id=14027438, api_hash='9c9527c9c3e59853818ba0b0e2486737')

List=['salam', 'hello']

@app.on_message(filters.text)
def caller(Client, message):
	print(message.text)
	text=message.text
	if text in List:
		app.send_message(chat_id=message.chat.id, text='welcome')
	
	
app.run()
