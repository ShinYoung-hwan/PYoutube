import argparse

from pytube import YouTube, Playlist
from pytube.cli import on_progress

from pyoutube.download import get_urls_from_playlist, download_stream, get_specific_options
from pyoutube.utils import refactoring_download_path, refactoring_url
from pyoutube.converter.utils import webm2mp3, remove_original
from pyoutube.converter.audio_converter import enterinfo_mp3_youtube

def parse_opt():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--download_path", type=str, default="./download")
    parser.add_argument("--type", type=str, default="video", choices=['video', 'audio'],help="video or audio")
    parser.add_argument("--url", type=str, default="https://www.youtube.com/watch?v=qBjLW5_dGAM&list=PLbpi6ZahtOH6GomiNz1MJDa2aQOeFiMKH&pp=iAQB", help="basic youtube url")
    
    return parser.parse_args()

def run(url: str, download_type: str, download_path: str, auto: bool) -> YouTube|str:
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = get_specific_options(yt, download_type, auto)
        download_stream(yt, stream, download_path, auto)
        
        return yt
    except Exception as e:
        print(e)
        return 'Exception'

if __name__ == "__main__":
    opt = parse_opt()
    download_path, download_type, url, auto = opt.download_path, opt.type, opt.url, True
    
    download_url = refactoring_url(url)
    download_path = refactoring_download_path(download_path)
    
    urls = get_urls_from_playlist(download_url)
    for url in urls:
        yt = run(refactoring_url(url), download_type, download_path, auto)
        if yt == 'Exception':
            continue
        
        playlist = Playlist(download_url)
        
        srcFile, dstFile = webm2mp3(yt.title, download_path)
        remove_original(srcFile, download_path)
        
        enterinfo_mp3_youtube(yt, playlist, dstFile, download_path)
    