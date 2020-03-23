import json

with open('items.json', 'r') as f:
    db = json.load(f)

# Check for items that are part of a recipe, but not an individual item (missing tree info)
print('---[[ DIAGNOSE: MISSING TREE INFO ]]---')
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
    print('---[[ DIAGNOSE: NO MISSING TREE INFO :) ]]---')

# Check for name mismatches for crafter recipes


# Check for items that have -1 for price (missing price info)

