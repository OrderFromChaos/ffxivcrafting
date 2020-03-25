def cost_lookup(dbname):
    import json
    from collections import deque
    from src.validator import validate_input

    with open(f'data/{dbname}', 'r') as f: # Intended to be called from root (menu.py)
        db = json.load(f)

    name = validate_input('Item name?', lambda x: x in db, "    Item not in database.")
    # if there is not any (item without craftable/gatherable/tradeable and not on mb), calculate drilldown costs
    # minimize from bottom of tree

    memory = dict()
    def recurse_cost(itemname):
        # determines the "minimum mb cost" value and passes it up
        if itemname in memory:
            return memory[itemname]
        else:
            obj = db[itemname]
            if not obj['craftable']:
                return obj['mbprice']
            elif obj['craftable']:
                subprices = []
                for ingname, amt in obj['craftinfo']['recipe'].items():
                    subprices.append(amt * recurse_cost(ingname))
                
                summa = sum(subprices) / obj['craftinfo']['output']
                if summa < obj['mbprice']:
                    ans = summa
                else:
                    ans = obj['mbprice']
                
                # ans = ans * 1.05

                memory[itemname] = int(ans)
                return int(ans)

    # DFS so bottom items are printed first
    d = deque()
    d.append((name, 1, 1, 0))
    while len(d) > 0:
        currname, amt, pamt, depth = d.pop()
        realq = amt*pamt
        currobj = db[currname]
        # Intended output:
        # 
        # 1 facet coat of crafting (.../168900, lvl 80** wvr craft)
        # ╚═ 4 pliable glass fiber (9333/19000, lvl 80** alc craft)
        # ╚═══ 3 sandalwood sap (999, lvl 80 btn @ legendary 2 AM/PM the rak'tika greatwood (24.6, 36.9))
        # ╚═══ 1 sublime solution (7500, 125 white crafter's scrip)
        # ╚═══ 1 scuroglow aethersand (800, 100 white gatherer's scrip)
        # ╚═══ 2 water cluster (9, lvl 50 btn @ unspoiled 1 AM, 5AM, 9AM mor dhona (32, 11)) 
        # ╚═══ 2 lightning cluster (8, lvl 50 btn @ unspoiled 1 AM, 5AM, 9AM mor dhona (32, 11))
        # ╚═ 3 ethereal silk (.../18969, lvl 80** wvr craft)
        # ╚═══ ...
        # 
        contextstr = ''
        if currobj['gatherable']:
            # (999, lvl 80 btn @ legendary 2 AM/PM the rak'tika greatwood (24.6, 36.9))
            gatherinfo = currobj['gatherinfo']
            contextstr = ('({0}, lvl {1}{2} {3} @ {4} {5} {6} {7})'.format(
                    realq*currobj['mbprice'],
                    gatherinfo['lvl'],
                    gatherinfo['gdata'],
                    gatherinfo['gatherer'],
                    gatherinfo['node'],
                    gatherinfo['time'],
                    gatherinfo['area'],
                    gatherinfo['coords']
                )
            )
        elif currobj['craftable']:
            # (9333/19000, lvl 80** alc craft)
            craftinfo = currobj['craftinfo']
            contextstr = ('({0}/{1}, lvl {2}{3} {4} craft)'.format(
                    realq*recurse_cost(currname),
                    realq*currobj['mbprice'],
                    craftinfo['lvl'],
                    craftinfo['cdata'],
                    craftinfo['crafter']
                )
            )
        elif currobj['tradeable']:
            # (7500, 125 white crafter's scrip)
            tradeinfo = currobj['tradeinfo']
            contextstr = ('({0}, {1} {2})'.format(
                    realq*currobj['mbprice'],
                    tradeinfo['cost'],
                    tradeinfo['unit']
                )
            )
        elif currobj['droppable']:
            # (200, [kill] tempest swallow @ the tempest (26.9, 14.6))
            dropinfo = currobj['dropinfo']
            contextstr = ('({0}, [kill] {1} @ {2} {3})'.format(
                    realq*currobj['mbprice'],
                    dropinfo['enemy'],
                    dropinfo['area'],
                    dropinfo['coords']
                )
            )
        else:
            raise Exception('Unrecognized drop type:', currobj)
        if depth > 0:
            print('  '*depth, end='')
            print('╚═', end='')
            # print('══'*(depth-1), end='')
            print(' ', end='')
        print(realq, currname, contextstr)

        if currobj['craftable']:
            for ingname, quant in currobj['craftinfo']['recipe'].items():
                d.append((ingname, quant, realq, depth + 1))

if __name__ == "__main__":
    cost_lookup('items.json')