from pytube import YouTube, Playlist, Stream

def filter_streams(yt: YouTube, stream_type: str) -> list:
    streams = list()
    
    for stream in yt.streams.filter(type=stream_type):
        streams.append(stream)

    return streams

def get_specific_options(yt: YouTube, stream_type: type):
    """
    <Stream: itag="17" mime_type="video/3gpp" res="144p" fps="12fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">
    <Stream: itag="18" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">
    <Stream: itag="22" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">
    <Stream: itag="313" mime_type="video/webm" res="2160p" fps="24fps" vcodec="vp9" progressive="False" type="video">
    <Stream: itag="271" mime_type="video/webm" res="1440p" fps="24fps" vcodec="vp9" progressive="False" type="video">
    <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="24fps" vcodec="avc1.640028" progressive="False" type="video">
    <Stream: itag="248" mime_type="video/webm" res="1080p" fps="24fps" vcodec="vp9" progressive="False" type="video">
    <Stream: itag="136" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.4d401f" progressive="False" type="video">
    <Stream: itag="247" mime_type="video/webm" res="720p" fps="24fps" vcodec="vp9" progressive="False" type="video">
    <Stream: itag="135" mime_type="video/mp4" res="480p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">
    <Stream: itag="244" mime_type="video/webm" res="480p" fps="24fps" vcodec="vp9" progressive="False" type="video">
    <Stream: itag="134" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">
    <Stream: itag="243" mime_type="video/webm" res="360p" fps="24fps" vcodec="vp9" progressive="False" type="video">
    <Stream: itag="133" mime_type="video/mp4" res="240p" fps="24fps" vcodec="avc1.4d4015" progressive="False" type="video">
    <Stream: itag="242" mime_type="video/webm" res="240p" fps="24fps" vcodec="vp9" progressive="False" type="video">
    <Stream: itag="160" mime_type="video/mp4" res="144p" fps="24fps" vcodec="avc1.4d400c" progressive="False" type="video">
    <Stream: itag="278" mime_type="video/webm" res="144p" fps="24fps" vcodec="vp9" progressive="False" type="video">
    <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">
    <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">
    <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">
    <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">
    <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">
    """
    streams = filter_streams(yt, stream_type)
    
    print("idx\tstream")
    for idx in range(len(streams)):
        print(f'{idx+1}\t{streams[idx]}')
        
    return streams[int(input('select options: etc 1 ...'))-1]

def get_url_from_playlist(playlist_url: str):
    playlist = Playlist(playlist_url)
    
    print(f"Access successfully: {playlist.title}")
    
    return playlist.video_urls

def download_video(yt: YouTube, opts: Stream, download_path: str):
    stream = yt.streams.filter(
        res=opts.resolution,
        fps=opts.fps,
        type=opts.type
    )
    print(stream)
    try:
        print("Downloading video now")
        stream.first().download(download_path)
        print(f"Downloading video complete: {yt.title}")
    except AttributeError:
        print(f"Downloading video failed: {yt.title}")
    
def download_audio(yt: YouTube, opts: Stream, download_path: str):
    stream = yt.streams.filter(
            abr=opts.abr,
            audio_codec=opts.audio_codec,
            progressive=opts.is_progressive,
            type=opts.type
    )
    print(stream)
    try:
        print("Downloading audio now")
        stream.first().download(download_path)
        print(f"Downloading audio complete: {yt.title}")
    except AttributeError:
        print(f"Downloading audio failed: {yt.title}")

if __name__ == "__main__":
    from opt_selector import parse_opt
    opts = parse_opt()