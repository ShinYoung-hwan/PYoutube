from pytube import YouTube

from pyoutube.download import get_url_from_playlist, download_video, download_audio, get_specific_options
from pyoutube.opt_selector import parse_opt

from pyoutube.utils import refactoring_download_path

def run_type_video(url: str, opt_type: str, download_path: str):
    yt = YouTube(url)
    opts = get_specific_options(yt, opt_type)
    download_video(yt, opts, download_path)

def run_type_audio(url: str, opt_type: str, download_path: str):
    yt = YouTube(url)
    opts = get_specific_options(yt, opt_type)
    download_audio(yt, opts, download_path)

if __name__ == "__main__":
    opt = parse_opt()
    download_path, is_playlist, opt_type, download_url = opt.download_path, opt.is_playlist, opt.type, opt.url
    print("User options: ", opt)
    
    download_path = refactoring_download_path(download_path)
    
    if is_playlist:
        urls = get_url_from_playlist(download_url)
        
        for url in urls:
            if opt_type == "video":
                run_type_video(url, opt_type, download_path)
            elif opt_type == "audio":
                run_type_audio(url, opt_type, download_path)
        
    elif opt_type == 'video':
        run_type_video(download_url, opt_type, download_path)
    else: # opt_type == "audio"
        run_type_audio(download_url, opt_type, download_path)
        
