from source.playlists.playlist_tools import PlaylistTools
import json

playlist_tools = PlaylistTools()
playlist_name="My Own WCS"
library_file="data/corys_social_playlists.json"
with open(library_file) as f:
    library=json.load(f)
playlist_id = playlist_tools.create_or_clean_playlist(name=playlist_name)
playlist_tools.add_tracks_to_playlist(playlist_id=playlist_id, tracks=library)