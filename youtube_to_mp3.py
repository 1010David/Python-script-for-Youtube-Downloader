import yt_dlp  # Importa la biblioteca yt-dlp para descargar videos de YouTube
import os  # Importa el módulo os para interactuar con el sistema de archivos

# Función para descargar el video de YouTube en formato MP4
def download_video(url, output_path='Descargas'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)  # Crea la carpeta si no existe

    # Configuración para yt-dlp
    ydl_opts = {
        'format': 'best',  # Descargar la mejor calidad de video y audio disponibles en un solo archivo
        'outtmpl': os.path.join(output_path, 'video.%(ext)s'),  # Define la plantilla para el nombre del archivo de salida
        'merge_output_format': 'mp4',  # Fusiona el video y el audio en un archivo MP4
        'postprocessors': [{  # Configuración para asegurar que el archivo MP4 sea el formato correcto
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    try:
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
    
    except Exception as e:
        print(f"Error al descargar el video: {e}")

# Bloque principal de ejecución
if __name__ == "__main__":
    # Solicita al usuario que introduzca la URL del video de YouTube
    url = input("Enter the YouTube video URL: ")
    # Llama a la función download_video para descargar el video
    video_path = download_video(url)
    if video_path:
        # Imprime la ruta del archivo de video descargado
        print(f"Downloaded video: {video_path}")
        print("El video está listo para ser reproducido.")
