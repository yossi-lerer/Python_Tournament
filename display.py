def display_list(data:list):
    for record in data:
        for field in record: 
            print(f"{field}: {record[field]}")

def display_dict(record):
    for field in record: 
        print(f"{field}: {record[field]}")