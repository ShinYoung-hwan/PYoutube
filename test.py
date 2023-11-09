from pytube import YouTube

from pyoutube.utils import DOWNLOAD_DIR
from pyoutube.utils import get_resolutions

if __name__ == "__test__":
    url = 'https://www.youtube.com/watch?v=BBdC1rl5sKY'
    yt = YouTube(url)
    print("제목 : ", yt.title)
    print("길이 : ", yt.length)
    print("게시자 : ", yt.author)
    print("게시날짜 : ", yt.publish_date)
    print("조회수 : ", yt.views)
    print("키워드 : ", yt.keywords)
    print("설명 : ", yt.description)
    print("썸네일 : ", yt.thumbnail_url)