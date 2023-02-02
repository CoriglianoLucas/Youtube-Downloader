# Youtube-Downloader

## Usage
1. Download and run the .exe file found in the dist folder.
2. Enter the video URL.
3. The script will download the audio of the video as an MP3 file with the title of the video as the file name.
4. If the title of the video contains invalid characters for file names, the script will clean it and use the cleaned title for the file name.
5. The script will prompt for another URL to download. Repeat the steps until you're done.

## Note
* To generate a new exe run the command: pyinstaller --onefile YouTubeDownloader.py
* The script will only download audio with either 160kbps or 128kbps bitrate. If the video doesn't have audio with those bitrates, the download will fail.