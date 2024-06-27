import os
import json


def load_json():
    combined_data = []
    folder_path = (
        "/home/harshitlohani/Desktop/Projects/petofy-chat-assistant/dataset/data"
    )
    # Traverse through the directory tree using os.walk
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                with open(file_path, "r") as f:
                    # Load JSON data from the file
                    data = json.load(f)
                    # Append to the combined list
                    combined_data.append(data)
    #print(combined_data)
    return combined_data


load_json()
