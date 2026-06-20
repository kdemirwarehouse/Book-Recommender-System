import json
import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from dotenv import load_dotenv

load_dotenv()

POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500"


def get_poster_url(movie_name: str):
    token = os.getenv("TMDB_API_READ_ACCESS_TOKEN")

    params = urlencode({
        "query": movie_name,
        "language": "tr-TR"
    })

    url = f"https://api.themoviedb.org/3/search/movie?{params}"

    request = Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "accept": "application/json"
        }
    )

    with urlopen(request) as response:
        data = json.loads(response.read().decode("utf-8"))

    if not data["results"]:
        return None

    poster_path = data["results"][0].get("poster_path")

    if not poster_path:
        return None

    return f"{POSTER_BASE_URL}{poster_path}"