import json
import os

def writing_data(path, new_record):
    if not os.path.isfile(path):
        new_record = [new_record]
        with open(path, "w") as f:
            json.dump(new_record, f, indent=4)
    else:
        with open(path, mode='r') as file:
            data = json.load(file)
            data.append(new_record)
        with open(path, mode='w') as file:
            json.dump(data, file, indent=4)

    with open(path, mode='r') as file:
        data = json.load(file)
    return data

def update_data(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    return data

def read_data(path):
    with open(path, mode='r') as file:
        data = json.load(file)
    return data
    
if __name__ == "__main__":
    print(read_data("match.json"))