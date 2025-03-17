from source.playlists.playlist_tools import PlaylistTools

playlist_tools = PlaylistTools()


playlist1="https://open.spotify.com/playlist/5JUxCWx8jehtKUH6XCgfaF?si=1f58f915a4a94c86"
playlist2="https://open.spotify.com/playlist/6q6r9n9A4GV475fhOJ45lx?si=48bf1ed63f4f4194"

playlist1_tracks={playlist_tools.track_to_str(track=track): track for track in playlist_tools.get_and_iterate_tracks(playlist_id=playlist1)}
playlist2_tracks={playlist_tools.track_to_str(track=track): track for track in playlist_tools.get_and_iterate_tracks(playlist_id=playlist2)}

in_1_but_not_2={id: track for id, track in playlist1_tracks.items() if id not in playlist2_tracks}
in_2_but_not_1={id: track for id, track in playlist2_tracks.items() if id not in playlist1_tracks}
in_both={id: track for id, track in playlist1_tracks.items() if id in playlist2_tracks}

for track in in_both.values():
    print(f"In both playlists: {playlist_tools.track_to_str(track=track)}")
for track in in_1_but_not_2.values():
    print(f"In 1, but not in 2: {playlist_tools.track_to_str(track=track)}")
for track in in_2_but_not_1.values():
    print(f"In 2, but not in 1: {playlist_tools.track_to_str(track=track)}")

print(f"len of first playlist: {len(playlist1_tracks)}")
print(f"len of second playlist: {len(playlist2_tracks)}")