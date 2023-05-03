import textract

from NameGenerator import NameGenerator

# Specify the path to the PDF file
pdf_path = 'resumes/Resume.pdf'

# Extract text from the PDF file
text = textract.process(pdf_path, method='pdfminer')

# Convert the text to a string and print it
text = text.decode('utf-8')

# Open a new file for writing
filename = NameGenerator().get_name() + "_resume.txt"
with open(filename, 'w') as output_file:
    # Write the text to the file
    output_file.write(text)