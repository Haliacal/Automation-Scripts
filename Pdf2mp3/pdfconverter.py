import pyttsx3,PyPDF3, pdfplumber, os

files = [f for f in os.listdir() if(os.path.isfile(f))]
speaker = pyttsx3.init()

for file in files:
    if(not file.lower().endswith(".pdf")): continue

    book = open(file, 'rb')
    pdfReader = PyPDF3.PdfFileReader(book)

    pages = pdfReader.numPages

    finalText = ""
 
    with pdfplumber.open(file) as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            finalText += page.extract_text()

    engine = pyttsx3.init()
    engine.save_to_file(finalText, file[:-4]+".mp3")
    engine.runAndWait()

    engine = pyttsx3.init()
    engine.say(finalText)
    engine.runAndWait()
    
    
