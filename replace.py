import json
import os

filepath = "data/logcutter/recipes"
for item in os.listdir(filepath):
    with open(f"{filepath}/{item}", 'r') as f:
        data = json.load(f)

    data["ingredient"]["item"] = data["ingredient"]["item"].replace("_log", "_wood").replace("_stem", "_hyphae")
    data["result"] = data["result"].replace("_log", "_wood").replace("_stem", "_hyphae")
    
    with open(f"{filepath}/{item.replace('_log', '_wood').replace('_stem', '_hyphae')}", 'w') as f:
        json.dump(data, f, indent=4)