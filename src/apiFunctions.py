import os
import requests
import discord

#apiKey = os.environ["TONISAPIKEY"]
oAuth = ""

def getChannels(serverID):
    apiAddress = "https://discordapp.com/api/v6/guilds/"+serverID
    print(apiAddress)

    header = {
        "Authorization": oAuth,
        "Content-Type": "application/json",
    }

    print(oAuth)
    r = requests.get(apiAddress, headers = header)

    server = r.json()
    channels = server

    return channels

def sayHello(channelID, message):
    apiAddress = "https://discordapp.com/api/v6/channels/" + str(channelID) + "/messages"
    print(apiAddress)

    header = {
        "Authorization": oAuth,
        "Content-Type": "application/json"
    }

    body = {"content" : message}

    r = requests.post(apiAddress, json = body, headers = header)


    return r


if __name__ == "__main__":
    print("weitermachen")