# YouTube Video Downloader and Audio Extractor

Este proyecto proporciona una herramienta para descargar videos de YouTube en formato MP4 y extraer el audio en formato MP3. Utiliza `yt-dlp` para descargar el video y `pydub` para convertir el audio.

## Requisitos

- Python 3.x
- pip (administrador de paquetes de Python)
- ffmpeg (para convertir audio)

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto:

1. **Clona el repositorio**:

    Abre una terminal y clona el repositorio (reemplaza `tu-usuario/tu-repo` con el nombre de tu repositorio):

    ```bash
    git clone https://github.com/tu-usuario/tu-repo.git
    cd tu-repo
    ```

2. **Crea un entorno virtual**:

    En la misma terminal, crea un entorno virtual para el proyecto:

    ```bash
    python -m venv myenv
    ```

3. **Activa el entorno virtual**:

    - En **Windows**:

        ```bash
        myenv\Scripts\activate
        ```

    - En **macOS/Linux**:

        ```bash
        source myenv/bin/activate
        ```

4. **Instala las dependencias**:

    Con el entorno virtual activado, instala las librerías necesarias:

    ```bash
    pip install yt-dlp pydub
    ```

    También necesitarás `ffmpeg` para la conversión de audio. Instálalo siguiendo las instrucciones de su [sitio oficial](https://ffmpeg.org/download.html).

5. **Ejecuta el script**:

    Ejecuta el script principal para descargar el video y extraer el audio. Introduce la URL del video de YouTube cuando se te solicite:

    ```bash
    python youtube_to_mp3.py
    ```

    El script descargará el video en formato MP4 y extraerá el audio en formato MP3, guardando ambos archivos en la carpeta `Descargas`.

## Estructura del Proyecto

