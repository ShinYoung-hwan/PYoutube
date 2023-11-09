import argparse

def parse_opt():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--download_path", type=str, default="./download")
    parser.add_argument("--type", type=str, default="video", help="video or playlist or audio")
    parser.add_argument("--is_playlist", type=bool, default=False)
    parser.add_argument("--url", type=str, default="https://www.youtube.com/watch?v=BBdC1rl5sKY", help="basic youtube url")
    
    """args
    fps: Any | None = None,
    res: Any | None = None,
    resolution: Any | None = None,
    mime_type: Any | None = None,
    type: Any | None = None,
    subtype: Any | None = None,
    file_extension: Any | None = None,
    abr: Any | None = None,
    bitrate: Any | None = None,
    video_codec: Any | None = None,
    audio_codec: Any | None = None,
    only_audio: Any | None = None,
    only_video: Any | None = None,
    progressive: Any | None = None,
    adaptive: Any | None = None,
    is_dash: Any | None = None,
    custom_filter_functions: Any | None = None
    Apply the given filtering criterion.

    :param mime_type:
        (optional) Two-part identifier for file formats and format contents composed of a "type", a "subtype".
    :type mime_type:
        str or None

    :param type:
        (optional) Type part of the mime_type (e.g.: audio, video).
    :type type:
        str or None

    :param subtype:
        (optional) Sub-type part of the mime_type (e.g.: mp4, mov).
    :type subtype:
        str or None

    :param file_extension:
        (optional) Alias to sub_type.
    :type file_extension: | 
        str or None

    :param abr:
        (optional) Average bitrate (ABR) refers to the average amount of data transferred per unit of time (e.g.: 64kbps, 192kbps).
    :type abr:
        str or None

    :param bitrate:
        (optional) Alias to abr.
    :type bitrate:
        str or None

    :param video_codec:
        (optional) Video compression format.
    :type video_codec:
        str or None

    :param audio_codec:
        (optional) Audio compression format.
    :type audio_codec:
        str or None

    :param bool progressive:
        Excludes adaptive streams (one file contains both audio and video tracks).

    :param bool adaptive:
        Excludes progressive streams (audio and video are on separate tracks).

    :param bool is_dash:
        Include/exclude dash streams.

    :param bool only_audio:
        Excludes streams with video tracks.

    :param bool only_video:
        Excludes streams with audio tracks.

    :param custom_filter_functions:
        (optional) Interface for defining complex filters without subclassing.
    :type custom_filter_functions:
        list or None
        """
    
    return parser.parse_args()