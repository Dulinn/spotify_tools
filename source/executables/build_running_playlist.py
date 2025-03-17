from source.audio_analysis import audio_analysis_tools
from source.audio_analysis.audio_analysis_tools import AudioAnalysisTools, FilterCriteria
from source.audio_analysis.audio_feature import AudioFeature
from source.playlists.playlist_tools import PlaylistTools
from typing import List

audio_analysis_tools = AudioAnalysisTools(adjust_tempo=False)
playlist_tools = PlaylistTools()
criteria = [
    FilterCriteria(audio_feature=AudioFeature.TEMPO, lower=157, upper=162),
    FilterCriteria(audio_feature=AudioFeature.ENERGY, lower=0.7, upper=1),
    FilterCriteria(audio_feature=AudioFeature.VALENCE, lower=0.5, upper=1),
]
source_playlists=["4P0ErOvOYd2GAXTRIHv00m",
                  "4eP5adKtw7IaYOnZq8tNlJ",
                  "0EVQR3A1xeOv5IhOik9q2p",
                  "0ebFtrpHcf1VUe5SaQQT2O",
                  "4a0BOxyBbcZD6g5mdlVy8u",
                  "37i9dQZF1EIcNylL4dr08W",
                  "7fdDgjOHEcwYgTQDP5OAnP",
                  "3WiVk9dGKbSFWZcXpxmWA2",
                  "4xW4qC8TuHmlUVJsHoO9Xv",
                  "1al1fy8WHBRu7GsPHHhZuU",
                  "0oilQoeNcbm6VNMHTYeNHt",]

target_playlist = playlist_tools.create_or_clean_playlist(name="Running 160BPM Extended Criteria")
all_tracks = set()
for playlist in source_playlists:
    for track in playlist_tools.get_and_iterate_tracks(playlist_id=playlist):
        all_tracks.add(track['id'])
tracks_filtered = audio_analysis_tools.filter_tracks(track_ids=all_tracks, criteria_list=criteria, skip_if_missing=False)
playlist_tools.add_tracks_to_playlist(playlist_id=target_playlist, tracks=tracks_filtered)
