from source.playlists.playlist_tools import PlaylistTools
import json
playlist_tools = PlaylistTools()

playlists_huge = [
    "https://open.spotify.com/playlist/5JUxCWx8jehtKUH6XCgfaF?si=d4ebfdea99a048cf",
    "https://open.spotify.com/playlist/78fQ9KW2RfDwMFZocCxTdY?si=c1c3f41d7c2241ce",
    "https://open.spotify.com/playlist/0puUKs6AEq1PvMqMzQo587?si=a34de639f7cd458f",
    "https://open.spotify.com/playlist/3d7MSID2rKuZHHXRgLO7GQ?si=29e1882c9bdb4a94",
    "https://open.spotify.com/playlist/1gP11jtFdpwyFppJiFJqNn?si=0658e576b24f4090",
    "https://open.spotify.com/playlist/1TqgDSWdd6L6Gv4z0km2pA?si=525ff82461f04189",
    "https://open.spotify.com/playlist/4mAoGyjo8ImNft8YCiqMwf?si=ecf6dd83d3974e92",
    #"https://open.spotify.com/playlist/2wIwBjXvhaIa01lkBXgd2l" 
]

own_playlists = [
    "https://open.spotify.com/playlist/3T4xy37PPtQZOY2O8tcuuS?si=0a4cdaa7d2de423d",
    "https://open.spotify.com/playlist/0u5PTfoZTSgk8sCNK9auCn?si=40dca5a8dbaf45b3",
    "https://open.spotify.com/playlist/2fPr81HAGxaYOudRc7XZNX?si=5024e236ea5f4ab6",
    "https://open.spotify.com/playlist/1sdkqOVYl6knHz2JzRZtzr?si=a341dccbceef4343",
    "https://open.spotify.com/playlist/7F0eXlfz2IGFIe5Wdzsd66?si=11da399dd3354916",
    "https://open.spotify.com/playlist/4F26n072uqOVZFfw2uaQUV?si=3c2a606b7d694733",
    "https://open.spotify.com/playlist/6wIUiwHMnfCkaiwi28wkCB?si=c1139308d0b54825",
    "https://open.spotify.com/playlist/1i40JEcs9RzxHM22bSNE3W?si=5ca5333740ba4392",
    "https://open.spotify.com/playlist/5oThLSiJ0JbDhBgL1BmYNR?si=015a580b0d0b4855",
    "https://open.spotify.com/playlist/58427iYHPXpGOmuGsjIYrQ?si=b7ede917830c4597",
    "https://open.spotify.com/playlist/42egmGMm9hkLx24c5YNC08?si=f6e483a5a4d34d40",
    "https://open.spotify.com/playlist/1gP11jtFdpwyFppJiFJqNn?si=74af7911c9014c4c",
    "https://open.spotify.com/playlist/3d7MSID2rKuZHHXRgLO7GQ?si=4acb38c8b28a4dde",
    "https://open.spotify.com/playlist/0puUKs6AEq1PvMqMzQo587?si=69446f93964048b0",
]


all_tracks = set()
track_counter=0
for playlist in playlists_huge:
    for track in playlist_tools.get_and_iterate_tracks(playlist_id=playlist):
        if track:
            all_tracks.add(track['id'])
            track_counter += 1
    print(f"Finished playlist. Number of tracks: {track_counter}, number of deduplicated tracks: {len(all_tracks)}")
#print(f"len of all tracks after merge: {len(all_tracks)}")

with open("/home/cordi/old_home_folder/cordi/Files/projects/SpotifyTools/data/libraries/wcs_large.json", "w") as f:
    json.dump(list(all_tracks), f)
