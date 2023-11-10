import os
import subprocess

from pyoutube.utils import refactoring_title
    
def webm2mp3(title: str, download_path: str) -> tuple:
    # Reference https://github.com/ooutama/WebmToMp3/blob/main/WebmToMp3.py
    webmFile = os.path.join(download_path, refactoring_title(title)+'.webm')
    mp3File = webmFile.replace('webm', 'mp3')

    command = f"ffmpeg -i \"{webmFile}\" -vn -ab 128k -ar 44100 -y \"{mp3File}\""
    subprocess.call(command, shell=True)
    
    return title+'.webm', title+'.mp3'
    
def remove_original(filename: str, download_path: str) -> None:
    filename = os.path.join(download_path, refactoring_title(filename))
    os.remove(filename) 

if __name__ == "__main__":
    
    titles = [ title for title in os.listdir('./download') if title.find('webm') >= 1]
    
    for title in titles:
        webm2mp3(title, './download')
        remove_original(title, './download')
    print("convert is done")
    
    
    