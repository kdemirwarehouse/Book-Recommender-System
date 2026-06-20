import json
import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TMDB_API_READ_ACCESS_TOKEN")

params = urlencode({
    "query": "Inception",
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

film = data["results"][0]

print("Film adı:", film["title"])
print("Poster path:", film["poster_path"])

poster_url = f"https://image.tmdb.org/t/p/w500{film['poster_path']}"
print("Poster URL:", poster_url)