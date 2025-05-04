import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Spotify API credentials
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)


# Buscar el ID del artista
#artist_name = "Linkin Park"
#result = spotify.search(q=f"artist:{artist_name}", type="artist", limit=1)
#artist_id = result["artists"]["items"][0]["id"]


artist_id = "6XyY86QOPPrYVGvF9ch6wz"

# Obtener top tracks
top_tracks = spotify.artist_top_tracks(artist_id, country='US')["tracks"]

# Extraer datos
songs_data = []
for track in top_tracks[:10]:  # Top 10
    name = track["name"]
    popularity = track["popularity"]
    duration_min = round(track["duration_ms"] / 60000, 2)
    songs_data.append({"Nombre": name, "Popularidad": popularity, "Duración (min)": duration_min})

# Crear DataFrame
df = pd.DataFrame(songs_data)


# Ordenar por popularidad ascendente
df_sorted = df.sort_values(by="Popularidad", ascending=True)

# Mostrar las 3 canciones menos populares
print("🎧 Top 3 canciones menos populares:")
print(df_sorted.head(3))


# Guardar CSV
df.to_csv("linkin_park_top10.csv", index=False)
# A partir de aqui he continuado en explore.ipynb