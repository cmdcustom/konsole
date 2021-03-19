import sys
import requests

if sys.argv[2] == 'csharp':
    print(requests.get(f'https://konsolecompile.cmdcustom.repl.co?ext=cs&data={open(sys.argv[1]).read()}').content.decode())
if sys.argv[2] == 'python':
    print(requests.get(f'https://konsolecompile.cmdcustom.repl.co?ext=py&data={open(sys.argv[1]).read()}').content.decode())
if sys.argv[2] == 'python2':
    print(requests.get(f'https://kcpy2.cmdcustom.repl.co?data={open(sys.argv[1]).read()}').content.decode())
if sys.argv[2] == 'bash':
    print(requests.get(f'https://konsolecompile.cmdcustom.repl.co?ext=sh&data={open(sys.argv[1]).read()}').content.decode())
if sys.argv[2] == 'nodejs':
    print(requests.get(f'https://konsolecompile.cmdcustom.repl.co?ext=js&data={open(sys.argv[1]).read()}').content.decode())
    
