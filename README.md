
# ClipTube

ClipTube is a Python script designed to interact with the system clipboard and the [yt-dlp](https://github.com/yt-dlp/yt-dlp) Python library. In my case, I use "xclip" since I'm on a Unix-like system. However, I plan to implement an option for "clip" to accommodate Windows users in the future.

## How to Install

Ensure that you have xclip installed on your system and the [yt-dlp](https://github.com/yt-dlp/yt-dlp) library.
For yt-dpl:
- Option 1 (install it directly):
``` bash
pip install yt-dlp
```
- Option 2 (install it on a virtual env):
```
# On your virtual env

pip install -r requirements.txt

```
For xclip in Debian based linux, for example:
``` bash
sudo apt install xclip
```

For downloading MP3 files, you'll also need the ffmpeg binary installed on your system. On Debian-based systems, you can install it with:

``` bash
sudo apt install ffmpeg

```

## How to config

Navigate to the `main.py` file and manually update your `download_location`:

```python
download_location = "/home/yourName/Downloads/youtube"
```
Additionally, uncomment/comment the appropriate lines to choose between MP4 and MP3 formats:

``` python
# Video
# download_video(url_youtube, *MP4_FORMAT)

# Audio
download_video(url_youtube, *MP3_FORMAT)
```


## How to use
1. Copy the YouTube URL to your clipboard (Ctrl + C).
2. Navigate to the cloned ClipTube directory in your terminal.
3. Execute the following command:
```bash
$ python main.py
```
