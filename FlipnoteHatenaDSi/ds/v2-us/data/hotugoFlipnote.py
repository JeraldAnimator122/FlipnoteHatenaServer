import json
import os
from datetime import datetime

METADATA_PATH = "FlipnoteHatenaDSi/ds/v2-us/movies/metadata.json"

def get_hot_list():
    if not os.path.exists(METADATA_PATH):
        return []

    with open(METADATA_PATH, 'r') as f:
        movies = json.load(f).get("movies", [])

    now = datetime.now()
    scored_movies = []

    for m in movies:
        # Check if "delete" is true
        if m.get("deleted", False):
            continue

        # Hot Score Logic: (Stars + Comments) / (Hours since upload + 2)
        upload_date = datetime.fromisoformat(m['upload_date'])
        hours_old = (now - upload_date).total_seconds() / 3600
        score = (m['stars'] + m['comments']) / (hours_old + 2)
        
        m['hot_score'] = score
        scored_movies.append(m)

    # Sort by Score Descending
    return sorted(scored_movies, key=lambda x: x['hot_score'], reverse=True)
