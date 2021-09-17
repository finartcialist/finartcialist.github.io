from datetime import datetime as dt
from dateutil.tz import gettz
import os
from feedgen.feed import FeedGenerator

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
    for f in files:
        fe = fg.add_entry()
        fe.id("https://www.finartcialist.com/fr/"+ path + f)
        fe.title(f)
        if len(path) > 0:
            fe.link(href="https://www.finartcialist.com/fr/" + path + '/' + f)
        else:
            fe.link(href="https://www.finartcialist.com/fr/" + f)
        fe.updated(dt.fromtimestamp(os.path.getmtime("./fr/" + path + '/'+ f),tz=gettz("America/New York")))

fg.atom_file('fr/atom_fr.xml')
