from source.spotify_client import get_spotify_client
from source.contants import LINOS_USER_ID, ALICIAS_USER_ID, CORYS_USER_ID
import json
from pathlib import Path
import csv

user_id=CORYS_USER_ID
filepath="data/corys_social_playlists.json"

client=get_spotify_client()
playlists = client.user_playlists(user=user_id, limit=100)
print(f"Number of playlists: {len(playlists['items'])}")


if Path(filepath).exists():
    with open(filepath) as input_file:
        list_of_playlists=json.load(input_file)
else:
    list_of_playlists=[]

existing_ids=[entry['id'] for entry in list_of_playlists]

for playlist in playlists['items']:
    if playlist['id'] in existing_ids:
        print(f"Playlist {playlist['name']} already exists")
    else:
        print(playlist['name'])
        user_input = input(f"Hit y to keep playlist, n to skip\n")
        if user_input.lower() == "y":
            list_of_playlists.append({"name": playlist["name"], "id": playlist["id"]})

with open(filepath, "w") as output:
    json.dump(list_of_playlists, output, indent=2)