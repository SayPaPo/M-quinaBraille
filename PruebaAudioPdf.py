import pyttsx
from pyPdf import PdfFileReader

engine = pyttsx.init()
engine.setProperty('voice', "spanish-latin-american")
input1 = PdfFileReader(file("tut.pdf", "rb"))
paginas = input1.getNumPages()
titulo =input1.getDocumentInfo().title
pagina1 = input1.getPage(0)
autor =input1.getDocumentInfo().author
#Extrae el texto de la pagina inicial del documento pdf
texto = pagina1.extractText()
#Reproduccion de la informacion del pdf
engine.say("El titulo de libro es %s" %titulo)
engine.say("La cantidad de paginas del libro son %s" %paginas)
engine.say("El autor del documento es %s" %autor)
engine.say("El texto de la pagina inicial es")
engine.say(texto)
engine.runAndWait()