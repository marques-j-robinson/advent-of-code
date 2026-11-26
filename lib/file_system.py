events = {
    "2015": "events/2015"
}

def read_input_data(e, d):
    with open(f"{events[e]}/{d}/data", "r", encoding="utf-8") as f:
        data = f.read()
        f.close()
    return data