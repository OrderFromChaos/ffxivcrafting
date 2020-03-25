def diagnostic(dbname):
    import json

    with open(f'data/{dbname}', 'r') as f:
        db = json.load(f)

    # Check for items that are part of a recipe, but not an individual item (missing tree info)
    print('---[[ DIAGNOSE: MISSING SUBINGREDIENTS ]]---')
    toplevel = set(list(db.keys()))
    searchfor = []
    for x in db.values():
        if x['craftable']:
            searchfor += list(x['craftinfo']['recipe'].keys())
    nomiss = True
    for x in searchfor:
        if x not in toplevel:
            print('MISSING', x)
            nomiss = False
    if nomiss:
        print('---[[ CLEAR: NO MISSING SUBINGREDIENTS :) ]]---')

    # Check for num. of items that have -1 for price (missing price info)
    noprice = 0
    nopricenames = []
    for i, x in db.items():
        if x['mbprice'] == -1:
            noprice += 1
            nopricenames.append(i)
    if noprice == 0:
        print(f'---[[ CLEAR: MISSING {noprice} PRICES ]]---')
    else:
        print(f'---[[ DIAGNOSE: MISSING {noprice} PRICES ]]---')
        for i in nopricenames:
            print(f'"{i}"')

    # Check for num. of items that have -2 for price (no mb sales)
    nosale = 0
    nosalenames = []
    for i, x in db.items():
        if x['mbprice'] == -2:
            nosale += 1
            nosalenames.append(i)
    if nosale == 0:
        print(f'---[[ CLEAR: {nosale} ITEMS NOT BEING SOLD ]]---')
    else:
        print(f'---[[ DIAGNOSE: {nosale} ITEMS NOT BEING SOLD ]]---')
        for i in nosalenames:
            print(f'"{i}"')


if __name__ == "__main__":
    diagnostic('items.json')
