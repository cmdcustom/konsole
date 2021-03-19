import requests
import os

print('\n')

while 1:
    cmd = input('root@nix:~# ')
    if cmd != '/e/':
        r = requests.get(f'https://shle.cmdcustom.repl.co?lang=sh&cmd={cmd}')
        print(r.content.decode())
    else:
        exit()
