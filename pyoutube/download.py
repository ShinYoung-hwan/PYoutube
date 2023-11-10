from pytube import YouTube, Playlist, Stream, StreamQuery

from pyoutube.utils import refactoring_title

def filter_streams(yt: YouTube, download_type: str) -> StreamQuery:
    # video, audio를 구별해서 반환하는 함수
    return yt.streams.filter(type=download_type)

def get_specific_options(yt: YouTube, download_type: str, auto: bool) -> Stream:
    # 사용자로부터 유튜브에 올라가있는 스트림 중 다운받을 스트림을 선택하는 함수
    streams = filter_streams(yt, download_type)
    if auto:
        return streams.first()
    
    print("itag\tstream")
    for stream in streams.order_by('itag').asc():
        print(f'{stream.itag}\t{stream}')
        #yt.streams.get_by_itag 요런 사용법이 있음.
    
    itag = int(input("Select itag that you want to download: "))
    return streams.get_by_itag(itag)

def get_urls_from_playlist(playlist_url: str):
    # playlist로 부터 하위 유튜브 컨텐츠의 주소를 발췌하는 함수 
    
    playlist = Playlist(playlist_url)
    
    print(f"Access successfully: {playlist.title}")
    
    return playlist.video_urls

def get_stream_by_filter(yt: YouTube, stream: Stream, auto: bool) -> Stream:
    # 사용자가 선택한 옵션에 맞는 스트림을 발췌하는 함수
    if auto:
        if stream.type == 'video':
            return yt.streams.filter(type=stream.type).order_by('resolution').desc().first()
            
        else: # opts=type =='audio
            return yt.streams.filter(type=stream.type).order_by('abr').desc().first()
    
    stream = yt.streams.get_by_itag(stream.itag)
    
    return stream

def download_stream(yt: YouTube, stream: Stream, download_path: str, auto: bool) -> None:
    # 요청에 맞는 스트림을 다운로드
    stream = get_stream_by_filter(yt, stream, auto)
    print(f'{yt.title}: {stream}')
    try:
        stream.download(download_path, ''.join([refactoring_title(yt.title), '.', stream.mime_type.split('/')[1]]))
    except AttributeError:
        print(f"Download failed: {yt.title}")
    else:
        print(f"Download complete: {yt.title}")

if __name__ == "__main__":
    playlist = Playlist(url="https://www.youtube.com/watch?v=BBdC1rl5sKY&list=PLWz0ar94hbfmGaqD_pgufx4ew9GBtN_WE&pp=iAQB")