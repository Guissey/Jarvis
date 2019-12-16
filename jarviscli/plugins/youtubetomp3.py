from __future__ import unicode_literals
import Jarvis
from colorama import Fore
from plugin import plugin, require
import youtube_dl
import os
from pathlib import Path

@require(network=True, native=["ffmpeg"])
@plugin('youtubetomp3')

def youtubetomp3(jarvis, s):
    '''
    Download the audio from the video in the specified youtube url. Also works for playlists. The file(s) will be downloaded in the Music folder or, if not found, in a folder named youtubetomp3. Just type youtubetomp3, then follow the instruction.
    '''
    
    #Looking for music folder. If not found the file will be downloaded in the created directory youtubetomp3 in home.
    music_trads = ['Music', 'music', 'Musique', 'Moussiiqa', 'Glazba', 'Musik', 'Música', 'Musica', 'Muziko', 'Muusika', 'Musiikki', 'Cerddoriaeth', 'Zene', 'Mousiki', 'Muziek', 'Muzyka', 'Musikk', 'Muzicã', 'Muzika', 'Musik', 'Hudba']
    home = str(Path.home())
    dest_path = home + "/youtubetomp3"
    for music in music_trads:
        path = home + '/' + music
        if os.path.exists(path):
            dest_path = path
            break

    jarvis.say("Enter the url of the video. Copy the link then paste with Ctrl + Shift + V", Fore.BLUE)
    url = jarvis.input()
	
    ydl_opts = {
'format': 'bestaudio/best',
'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192', }],
'outtmpl': dest_path + '/%(title)s-%(id)s.%(ext)s',
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        jarvis.say("File downloaded in " + dest_path, Fore.BLUE)
    except:
        jarvis.say("An error occured. Make sure you copied the link correctly and have access to the internet", Fore.BLUE)
