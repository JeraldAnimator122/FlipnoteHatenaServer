import json
import os

METADATA_PATH = "FlipnoteHatenaDSi/ds/v2-us/movies/metadata.json"

def get_liked_flipnotes(fsid):
    if not os.path.exists(METADATA_PATH):
        return []

    with open(METADATA_PATH, 'r') as f:
        movies = json.load(f).get("movies", [])

    # Filter for movies where this FSID is in the 'starred_by' list
    # and "deleted" is not true
    return [m for m in movies if fsid in m.get('starred_by', []) and not m.get("deleted", False)]
