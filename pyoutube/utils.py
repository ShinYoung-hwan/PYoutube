import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOWNLOAD_DIR = os.path.join(BASE_DIR, 'download')

def is_exist(path: str) -> bool:
    return os.path.exists(path)

def create_dirctory(path: str) -> None:
    if not is_exist(path):
        os.makedirs(path)
        print("Download Directory is created")
        
def clear_download_directory() -> None:
    for file in os.listdir(DOWNLOAD_DIR):
        file = os.path.join(DOWNLOAD_DIR, file)
        os.remove(file)
        
def refactoring_download_path(opt_download_path: str):
    if opt_download_path == "./download":
        return DOWNLOAD_DIR
    else:
        return opt_download_path

if __name__ == "__main__":
    pass