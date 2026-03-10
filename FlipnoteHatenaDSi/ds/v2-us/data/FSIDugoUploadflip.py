import json
import os

METADATA_PATH = "FlipnoteHatenaDSi/ds/v2-us/movies/metadata.json"

def get_user_uploads(fsid):
    if not os.path.exists(METADATA_PATH):
        return []

    with open(METADATA_PATH, 'r') as f:
        movies = json.load(f).get("movies", [])

    # Filter by Author ID and ensure it isn't deleted
    return [m for m in movies if m['author_id'] == fsid and not m.get("deleted", False)]
