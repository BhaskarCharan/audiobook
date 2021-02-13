import pyttsx3
import PyPDF2
book =open('dsa.pdf', 'rb')
pdfReader =PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker =pyttsx3.init()
page = pdfReader.getPage(17)
text = page.extractText()
speaker.say(text)
speaker.say('hello sai bhaskar charan')
speaker.runAndWait()
