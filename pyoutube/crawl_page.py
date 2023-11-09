from bs4 import BeautifulSoup
from lxml import etree
import requests

def crawl_webpage(url):
    
    html = requests.get(url)
    html.raise_for_status()
    soup = BeautifulSoup(html.text, "html.parser") 
    dom = etree.HTML(str(soup)) 

if __name__ == "__main__":
    soup = crawl_webpage("https://www.youtube.com/watch?v=BBdC1rl5sKY")
    
    
