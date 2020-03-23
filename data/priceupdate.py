import json

with open('items.json', 'r') as f:
    db = json.load(f)

for k, info in db.items():
    if info['mbprice'] == -1:
        price = input('Price of ' + k + '? (-2 if no listings) ')
        price = int(price)
        db[k]['mbprice'] = price

with open('items.json', 'w') as f:
    json.dump(db, f, indent=4)