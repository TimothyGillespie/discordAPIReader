import os
import requests

apiKey = os.environ["TONISAPIKEY"]
token_type = "bot" # is this correct?

def getChannels(serverID):
    apiAddress = "https://discordapp.com/api/v6/guilds/%s".format(serverID)

    header = {"Authorization": "%s %s".format(token_type, apiKey)}

    r = requests.post(apiAddress, data = header)

    server = r.json()
    channels = server.channels

    return channels