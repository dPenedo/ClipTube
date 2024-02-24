import os
import subprocess

DOWNLOAD_LOCATION = "/home/daniel/Descargas/youtube/"
MP3_FORMAT = ["-x", "--audio-format", "mp3"]
MP4_FORMAT = ["--remux-video", "mp4"]
CLIPBOARD_PROGRAM = "xclip"


def get_clipbloard_data():
    clipbard_data = subprocess.run(
        [CLIPBOARD_PROGRAM, "-o"], capture_output=True, text=True
    )
    clipbard_text = clipbard_data.stdout
    return clipbard_text


url_youtube = get_clipbloard_data()
# TODO: Add multiple urls if there is a argument called many


def download_video(url, *formato):
    try:
        output = f"{DOWNLOAD_LOCATION}%(title)s.%(ext)s"

        subprocess.run(["yt-dlp", *formato, "-o", output, url], check=True)
        print("✓ Video downloaded succesfully.")
    except subprocess.CalledProcessError as e:
        print(f"X Error downloading the video: {e}")


# TODO: make the different media output work with argument on command line called video or audio
# Video
# download_video(url_youtube, *MP4_FORMAT)

# Audio
download_video(url_youtube, *MP3_FORMAT)
