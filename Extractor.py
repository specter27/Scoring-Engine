import textract

from NameGenerator import NameGenerator
from Sanitisor import Sanitisor


class Extractor:
    # Specify the path to the uploaded PDF file
    __uploaded_file_path = ""
    __filename = ""
    # variable to be set if the resume needs to be cleaned/sanitized
    __cleaning_req = False
    # 0 -> resume & 1 -> job-description
    __file_type = 0
    __sanitised_file = []

    def __init__(self, path, cleanup, file_type):
        # start the extraction when the Extractor is initialized
        self.__uploaded_file_path = path
        self.__cleaning_req = cleanup
        self.__file_type = file_type
        self.__sanitised_file = []
        self.start_extraction()

    def start_extraction(self):
        # 1. Extract text from the PDF/docx file
        text = textract.process(self.__uploaded_file_path, method='pdfminer')

        # Convert the text to a string and print it
        text = text.decode('utf-8')
        # Generating a random name for the resume file
        generated_filename = NameGenerator().get_name()
        if self.__file_type == 0:
            generated_file_path = "extracted_resumes/extracted_" + generated_filename + "_resume.txt"
        else:
            generated_file_path = "extracted_job-descriptions/extracted_" + generated_filename + "_job-description.txt"
        self.__filename = generated_filename
        # Open a new file for writing
        with open(generated_file_path, 'w') as output_file:
            # Write the text to the file
            output_file.write(text)

        # Sanitization done only if the user requested and set the cleaning req
        self.__sanitised_file = Sanitisor(generated_file_path,  generated_filename, self.__cleaning_req, self.__file_type).get_cleaned_file()



    def get_sanitised_file(self):
        return self.__sanitised_file