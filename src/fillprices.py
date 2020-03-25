def fillprices(dbname):
    import json
    from src.validator import validate_input, int_validator

    with open(f'data/{dbname}', 'r') as f:
        db = json.load(f)

    for k, info in db.items():
        if info['mbprice'] == -1:
            price = int(validate_input('Price of ' + k + '? (-2 if no listings) ', int_validator))
            db[k]['mbprice'] = price

    with open(f'data/{dbname}', 'w') as f:
        json.dump(db, f, indent=4)


if __name__ == "__main__":
    fillprices('items.json')
