
# ClipTube

ClipTube is a Python script designed to interact with the system clipboard and the [yt-dlp](https://github.com/yt-dlp/yt-dlp) Python library. In my case, I use "xclip" since I'm on a Unix-like system. However, I plan to implement an option for "clip" to accommodate Windows users in the future.

## How to Install

Ensure that you have xclip installed on your system and the [yt-dlp](https://github.com/yt-dlp/yt-dlp) library.

## How to Use

Navigate to the `main.py` file and update your `download_location`:

```python
download_location = "/home/yourName/Downloads/youtube"
```


Then, just copy on your clipboard (ctrl + c) a youtube URL, go to the cloned ClipTube directory on your terminal and execute:
```bash
$ python main.py
```
