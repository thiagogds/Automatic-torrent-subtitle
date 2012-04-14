from BeautifulSoup import BeautifulSoup

f = open('/Users/thiago/Development/Autosubs/html', 'r')
html = f.read()

soup = BeautifulSoup(html)
table = soup.find('table', {"class": "buscaDestaque"})
onclick = table['onclick']
subtitle_id = onclick[21:53]

f2 = open('/Users/thiago/Development/Autosubs/legenda_id.txt', 'w')
f2.write(subtitle_id)
f2.close
f.close()
