import sys
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

def download_video(url, *format):
    try:
        output = f"{DOWNLOAD_LOCATION}%(title)s.%(ext)s"

        subprocess.run(["yt-dlp", *format, "-o", output, url], check=True)
        if format == tuple(MP4_FORMAT):
            print("✓ Video downloaded succesfully.")
        elif format == tuple(MP3_FORMAT):
            print("✓ Audio downloaded succesfully.")
    except subprocess.CalledProcessError as e:
        print(f"X Error downloading the video: {e}")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You have to give only one argumnet: -v or -a")
        sys.exit(1)
    mode = sys.argv[1]
    if mode not in ["-v", "-a"]:
        print(f"Invalid argument. It has to be -v (for [V]ideo) or -a (for [A]udio)")
        sys.exit(1)
    if mode == "-v":
        print(" Youtube video is dowloading...")
        download_video(url_youtube, *MP4_FORMAT)
    if mode == "-a":
        print(" Youtube audio is dowloading...")
        download_video(url_youtube, *MP3_FORMAT)
