from json_fs import read_data

def sorting_scraping_groups(data):
    sorting = sorted(data, key=lambda d: (d["points"], d["goals_for"] - d["goals_against"], d["goals_for"], d["name"]), reverse=True)
    return sorting
