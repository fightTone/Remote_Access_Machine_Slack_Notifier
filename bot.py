import slack
import os
import pathlib
from pathlib import Path
from dotenv import load_dotenv
from tmate_session_starter import get_ssh_connection_string
from datetime import datetime
import getpass
import requests

def get_public_ip():
    return requests.get('https://api64.ipify.org').text

def get_geolocation(public_ip):
    response = requests.get(f'https://ipinfo.io/{public_ip}/json')
    return response.json()

current_user = getpass.getuser()
ip_address = get_public_ip()
location_details = get_geolocation(ip_address)


client = slack.WebClient(token="PUT_YOU_OWn_TOKEN_HERE")
connection_details = get_ssh_connection_string()
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
msg = (f"""
Machine User: {current_user}
Machine Address: {ip_address}
IP Location Details: 
```{location_details}```
────────────────────────────────────────
```
    Connection Details ({current_time}):
{connection_details}
────────────────────────────────────────
```
""")
#update with your desired channel
client.chat_postMessage(channel='#personal_notifier_gee', text=msg)