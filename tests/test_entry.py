import subprocess
import sys
import os
import json

from src.entry import item_entry

# Empty test file
def clear_file():
    with open('data/test.json', 'w') as f:
        f.write('{\n\n}\n')

def stdin_call(inputfile, function):
    backup = sys.stdin
    with open(f'tests/{inputfile}', 'r') as f:
        sys.stdin = f
        function('test.json')
    print()
    sys.stdin = backup

def test_entry_drop():
    clear_file()
    stdin_call('entry_drop.txt', item_entry)
    expected = '''{
    "sea swallow skin": {
        "gatherable": false,
        "gatherinfo": {},
        "craftable": false,
        "craftinfo": {},
        "tradeable": false,
        "tradeinfo": {},
        "droppable": true,
        "dropinfo": {
            "enemy": "tempest swallow",
            "area": "the tempest",
            "coords": [
                26.9,
                14.6
            ]
        },
        "mbprice": -1
    }
}'''
    with open('data/test.json', 'r') as f:
        db = json.load(f)
    assert json.dumps(db, indent=4) == expected

def test_entry_gatherer():
    clear_file()
    stdin_call('entry_gatherer.txt', item_entry)
    expected = '''{
    "sandalwood sap": {
        "gatherable": true,
        "gatherinfo": {
            "gatherer": "btn",
            "lvl": 80,
            "gdata": "",
            "node": "legendary",
            "time": "2 AM/PM",
            "area": "the rak'tika greatwood",
            "coords": [
                24.6,
                36.9
            ]
        },
        "craftable": false,
        "craftinfo": {},
        "tradeable": false,
        "tradeinfo": {},
        "droppable": false,
        "dropinfo": {},
        "mbprice": -1
    }
}'''
    with open('data/test.json', 'r') as f:
        db = json.load(f)
    assert json.dumps(db, indent=4) == expected

def test_entry_crafter():
    clear_file()
    stdin_call('entry_crafter.txt', item_entry)
    expected = '''{
    "facet coat of crafting": {
        "gatherable": false,
        "gatherinfo": {},
        "craftable": true,
        "craftinfo": {
            "crafter": "wvr",
            "lvl": 80,
            "cdata": "**",
            "output": 1,
            "recipe": {
                "pliable glass fiber": 4,
                "ethereal silk": 3,
                "sea swallow leather": 1,
                "sublime solution": 2,
                "agewood aethersand": 2,
                "lightning cluster": 2,
                "wind cluster": 2
            }
        },
        "tradeable": false,
        "tradeinfo": {},
        "droppable": false,
        "dropinfo": {},
        "mbprice": -1
    }
}'''
    with open('data/test.json', 'r') as f:
        db = json.load(f)
    assert json.dumps(db, indent=4) == expected

def test_entry_trade():
    clear_file()
    stdin_call('entry_trade.txt', item_entry)
    expected = '''{
    "scuroglow aethersand": {
        "gatherable": false,
        "gatherinfo": {},
        "craftable": false,
        "craftinfo": {},
        "tradeable": true,
        "tradeinfo": {
            "cost": 100,
            "unit": "white gatherer's scrip"
        },
        "droppable": false,
        "dropinfo": {},
        "mbprice": -1
    }
}'''
    with open('data/test.json', 'r') as f:
        db = json.load(f)
    assert json.dumps(db, indent=4) == expected
