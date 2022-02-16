import json
from sys import stdin

data = [i.rstrip() for i in stdin]
data = [i.split(' = ')[1] for i in data]

ans = {"complex": []}
for i in data:
    k = 0
    if len(i.split(' + ')) < 2:
        t = i.split(' - ')
        k = 1
    else:
        t = i.split(' + ')
    if k == 1:
        t[1] = "-" + t[1].split(' * ')[0]
    else:
        t[1] = t[1].split(' * ')[0]
    ans['complex'].append({"Re": float(t[0]), "Im": float(t[1])})

with open('output.json', 'w', encoding='utf8') as out:
    json.dump(ans, out, indent=2)
