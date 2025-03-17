from source.audio_analysis.audio_feature import AudioFeature

def unlist_audio_features(audio_analysis):
    audio_features = audio_analysis["audio_features"]
    if isinstance(audio_features, list):
        if len(audio_features) != 1:
            raise NotImplementedError(f"Audio Features has unexpected length: {len(audio_features)}")
        else:
            audio_analysis["audio_features"] = audio_features[0]


def adjust_tempo(audio_analysis, threshold=135):
    original_tempo = audio_analysis["audio_features"][AudioFeature.TEMPO.value]
    if original_tempo > threshold:
        audio_analysis["audio_features"][AudioFeature.TEMPO.value] = original_tempo/2
