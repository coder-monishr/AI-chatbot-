# this is a program using 


import os
import embedchain 
import App

os.environ["OPEN_API_KEY"] = "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"
elon_bot = App()

#online resources

elon_bot.add("web_page", "https://en.wikipedia.org/wiki/Elon_Musk")
elon_bot.add("web_page", "https://tesla.com/elon-musk")
elon_bot.add("youtube_video", "https://www.youtube.com/watch?v=MxZpaJK7474")

#query the bot
response = elon_bot.query("HOw many companies does elon musk run? ")
print(response)