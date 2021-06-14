
import tweepy
import json
from auth_parameter  import AuthApiTwitter
from streaming_simple import SimpleOutListener

if __name__ == '__main__':
    try:

        my_file = open("output.json","a")

        #creando instancia de escucha
        listen = SimpleOutListener(my_file)
        authentication=AuthApiTwitter()
        auth = tweepy.OAuthHandler(authentication.consumer_key, authentication.consumer_secret)
        auth.set_access_token(authentication.access_token, authentication.access_token_secret)

        #Connecta con la api
        stream = tweepy.Stream(auth, listen)	

        #Terms to track
        stream.filter(track=["#EleccionesGobernador2021","#VOTACIONES2021","#Elecciones2021CL","#E32021","#EleccionesCHVCNN"],
        languages=["es"],
        locations=[-71.511939925,-34.3485699246,-69.7892355348,-32.9657213682])

 

    except KeyboardInterrupt:
        pass

    finally:
        my_file.close()