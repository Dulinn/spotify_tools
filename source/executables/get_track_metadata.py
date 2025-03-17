from source.spotify_client import get_spotify_client
import json

tracks=[
    #"https://open.spotify.com/track/5kA6evdqi1tmcJXu9bAqab?si=7ae5f09735e043a7",
    #"https://open.spotify.com/track/5xRslMQ3ZOEc2urW34ax1i?si=9dbaf4b3f2234782",
    #"https://open.spotify.com/track/6e9sNlDfuBx1TzDA7XTCEe?si=2c03e9531d394c56",
    #"https://open.spotify.com/track/3B7udSGy2PfgoCniMSb523?si=ac46a1e445444e1c",
    "https://open.spotify.com/track/5pY3ovFxbvAg7reGZjJQSp?si=5943d0643a6042f7"
]
track="https://open.spotify.com/intl-de/track/2eZJ9lrNeSqDt9iOgtft0M"

client = get_spotify_client()
track_data = client.track(track_id=track)
with open(f"stare.json", "w") as f:
    json.dump(track_data, f, indent=2)

