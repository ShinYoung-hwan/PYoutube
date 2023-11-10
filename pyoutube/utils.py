import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOWNLOAD_DIR = os.path.join(BASE_DIR, 'download')

def is_exist(path: str) -> bool:
    return os.path.exists(path)

def create_dirctory(path: str) -> None:
    if not is_exist(path):
        os.makedirs(path)
        print("Download Directory is created")
        
def refactoring_download_path(opt_download_path: str) -> str:
    download_dir = DOWNLOAD_DIR if opt_download_path == "./download" else opt_download_path
    return download_dir

def refactoring_url(url: str) -> str:
    # 
    return url.replace('\\', '')

def refactoring_title(title: str) -> str:
    # '/' is used to identify the path
    return title.replace('/', '') 
    
def clear_download_directory() -> None:
    for file in os.listdir(DOWNLOAD_DIR):
        file = os.path.join(DOWNLOAD_DIR, file)
        os.remove(file)
    
if __name__ == "__main__":
    pass