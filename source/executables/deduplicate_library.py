from source.playlists.playlist_tools import PlaylistTools, DeduplicationMethod
import json


playlist_tools = PlaylistTools()
playlist_name="Library WCS Own"
library_file="/home/cordi/old_home_folder/cordi/Files/projects/SpotifyTools/data/libraries/wcs_huge.json"
with open(library_file) as f:
    library=json.load(f)
print(f"Library size {len(library)}")
all_tracks=[]
for batch in playlist_tools._list_batcher(list_to_batch=library, batch_size=50):
    #print(batch)
    result = playlist_tools.spotify_client.tracks(tracks=batch)
    #print(result['tracks'])
    #print(type(result['tracks']))
    all_tracks += result['tracks']
    #print(all_tracks)

playlist_tools.deduplicate_tracks(tracks=all_tracks, deduplication_method=DeduplicationMethod.ISRC)
