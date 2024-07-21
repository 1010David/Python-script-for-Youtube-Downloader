import yt_dlp  # Importa la biblioteca yt-dlp para descargar videos de YouTube
from pydub import AudioSegment  # Importa la clase AudioSegment de la biblioteca pydub para manejar archivos de audio
import os  # Importa el módulo os para interactuar con el sistema de archivos

# Función para descargar el video de YouTube en formato MP4
def download_video(url, output_path='Descargas'):
    # Configuración para yt-dlp
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Descargar la mejor calidad de video y audio disponibles
        'outtmpl': os.path.join(output_path, 'video.%(ext)s'),  # Define la plantilla para el nombre del archivo de salida
        'merge_output_format': 'mp4',  # Fusiona el video y el audio en un archivo MP4
    }
    
    # Crea una instancia de YoutubeDL con las opciones definidas
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Descarga el video de YouTube usando la URL proporcionada
        ydl.download([url])
    
    # Busca el archivo MP4 en la carpeta de descargas
    for file in os.listdir(output_path):
        if file.endswith('.mp4'):
            return os.path.join(output_path, file)  # Devuelve la ruta completa del archivo MP4 descargado
    
    # Lanza una excepción si no se encuentra el archivo MP4
    raise FileNotFoundError("El archivo MP4 no se encontró en la carpeta de descargas.")

# Función para extraer el audio del video y guardarlo en formato MP3
def extract_audio(video_path, output_path='Descargas'):
    # Carga el archivo de video utilizando AudioSegment
    audio = AudioSegment.from_file(video_path)
    # Define la ruta del archivo MP3 basado en la ruta del archivo de video
    mp3_path = os.path.splitext(video_path)[0] + '.mp3'
    # Exporta el audio en formato MP3
    audio.export(mp3_path, format='mp3')
    return mp3_path  # Devuelve la ruta completa del archivo MP3

# Bloque principal de ejecución
if __name__ == "__main__":
    # Solicita al usuario que introduzca la URL del video de YouTube
    url = input("Enter the YouTube video URL: ")
    # Llama a la función download_video para descargar el video
    video_path = download_video(url)
    # Llama a la función extract_audio para extraer el audio del video
    mp3_path = extract_audio(video_path)
    # Imprime la ruta del archivo de video descargado
    print(f"Downloaded video: {video_path}")
    # Imprime la ruta del archivo de audio extraído
    print(f"Extracted audio: {mp3_path}")
