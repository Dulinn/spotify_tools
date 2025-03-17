from source.playlists.playlist_tools import PlaylistTools, DeduplicationMethod
import csv
playlist_tools = PlaylistTools()
import json

filepath="data/corys_social_playlists.json"

new_playlist_id = playlist_tools.create_or_clean_playlist("Own WCS")


with open(filepath) as input_file:
    playlists=json.load(input_file)

playlists_to_merge = [entry['id'] for entry in playlists]

playlist_tools.merge_and_deduplicate(source_playlist_ids=playlists_to_merge, target_playlist_id=new_playlist_id, deduplication_method=DeduplicationMethod.ISRC)