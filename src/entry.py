def item_entry(dbname):
    import json
    import re
    from validator import validate_input, int_validator, coord_validator

    WRITE_TO_FILE = True # For DEBUG

    with open(f'data/{dbname}', 'r') as f:
        db = json.load(f)

    name = input('Item name? ')
    itemdata = dict()

    continuebool = True
    if name in db.keys():
        print('Name already in database. Want to overwrite?')
        continuebool = validate_input('Overwrite? [0/1]', ['0','1'])
        continuebool = bool(int(continuebool))

    if not continuebool:
        return

    gbool = validate_input('Gatherable? [0/1]', ['0','1'])
    itemdata['gatherable'] = bool(int(gbool))

    gatherinfo = dict()
    if gbool == '1':
        gatherinfo['gatherer'] = validate_input('Gatherer class?', ['btn', 'fsh', 'min'])
        gatherinfo['lvl'] = int(validate_input('Gatherer level?', int_validator))
        gatherinfo['gdata'] = input('Additional gatherer info (eg **)? ')
        gatherinfo['node'] = validate_input('Node type?',
                        ['', 'normal', 'unspoiled', 'ephemeral', 'folklore', 'legendary'])
        gatherinfo['time'] = input('Open times? ')
        gatherinfo['area'] = input('Location? ')
        coords = validate_input('Coordinates?', coord_validator)
        gatherinfo['coords'] = [float(x) for x in re.findall(findnums, coords)[0][0].split(',')]
    itemdata['gatherinfo'] = gatherinfo


    cbool = validate_input('Craftable? [0/1]', ['0','1'])
    itemdata['craftable'] = bool(int(cbool))

    craftinfo = dict()
    if cbool == '1':
        crafters = ['alc', 'arm', 'bsm', 'cul', 'crp', 'gsm', 'ltw', 'wvr']
        craftinfo['crafter'] = validate_input('Crafter class?', crafters)
        craftinfo['lvl'] = int(validate_input('Crafter level?', int_validator))
        craftinfo['cdata'] = input('Additional crafter info (eg **)? ')
        craftinfo['output'] = int(validate_input('How much does the recipe output?', int_validator))
        # Grab recipe info
        recipe = dict()
        print('Starting recipe info. If you\'re done writing recipes, type "quit".')
        print('Recipes should be formatted as follows:')
        print('<name in lowercase> <quantity>')
        currinput = input()
        ingredientre = re.compile(r'((\w+\s)+(\d+))')
        ingredients = []
        while currinput != 'quit':
            search = re.findall(ingredientre, currinput)
            if search:
                ingredients.append((' '.join(search[0][0].split(' ')[:-1]), search[0][-1]))
            else:
                print('    Incorrectly formatted! Not entered to ingredient list.')
            currinput = input()
        for n, q in ingredients:
            recipe[n] = int(q)
        craftinfo['recipe'] = recipe
    itemdata['craftinfo'] = craftinfo


    tbool = validate_input('Tradeable? [0/1]', ['0','1'])
    itemdata['tradeable'] = bool(int(tbool))

    tradeinfo = dict()
    if tbool == '1':
        tradeinfo['cost'] = int(validate_input('Number of units?', int_validator))
        tradeinfo['unit'] = input('Type of unit? ')
    itemdata['tradeinfo'] = tradeinfo


    dbool = validate_input('Droppable? [0/1]', ['0','1'])
    itemdata['droppable'] = bool(int(dbool))

    dropinfo = dict()
    if dbool == '1':
        dropinfo['enemy'] = input('Name of enemy? ')
        dropinfo['area'] = input('Location? ')
        coords = validate_input('Coordinates?', coord_validator)
        dropinfo['coords'] = [float(x) for x in re.findall(findnums, coords)[0][0].split(',')]
    itemdata['dropinfo'] = dropinfo


    itemdata['mbprice'] = -1


    if WRITE_TO_FILE:
        db[name] = itemdata
        with open(f'data/{dbname}', 'w') as f:
            json.dump(db, f, indent=4)
    else:
        print('\n')
        print(json.dumps(itemdata, indent=4))

if __name__ == "__main__":
    item_entry('items.json')