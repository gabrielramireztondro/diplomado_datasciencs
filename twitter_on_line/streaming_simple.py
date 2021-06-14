import tweepy
import json

class SimpleOutListener(tweepy.StreamListener):

    def __init__(self,my_file):

        super(SimpleOutListener,self).__init__(self)

        self.my_file=my_file

    def on_connect(self):
        print('Conectando a Api...')

    def on_data(self, data):
        self.my_file.write(data)

        j=json.loads(data)

        text=j["text"] 
        print(text) #Print it out
        return True

    def on_error(self, status):
        print(status)

    def on_timeout(self):
        pass
