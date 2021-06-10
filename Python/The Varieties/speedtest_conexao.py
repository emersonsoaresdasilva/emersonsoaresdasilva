# → pip install speedtest-cli

import speedtest
import socket 
import requests

from requests import get

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
external_ip = get('http://meuip.com/api/meuip.php').text

speed = speedtest.Speedtest()

download = speed.download() / 1048576
upload = speed.upload() / 1048576

print(f'My download speed is: {download:.2f} Mbps')
print(f'My upload speed is: {upload:.2f} Mbps')

print(f'\nMy local IP is: {local_ip}')
print(f'My external IP is: {external_ip}')

# ← python speedtest_conexao.py