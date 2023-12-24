import os
import subprocess

download_location = "/home/daniel/Descargas/youtube/"


def obtener_portapapeles():
    datos_de_portapapeles = subprocess.run(["xclip", "-o"], capture_output=True, text=True)
    texto_de_portapapeles = datos_de_portapapeles.stdout
    return texto_de_portapapeles

url_youtube = obtener_portapapeles()

def descargar_video(url_youtube):
    try:
        output = f"{download_location}%(title)s.%(ext)s"

        subprocess.run(['yt-dlp', "-o", output, url_youtube], check=True)
        print("Video descargado.")
    except subprocess.CalledProcessError as e:
        print("Error al descargar el video:", e)

descargar_video(url_youtube)


