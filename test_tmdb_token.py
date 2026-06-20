import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TMDB_API_READ_ACCESS_TOKEN")

if token:
    print("Token başarıyla okundu.")
    print(f"İlk 10 karakter: {token[:10]}...")
else:
    print("Token bulunamadı. .env dosyasını kontrol et.")