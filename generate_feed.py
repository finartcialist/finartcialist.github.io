from datetime import datetime as dt
from dateutil.tz import gettz
import os
from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup

fg = FeedGenerator()
fg.load_extension('base')

fg.id('https://www.finartcialist.com/fr/index.html')
fg.title('finartcialist')
fg.author( {'name':'finartcialist', 'email':'info@finartcialist.com'})
fg.link( href="https://www.finartcialist.com", rel='alternate')
fg.subtitle("Fil RSS - finartcialist - arts x finance")
fg.link(href="https://www.finartcialist.com", rel="self")
fg.language("fr")

for root, subFolders, files in os.walk("./fr/"):
    path = os.path.basename(root)
    print(path)
    for f in files:
        if f != "atom_fr.xml":
            if len(path) > 0:
                path_to_html = 'fr/' + path + '/' + f
            else:
                path_to_html = 'fr/' + f
            print(path_to_html)
            with open('./' + path_to_html) as html_text:
                soup = BeautifulSoup(html_text, 'html.parser')
                title = soup.title.string

            fe = fg.add_entry()
            fe.id("https://www.finartcialist.com/" + path_to_html)
            fe.title(title)
            if len(path) > 0:
                fe.link(href="https://www.finartcialist.com/fr/" + path + '/' + f)
            else:
                fe.link(href="https://www.finartcialist.com/fr/" + f)
            fe.updated(dt.fromtimestamp(os.path.getmtime("./fr/" + path + '/'+ f),tz=gettz("America/New York")))

fg.atom_file('fr/atom_fr.xml')

fg_en = FeedGenerator()
fg_en.load_extension('base')

fg_en.id('https://www.finartcialist.com/en/index.html')
fg_en.title('finartcialist')
fg_en.author( {'name':'finartcialist', 'email':'info@finartcialist.com'})
fg_en.link( href="https://www.finartcialist.com", rel='alternate')
fg_en.subtitle("Fil RSS - finartcialist - arts x finance")
fg_en.link(href="https://www.finartcialist.com", rel="self")
fg_en.language("fr")

for root, subFolders, files in os.walk("./en/"):
    path = os.path.basename(root)

    for f in files:
        if f != "atom_en.xml":
            if len(path) > 0:
                path_to_html = 'en/' + path + '/' + f
            else:
                path_to_html = 'en/' + f
            print(path_to_html)
            with open('./' + path_to_html) as html_text:
                soup = BeautifulSoup(html_text, 'html.parser')
                title = soup.title.string    
    
            fe = fg_en.add_entry()
            fe.id("https://www.finartcialist.com/" + path_to_html)
            fe.title(title)
            if len(path) > 0:
                fe.link(href="https://www.finartcialist.com/en/" + path + '/' + f)
            else:
                fe.link(href="https://www.finartcialist.com/en/" + f)
            fe.updated(dt.fromtimestamp(os.path.getmtime("./en/" + path + '/'+ f),tz=gettz("America/New York")))

fg_en.atom_file('en/atom_en.xml')
