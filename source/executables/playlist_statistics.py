from source.playlists.playlist_tools import PlaylistTools
from source.audio_analysis.audio_analysis_tools import AudioAnalysisTools
from source.audio_analysis.audio_feature import AudioFeature
from datetime import timedelta
from source.audio_analysis.audio_analysis_post_processors import unlist_audio_features
from urllib3.exceptions import ResponseError
from spotipy.exceptions import SpotifyException


playlist_id = "https://open.spotify.com/playlist/5KCj2FVIJuboQhXAxXatQR?si=05fddd8ad8514e93"

playlist_tools = PlaylistTools()
analysis_tools =AudioAnalysisTools(adjust_tempo=True)


playlist_time_seconds = 0
for i, track in enumerate(playlist_tools.get_and_iterate_tracks(playlist_id=playlist_id)):
    id=track['id']
    try:
        bpm = analysis_tools.get_audio_feature(track_id=id, feature=AudioFeature.TEMPO)
        energy = analysis_tools.get_audio_feature(track_id=id, feature=AudioFeature.ENERGY)
        acousticness = analysis_tools.get_audio_feature(track_id=id, feature=AudioFeature.ACOUSTICNESS)
    except (SpotifyException, ResponseError) as e:
        bpm = 0
        energy = 0
        acousticness = 0
        #print(f"Exception: {e}")


    def indicator_str(low, high, length, value):
        value=min(value, high)
        value=max(value, low)
        value=value-low
        low_to_high = high-low
        value_per_dash = low_to_high/length
        num_dashes = int(value/value_per_dash)
        return " "*(length-num_dashes)+"-"*num_dashes
    
    bpm_str=indicator_str(70, 120, 10, bpm)
    if bpm==0:
        bpm_str="x"*10
    energy_str=indicator_str(0, 1, 10, energy)
    acousticness_str=indicator_str(0, 1, 10, acousticness)

    #print(track.keys())
    print(f"{i:02} Time: {timedelta(seconds=playlist_time_seconds)} BPM: {bpm_str} {int(bpm):3}, En: {energy_str} A: {acousticness_str}  Name: {track['name']} - {', '.join(artist['name'] for artist in track['artists'])}")
    playlist_time_seconds+=int(track['duration_ms']/1000)
    

