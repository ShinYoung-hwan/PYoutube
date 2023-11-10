import argparse

from pytube import YouTube
from pytube.cli import on_progress

from pyoutube.download import get_urls_from_playlist, download_stream, get_specific_options
from pyoutube.utils import refactoring_download_path, refactoring_url

def parse_opt():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--download_path", type=str, default="./download")
    parser.add_argument("--type", type=str, default="video", choices=['video', 'audio'],help="video or audio")
    parser.add_argument("--playlist", action="store_true")
    parser.add_argument("--url", type=str, default="https://www.youtube.com/watch?v=BBdC1rl5sKY", help="basic youtube url")
    parser.add_argument("--auto", action="store_true")
    
    return parser.parse_args()

def run(url: str, download_type: str, download_path: str, auto: bool) -> None:
    yt = YouTube(url, on_progress_callback=on_progress)
    stream = get_specific_options(yt, download_type, auto)
    download_stream(yt, stream, download_path, auto)

if __name__ == "__main__":
    opt = parse_opt()
    download_path, is_playlist, download_type, download_url, auto = opt.download_path, opt.playlist, opt.type, refactoring_url(opt.url), opt.auto
    print("User options: ", opt)
    
    download_path = refactoring_download_path(download_path)
    
    # download playlist
    if is_playlist:
        urls = get_urls_from_playlist(download_url)
        for url in urls:
            run(url, download_type, download_path, auto)
    
    # download a content
    else:
       run(download_url, download_type, download_path, auto)
        
