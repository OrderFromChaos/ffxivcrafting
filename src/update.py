def item_update(dbname):
    import json
    from collections import deque
    from src.validator import validate_input, int_validator

    with open(f'data/{dbname}', 'r') as f:
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

                price = int(validate_input('Price of ' + name + '? (-2 if no listings) ', int_validator))
                db[name]['mbprice'] = price

                if info['craftable']:
                    for recname in info['craftinfo']['recipe'].keys():
                        if recname.split(' ')[-1] not in ['cluster','crystal','shard']:
                            q.append(recname)

        with open(f'data/{dbname}', 'w') as f:
            json.dump(db, f, indent=4)
    else:
        print('Item not found.')

if __name__ == "__main__":
    item_update('items.json')