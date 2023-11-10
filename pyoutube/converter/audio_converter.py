import os
import sys

import eyed3
from pytube import YouTube, Playlist
from pydub import AudioSegment

sys.path.append(os.getcwd())
from pyoutube.utils import refactoring_title

def cut_audio(filename, input_path, output_path, start_time=0, end_time=None):
    input_path_file = os.path.join(input_path, refactoring_title(filename))
    output_path_file = os.path.join(output_path, refactoring_title(filename))
    print('try to cut:', input_path_file)
    file_extention = filename.split('.')[1]

    try:
        audioFile = AudioSegment.from_file(input_path_file, format=file_extention)
        trimmed_mp3File = audioFile[start_time:] if end_time is None else audioFile[start_time:end_time]
        trimmed_mp3File.export(output_path_file, format=file_extention)
        print(f'cut audio success {filename}')
        enterinfo_audio(filename, input_path, output_path)
    except Exception as e:
        print(f'cut audio fail {filename}')
        print(e)
    
def enterinfo_audio(filename, input_path, output_path):
    input_path_file = os.path.join(input_path, refactoring_title(filename))
    output_path_file = os.path.join(output_path, refactoring_title(filename))
    
    srcFile = eyed3.load(input_path_file)
    dstFile = eyed3.load(output_path_file)
    dstFile.tag.title = srcFile.tag.title
    dstFile.tag.artist = srcFile.tag.artist
    dstFile.tag.album = srcFile.tag.album
    dstFile.tag.album_artist = srcFile.tag.album_artist
    
    dstFile.tag.save()
    
def enterinfo_mp3_youtube(yt: YouTube, playlist: Playlist, filename: str, download_path: str) -> None:
    filename = os.path.join(download_path, refactoring_title(filename))
    
    audioFile = eyed3.load(filename)
    audioFile.tag.title = yt.title
    audioFile.tag.artist = yt.author
    audioFile.tag.album = playlist.title
    audioFile.tag.album_artist = 'Various Artist'
    
    audioFile.tag.save()
    
if __name__ == "__main__":
    from pyoutube.utils import refactoring_url
    input_path = './download/intro'
    output_path = './download'
    files = [ file for file in os.listdir(input_path) if file.find('mp3') > 0 ]
    
    for file in files:
        cut_audio(file, input_path, output_path, 7718, None)
    