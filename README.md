# YouTube Playlist Title Extractor and Comparator

This Python script uses the YouTube API to extract video titles from one or two given YouTube playlists. It can also compare the titles between two playlists to find common songs.

## Requirements

- Python 3.x
- Google API Python Client

You can install the Google API Python Client using pip:

```
pip install --upgrade google-api-python-client
```

## How to Use

1. Replace `YOUR_API_KEY_HERE` with your actual YouTube API key.
2. Replace `YOUR_FIRST_PLAYLIST_URL_HERE` with the URL of the first playlist you want to extract titles from.
3. Optionally, replace `YOUR_SECOND_PLAYLIST_URL_HERE` with the URL of the second playlist you want to compare with the first.
4. Run the script.

## Classes and Methods

- `YouTubePlaylistExtractor`: The main class that handles the extraction and comparison.
  - `obtener_id_lista_reproduccion(self, lista_reproduccion_url)`: Extracts the playlist ID from the given YouTube playlist URL.
  - `obtener_titulos(self, playlist_id)`: Fetches the titles of all videos in the specified playlist, supports pagination.

## Example

```python
API_KEY = "YOUR_API_KEY_HERE"
PLAYLIST_URL1 = "YOUR_FIRST_PLAYLIST_URL_HERE"
PLAYLIST_URL2 = "YOUR_SECOND_PLAYLIST_URL_HERE"  # Optional

extractor = YouTubePlaylistExtractor(API_KEY)

# First playlist
playlist_id1 = extractor.obtener_id_lista_reproduccion(PLAYLIST_URL1)
titles1 = extractor.obtener_titulos(playlist_id1)
if titles1:
    print("Titles in the first playlist:")
    for title in titles1:
        print(title)

# ... (rest of the code for the second playlist and comparison)
```

