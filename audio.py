import os
from pytube import Playlist, YouTube
import argparse
import re

class verbose:
    """ANSI color codes for terminal output."""
    STOP = '\033[0m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    INFO = f'\033[92m{BOLD} [INFO] {STOP}'
    WARNING = f'\033[93m{BOLD} [WARNING] {STOP}'
    ERROR = f'\033[91m{BOLD} [ERROR] {STOP}'

def print_info(message):
    """Prints an information message."""
    print(verbose.INFO + message)

def print_warning(message):
    """Prints a warning message."""
    print(verbose.WARNING + message)

def print_error(message):
    """Prints an error message."""
    print(verbose.ERROR + message)

def get_playlist_videos(playlist_id):
    """
    Get video URLs from a playlist ID.
    """
    playlist = Playlist(f'https://www.youtube.com/playlist?list={playlist_id}')
    return playlist.video_urls

def download_and_convert_to_mp3(playlist_input):
    try:
        # Check if input is a full URL or just the playlist ID
        if playlist_input.startswith("https://www.youtube.com/playlist?list="):
            playlist_id = re.search(r'list=([^\s&]+)', playlist_input).group(1)
        else:
            playlist_id = playlist_input

        # Download videos from the playlist
        print_info("Fetching playlist information...")
        playlist_videos = get_playlist_videos(playlist_id)
        print_info(f"Found {verbose.UNDERLINE}{len(playlist_videos)}{verbose.STOP} videos in the playlist.")

        for video_url in playlist_videos:
            try:
                video = YouTube(video_url)
                audio_stream = video.streams.filter(only_audio=True, file_extension='mp4').first()
                if audio_stream:
                    print_info(f"Downloading video for: {verbose.UNDERLINE}{video.title}{verbose.STOP}")
                    audio_stream.download()
                else:
                    print_warning(f"Could not find video stream for : {verbose.UNDERLINE}{video.title}{verbose.STOP}")
            except Exception as e:
                print_error(f"Error downloading video for {verbose.UNDERLINE}{video_url}{verbose.STOP}: {str(e)}")

        # Convert downloaded videos to MP3
        print_info("Converting videos to MP3 format...")
        for file in os.listdir('.'):
            if file.endswith(".mp4"):
                try:
                    # Rename the file extension from mp4 to mp3
                    os.rename(file, os.path.splitext(file)[0] + '.mp3')
                except Exception as e:
                    print_error(f"Error converting video {verbose.UNDERLINE}{file}{verbose.STOP} to MP3: {str(e)}")
        print_info("Download and conversion completed successfully.")

    except Exception as e:
        print_error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and convert YouTube playlist videos to MP3.")
    parser.add_argument("-p", "--playlist", type=str, help="URL or ID of the YouTube playlist")
    args = parser.parse_args()

    if args.playlist:
        download_and_convert_to_mp3(args.playlist)
    else:
        playlist_input = input("Enter the URL or ID of the YouTube playlist: ")
        download_and_convert_to_mp3(playlist_input)
