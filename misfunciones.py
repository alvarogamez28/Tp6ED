import feedparser

def news(k,n):
   FEED={'elp':'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml','bbc':'http://feeds.bbci.co.uk/news/world/rss.xml'}
   articles = feedparser.parse(FEED[k])['entries'][:n]
   return articles

def aula(nombre):
  with open('mifile') as f:
      for line in f:  
        campos = line.strip().split(':')
        if campos[0] == nombre:
          return campos[1]


### las siguientes ya las teníamos ###

def jugar(n1,v1,n2,v2):
  undict = {'tijera':'papel','papel':'piedra','piedra':'tijera'}
  nom = ''
  if undict[v1] == v2:
    nom = n1
  if undict[v2] == v1:
    nom = n2
  return nom

def valida_letra(letra):
       if len(letra) == 1:
         if letra.isalpha() and letra.isupper():
            return True
       if len(letra) == 2 :
         if letra == 'A5' or letra == 'B5' or letra == 'Y5' or letra == 'Z5':
            return True
       return False

def aulaAlumCarac(lista,carac,pos):
  aulas = []
  alumnosAulas = []
  for linea in lista:
    campos = linea.split(':')
    if campos[pos] == carac:
      if campos[1] in aulas:
        i = aulas.index(campos[1])
        alumnosAulas[i] = alumnosAulas[i] + ", " + campos[0]
      else:
        aulas.append(campos[1])
        alumnosAulas.append(campos[0])
  return aulas,alumnosAulas

