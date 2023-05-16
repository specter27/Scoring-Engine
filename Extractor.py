import textract

from NameGenerator import NameGenerator
from Sanitisor import Sanitisor


class Extractor:
    # Specify the path to the uploaded PDF file
    __uploaded_file_path = ""
    __filename = ""
    # variable to be set if the resume needs to be cleaned/sanitized
    __cleaning_req = False
    __extracted_resume = []

    def __init__(self, path, cleanup):
        # start the extraction when the Extractor is initialized
        self.__uploaded_file_path = path
        self.__cleaning_req = cleanup
        self.start_extraction()

    def start_extraction(self):
        # 1. Extract text from the PDF/docx file
        text = textract.process(self.__uploaded_file_path, method='pdfminer')

        # Convert the text to a string and print it
        text = text.decode('utf-8')
        # Generating a random name for the resume file
        generated_filename = NameGenerator().get_name() + "_resume.txt"
        self.__filename = generated_filename
        # Open a new file for writing
        with open(generated_filename, 'w') as output_file:
            # Write the text to the file
            output_file.write(text)

        # Sanitisation done only if the user requested and set the cleaning req
        self.__extracted_resume = Sanitisor(self.__filename, self.__cleaning_req).get_cleaned_resume()



    def get_extracted_resume(self):
        return self.__extracted_resume