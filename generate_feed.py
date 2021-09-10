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

for path, subFolders, files in os.walk("./fr/"):
    for f in files:
        fe = fg.add_entry()
        fe.id("https://www.finartcialist.com/fr/" + f)
        fe.title(f)
        fe.link(href="https://www.finartcialist.com/fr/demarche.html")
    

# rssfeed = fg.rss_str(pretty=True)

fg.rss_file('rss_fr.xml')
