# Options:
# 1 (cost lookup)
# 2 (itementry)
# 3 (itemupdate)
# 4 (run diagnostic)
# 0 (quit)

from src.cost_lookup import cost_lookup
from src.diagnostic import diagnostic
from src.entry import item_entry
from src.fillprices import fillprices
from src.update import item_update

valid = {1,2,3,4}
valid = set([str(x) for x in valid])

intro = 'Welcome to the FFXIV crafter/gatherer interface!'
prompt = '''Select an option:
1. Look up an item's cost tree
2. Enter an item's info
3. Update an item's prices recursively
4. Run a diagnostic for bad inputs
0. Quit'''

dataset = 'items.json'

userinput = '~'
print(intro)
while userinput != '0':
    print(prompt)
    userinput = input()
    if userinput not in valid:
        continue
    
    if userinput == '1':
        cost_lookup(dataset)
    elif userinput == '2':
        item_entry(dataset)
        fillprices(dataset)
    elif userinput == '3':
        item_update(dataset)
    elif userinput == '4':
        diagnostic(dataset)
