# YouTube Playlist Downloader

This script allows you to download all the videos from a YouTube playlist and convert them to MP3 format.

## Requirements

- Python 3.x
- [pytube](https://pypi.org/project/pytube/)

## Installation

You can install the required dependencies using pip:

```
pip install pytube
```

## Usage

1. Run the script by executing the following command in your terminal:

```
python audio.py [-p PLAYLIST_URL]
```

- Optional Arguments:
  - `-p, --playlist PLAYLIST_URL`: URL of the YouTube playlist you want to download.

2. If you provide the `-p` flag followed by the playlist URL, the script will download and convert the videos from the specified playlist directly.
   
3. If you don't provide the `-p` flag, the script will prompt you to enter the URL of the YouTube playlist.

## Colored Output

The script provides colored output to distinguish between different types of messages:

- **[INFO]**: Informational messages displayed in green.
- **[WARNING]**: Warning messages displayed in yellow.
- **[ERROR]**: Error messages displayed in red.

## Error Handling

The script includes error handling to deal with various potential issues during the download and conversion process. Specific error messages are provided to help diagnose any problems that may occur.