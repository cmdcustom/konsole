import requests

print('\n')

while 1:
    cmd = input('>> ')
    if cmd != '/e/':
        r = requests.get(f'https://shle.cmdcustom.repl.co?lang=python2&cmd={cmd}')
        print(r.content.decode())
    else:
        exit()
