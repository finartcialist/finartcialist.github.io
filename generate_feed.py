# https://finartcialist.com/en/atom_en.xml

from datetime import datetime as dt
from dateutil.tz import gettz
import os
from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup

dot = "./"

fg = FeedGenerator()
fg.load_extension('base')

fg.id('https://www.finartcialist.com/v2/fr/blog/')
fg.title('blogue - finartcialist')
fg.author( {'name':'finartcialist', 'email':'info@finartcialist.com'})
fg.link( href="https://www.finartcialist.com", rel='alternate')
fg.subtitle("RSS - finartcialist - arts x finance")
fg.link(href="https://www.finartcialist.com", rel="self")
fg.language("fr")


fr_path = "v2/fr/blog/"

for root, subFolders, files in os.walk(dot + fr_path):
    path = os.path.basename(root)
    print(path)
    for f in files:
        if f != "index.html":
            if len(path) > 0:
                path_to_html = fr_path + path + '/' + f
            else:
                path_to_html = fr_path + f
            print(path_to_html)
            with open('./' + path_to_html) as html_text:
                soup = BeautifulSoup(html_text, 'html.parser')
                title = soup.title.string

            fe = fg.add_entry()
            fe.id("https://www.finartcialist.com/" + path_to_html)
            fe.title(title)
            # if len(path) > 0:
            fe.link(href="https://www.finartcialist.com/" + path_to_html)
            fe.updated(dt.fromtimestamp(os.path.getmtime(dot + fr_path + path + '/'+ f),tz=gettz("America/New York")))

fg.atom_file('fil.xml')

fg_en = FeedGenerator()
fg_en.load_extension('base')

fg_en.id('https://www.finartcialist.com/v2/en/blog')
fg_en.title('blog - finartcialist')
fg_en.author( {'name':'finartcialist', 'email':'info@finartcialist.com'})
fg_en.link( href="https://www.finartcialist.com", rel='alternate')
fg_en.subtitle("RSS - finartcialist - arts x finance")
fg_en.link(href="https://www.finartcialist.com", rel="self")
fg_en.language("en")

en_path = "v2/en/blog/"

def add_entry_english(en_path, flag_index):
    index = ["index.html", "v3-02.html", "v3-03.html"]

    for root, subFolders, files in os.walk(dot + en_path):
        path = os.path.basename(root)

        for f in files:
            if (flag_index and f == index) or (flag_index or f not in index) and f != "style.css":
                if len(path) > 0:
                    path_to_html = en_path + path + '/' + f
                else:
                    path_to_html = en_path + f
                print(path_to_html)
                with open('./' + path_to_html) as html_text:
                    soup = BeautifulSoup(html_text, 'html.parser')
                    title = soup.title.string    
    
                fe = fg_en.add_entry()
                fe.id("https://www.finartcialist.com/" + path_to_html)
                fe.title(title)
                # if len(path) > 0:
                fe.link(href="https://www.finartcialist.com/" + path_to_html)
                # else:
                #   fe.link(href="https://www.finartcialist.com/" + f)
                fe.updated(dt.fromtimestamp(os.path.getmtime(dot + en_path + path + '/'+ f),tz=gettz("America/New York")))

add_entry_english(en_path, False)
add_entry_english('v3/', False)

fg_en.atom_file('feed.xml')
