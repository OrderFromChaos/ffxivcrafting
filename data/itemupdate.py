import json
from collections import deque

with open('items.json', 'r') as f:
    db = json.load(f)

name = input("Item name? ")

if name in db.keys():
    q = deque()
    q.append(name)
    visited = set()
    while len(q) > 0:
        name = q.pop()
        if name not in visited:
            visited.add(name)
            info = db[name]

            price = input('Price of ' + name + '? (-2 if no listings) ')
            price = int(price)
            db[name]['mbprice'] = price

            if info['craftable']:
                for recname in info['craftinfo']['recipe'].keys():
                    if recname.split(' ')[-1] not in ['cluster','crystal','shard']:
                        q.append(recname)

    with open('items.json', 'w') as f:
        json.dump(db, f, indent=4)
else:
    print('Item not found.')