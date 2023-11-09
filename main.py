from pytube import YouTube
from pytube.cli import on_progress

from pyoutube.download import get_urls_from_playlist, download_stream, get_specific_options
from pyoutube.opt_selector import parse_opt
from pyoutube.utils import refactoring_download_path, refactoring_url

def run(url: str, opt_type: str, download_path: str, auto: bool) -> None:
    yt = YouTube(url, on_progress_callback=on_progress)
    opts = get_specific_options(yt, opt_type, auto)
    download_stream(yt, opts, download_path, auto)

if __name__ == "__main__":
    opt = parse_opt()
    download_path, is_playlist, opt_type, download_url, auto = opt.download_path, opt.playlist, opt.type, refactoring_url(opt.url), opt.auto
    print("User options: ", opt)
    
    download_path = refactoring_download_path(download_path)
    
    # download playlist
    if is_playlist:
        urls = get_urls_from_playlist(download_url)
        for url in urls:
            run(url, opt_type, download_path, auto)
    
    # download a content
    else:
       run(download_url, opt_type, download_path, auto)
        
