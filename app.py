from decouple import config
import telebot
import http.client
import http
import json



conn = http.client.HTTPSConnection("facebook-reel-and-video-downloader.p.rapidapi.com")
headers = {
    'X-RapidAPI-Key': "9401f3099dmsh183323edbeb4857p1ca1e2jsn8f4e317df8cd",
    'X-RapidAPI-Host': "facebook-reel-and-video-downloader.p.rapidapi.com"
}

BOT_TOKEN=config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello! , how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "Loading.....")
    print(message.text)
    conn = http.client.HTTPSConnection("facebook-reel-and-video-downloader.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "9401f3099dmsh183323edbeb4857p1ca1e2jsn8f4e317df8cd",
        'X-RapidAPI-Host': "facebook-reel-and-video-downloader.p.rapidapi.com"
    }
    link ="/app/main.php?url="+message.text
    conn.request("GET", link,headers=headers)

    res = conn.getresponse()
    data = res.read()
    my_string = data.decode('utf-8')
    datas = json.loads(my_string)
    praser_value = str(datas["links"])
    bot.reply_to(message, praser_value)


bot.infinity_polling()
