from source.audio_analysis.audio_feature import AudioFeature
from source.spotify_client import get_spotify_client
from source.audio_analysis.audio_analysis_post_processors import unlist_audio_features, adjust_tempo
from pathlib import Path
import json
from dataclasses import dataclass
from tqdm import tqdm

DEFAULT_AUDIO_ANALYSIS_DATA_FOLDER="/home/cordi/old_home_folder/cordi/Files/projects/SpotifyTools/data/audio_analysis"

@dataclass
class FilterCriteria:
    audio_feature: AudioFeature
    lower: float
    upper: float

class AudioAnalysisFileReader:
    def __init__(self, audio_analysis_data_folder=DEFAULT_AUDIO_ANALYSIS_DATA_FOLDER, post_process_adjust_tempo=True) -> None:
        self.audio_analysis_data_folder=Path(audio_analysis_data_folder)
        post_processors = [unlist_audio_features,] 
        if post_process_adjust_tempo:
            post_processors.append(adjust_tempo)
        self.post_processors = post_processors
        self.spotify_client=get_spotify_client()
        self.tracks=dict()
        self._read_all_audio_analysis_track_ids()

    def get_all_audio_analysis_track_ids(self):
        return self.tracks.keys()

    def _read_all_audio_analysis_track_ids(self):
        for path in self.audio_analysis_data_folder.glob("*.json"):
            track_id = path.stem
            if track_id not in self.tracks:
                self.tracks[track_id] = None

    def get_audio_analysis(self, track_id, skip_if_missing=False):
        if track_id not in self.tracks:
            if skip_if_missing:
                return None
            else:
                self._download_audio_analysis(track_id=track_id)
        elif self.tracks[track_id] is None:
            self._read_audio_analysis(track_id=track_id)

        return self.tracks[track_id]
        
    def _download_audio_analysis(self, track_id):
        
        track = self.spotify_client.track(track_id=track_id)
        audio_analysis = self.spotify_client.audio_analysis(track_id=track_id)

        combined_object={
            "track": track,
            "audio_analysis": audio_analysis,
            #"audio_features": audio_features,
        }
        save_path=Path(self.audio_analysis_data_folder, f"{track_id}.json")
        with save_path.open("w") as save_file:
            json.dump(combined_object, save_file, indent=2)
        self._post_process_audio_analysis(audio_analysis=combined_object)
        self.tracks[track_id] = combined_object


    def _read_audio_analysis(self, track_id):
        filepath = self.audio_analysis_data_folder.joinpath(f"{track_id}.json")
        with open(filepath) as f:
            audio_analysis = json.load(f)
            self._post_process_audio_analysis(audio_analysis=audio_analysis)
            self.tracks[track_id] = audio_analysis

    def _post_process_audio_analysis(self, audio_analysis):
        for post_processor in self.post_processors:
            post_processor(audio_analysis)


class AudioAnalysisTools:
    def __init__(self, adjust_tempo=True) -> None:
        self.reader=AudioAnalysisFileReader(post_process_adjust_tempo=adjust_tempo)

    def filter_all_tracks(self, criteria_list):
        return self.filter_tracks(self.reader.get_all_audio_analysis_track_ids(), criteria_list=criteria_list)
    
    def filter_specific_tracks(self, tracks, criteria_list, skip_if_missing=False):
        return self.filter_tracks(track_ids=tracks, criteria_list=criteria_list, skip_if_missing=skip_if_missing)

    def filter_tracks(self, track_ids, criteria_list, skip_if_missing=False):
        filtered_track_ids = []
        for track_id in tqdm(track_ids):
            audio_analysis = self.reader.get_audio_analysis(track_id=track_id, skip_if_missing=skip_if_missing)
            
            if audio_analysis and all([self.track_matches_criteria(audio_analysis, criteria) for criteria in criteria_list]):
                filtered_track_ids.append(track_id)
        
        return filtered_track_ids
        

    def track_matches_criteria(self, audio_analysis, criteria: FilterCriteria):
        feature_value = audio_analysis['audio_features'][criteria.audio_feature.value]
        return feature_value > criteria.lower and feature_value <= criteria.upper
    
    def get_audio_feature(self, track_id, feature: AudioFeature, skip_if_missing=True):
        audio_analysis = self.reader.get_audio_analysis(track_id=track_id, skip_if_missing=skip_if_missing)
        if audio_analysis is not None:
            return audio_analysis["audio_features"][feature.value]
        else:
            return 0


