from pytube import YouTube, Playlist, Stream, StreamQuery

def filter_streams(yt: YouTube, stream_type: str) -> StreamQuery:
    # video, audio를 구별해서 반환하는 함수
    return yt.streams.filter(type=stream_type)

def get_specific_options(yt: YouTube, stream_type: str, auto: bool) -> Stream:
    # 사용자로부터 유튜브에 올라가있는 스트림 중 다운받을 스트림을 선택하는 함수
    streams = filter_streams(yt, stream_type)
    
    if auto:
        return streams.first()
    
    print("idx\tstream")
    for idx in range(len(streams)):
        print(f'{idx+1}\t{streams[idx]}')
        
    return streams[int(input('select options: etc 1 ...'))-1]

def get_urls_from_playlist(playlist_url: str):
    # playlist로 부터 하위 유튜브 컨텐츠의 주소를 발췌하는 함수 
    
    playlist = Playlist(playlist_url)
    
    print(f"Access successfully: {playlist.title}")
    
    return playlist.video_urls

def get_stream_by_filter(yt: YouTube, opts: Stream, auto: bool) -> StreamQuery:
    # 사용자가 선택한 옵션에 맞는 스트림을 발췌하는 함수
    if auto:
        if opts.type == 'video':
            return yt.streams.filter(type=opts.type).order_by('abr').desc()
            
        else: # opts=type =='audio
            return yt.streams.filter(type=opts.type).order_by('resolution').desc()
    
    if opts.type == "video":
        stream = yt.streams.filter(
            res=opts.resolution,
            fps=opts.fps,
            type=opts.type
        )
    else: # opts.type == "audio"
        stream = yt.streams.filter(
            abr=opts.abr,
            audio_codec=opts.audio_codec,
            progressive=opts.is_progressive,
            type=opts.type
        )

    return stream

def download_stream(yt: YouTube, opts: Stream, download_path: str, auto: bool) -> None:
    # 요청에 맞는 스트림을 다운로드
    stream = get_stream_by_filter(yt, opts, auto)
    print(f'{yt.title}: {stream.first()}')
    try:
        stream.first().download(download_path)
    except AttributeError:
        print(f"Download failed: {yt.title}")
    else:
        print(f"Download complete: {yt.title}")

if __name__ == "__main__":
    playlist = Playlist(url="https://www.youtube.com/watch?v=BBdC1rl5sKY&list=PLWz0ar94hbfmGaqD_pgufx4ew9GBtN_WE&pp=iAQB")