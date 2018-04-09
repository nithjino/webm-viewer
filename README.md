# Webm Viewer
Why did I make this? I just wanted a simple way to view a folder of webm clips. I know I can just make any video player to open up a folder but that isn't any fun

## Requirements:
* Python 3
* [PyQt](https://www.riverbankcomputing.com/software/pyqt/download5)
* [python-mpv](https://github.com/jaseg/python-mpv)
* [libmpv](https://github.com/jaseg/python-mpv#libmpv-no-kidding)

## Instructions
File -> Open Folder that contains the webms. The application will store all the webm locations

Press `z` to go backwards in the playlist. 

Press `x` to go forwards in the playlist. This will loop around the playlist. Ex: If you are at the first video in the playlist and want to go backwards, it will play the last video in the playlist.

Press `m` to mute or unmute the video.

Press `space` to pause or play the video

## Screenshots
![alt text](https://media.discordapp.net/attachments/224644073795878913/432742874967441418/unknown.png)

## Things I want to implement if I find the time to do so
- [x] mute the video without having to use an input config
- [x] pause the video without having to use an input config
- [ ] loop the video without having to use a mpv config