from source.spotify_client import get_spotify_client
from source.playlists.playlist_tools import PlaylistTools
from source.contants import TEST_ACCOUNT_USER_ID
from pathlib import Path
import json
from time import sleep

spotify_client = get_spotify_client()
playlist_tools = PlaylistTools()

data_folder="/home/cordi/old_home_folder/cordi/Files/projects/SpotifyTools/data/audio_analysis"
track_counter_all=0
track_counter_skipped=0
track_counter_not_skipped=0

playlist_ids=("1gP11jtFdpwyFppJiFJqNn", "0puUKs6AEq1PvMqMzQo587", "3d7MSID2rKuZHHXRgLO7GQ", "5JUxCWx8jehtKUH6XCgfaF")
playlist_ids=["78fQ9KW2RfDwMFZocCxTdY",]
playlist_ids=["2VsswDPtjj0SsdxWYaQbnz"]

for playlist_id in playlist_ids:
    print(f"New playlist: {playlist_id}")
    for track in playlist_tools.get_and_iterate_tracks(playlist_id=playlist_id):
        track_id=track['id']
        track_counter_all+=1
        print(f"counter: {track_counter_all}, skipped: {track_counter_skipped}, not skipped: {track_counter_not_skipped}")


        save_path=Path(data_folder, f"{track_id}.json")
        if not save_path.exists():
            track_counter_not_skipped+=1
            audio_analysis = spotify_client.audio_analysis(track_id=track_id)
            audio_features = spotify_client.audio_features(track_id)
            save_object={
                "track": track,
                "audio_analysis": audio_analysis,
                "audio_features": audio_features,
            }
            with save_path.open("w") as save_file:
                json.dump(save_object, save_file, indent=2)
                #sleep(5)
        else:
            track_counter_skipped+=1
            
