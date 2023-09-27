
import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from urllib.parse import urlparse, parse_qs

class YouTubePlaylistExtractor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube_service = build("youtube", "v3", developerKey=api_key)

    def obtener_id_lista_reproduccion(self, lista_reproduccion_url):
        """
        Extracts the playlist ID from the given YouTube playlist URL.
        """
        parsed_url = urlparse(lista_reproduccion_url)
        query_params = parse_qs(parsed_url.query)
        lista_reproduccion_ids = query_params.get('list')
        
        if not lista_reproduccion_ids:
            raise ValueError('No se pudo extraer el ID de la lista de reproducción del URL')
        
        return lista_reproduccion_ids[0]
    
    def obtener_titulos(self, playlist_id):
        titles = []
        next_page_token = None
        
        while True:
            try:
                playlist_request = self.youtube_service.playlistItems().list(
                    part="snippet",
                    maxResults=50,
                    pageToken=next_page_token,
                    playlistId=playlist_id
                )
                playlist_response = playlist_request.execute()
                
                titles += [item["snippet"]["title"] for item in playlist_response["items"]]
                
                next_page_token = playlist_response.get('nextPageToken')
                
                if next_page_token is None:
                    break
                    
            except HttpError as e:
                print(f"An HTTP error {e.resp.status} occurred: {e.content}")
                return None

        return titles

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY_HERE"
    PLAYLIST_URL1 = "YOUR_FIRST_PLAYLIST_URL_HERE"
    PLAYLIST_URL2 = "YOUR_SECOND_PLAYLIST_URL_HERE" 
    
    extractor = YouTubePlaylistExtractor(API_KEY) 
    
    # Primera lista
    playlist_id1 = extractor.obtener_id_lista_reproduccion(PLAYLIST_URL1)
    titles1 = extractor.obtener_titulos(playlist_id1)
    if titles1:
        print("Títulos en la primera lista:")
        for title in titles1:
            print(title)
    
    # Segunda lista
    if PLAYLIST_URL2:  # Solo si la URL2 está presente
        if PLAYLIST_URL2 == PLAYLIST_URL1:
            print("\nLa segunda URL es idéntica a la primera, se ignorará.")
        else:
            try:
                playlist_id2 = extractor.obtener_id_lista_reproduccion(PLAYLIST_URL2)
            except ValueError:
                print("\nLa segunda URL no parece ser un enlace de lista de reproducción de YouTube válido.")
            else:
                titles2 = extractor.obtener_titulos(playlist_id2)
                if titles2:
                    print("\nTítulos en la segunda lista:")
                    for title in titles2:
                        print(title)

                # Encontrar canciones en común
                common_songs = set(titles1).intersection(set(titles2))
                if common_songs:
                    print("\nCanciones repetidas entre las listas:")
                    for song in common_songs:
                        print(song)
                else:
                    print("\nNo hay canciones repetidas.")
    else:
        print("\nNo se proporcionó una segunda lista de reproducción.")
