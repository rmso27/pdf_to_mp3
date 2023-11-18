import pyttsx3, PyPDF2

readPDF = PyPDF2.PdfReader(open('test.pdf', 'rb')) # Read PDF content
audioEngine = pyttsx3.init() # Initialize

# Get PDF pages content
for page in range(len(readPDF.pages)):
    text = readPDF.pages[page].extract_text() # Extract text from page

# Generate .mp3 file
audioEngine.save_to_file(text, 'test.mp3')
audioEngine.say(text) # Play the text
audioEngine.runAndWait()
audioEngine.stop()
