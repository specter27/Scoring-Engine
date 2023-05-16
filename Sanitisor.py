import re
# This class is responsible for formatting/sanitizing the resume.txt file
class Sanitisor:

    __filename = ""
    __cleaned_resume_txt = []
    __sanitisation_check = False
    def __init__(self,filename, cleanup_check):
        self.__filename = filename
        self.__sanitisation_check = cleanup_check
        self.__start_sanitization()

    def __start_sanitization(self):
        cleaned_resume_path = f"cleaned_resumes/cleaned_{self.__filename}"
        # Open the input file in read mode and the output file in write mode
        with open(self.__filename, 'r') as input_file, open(cleaned_resume_path, 'w') as output_file:
            # Loop through each line in the input file
            for line in input_file:

                if self.__sanitisation_check:
                    # 1a. Removing the email id
                    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    # replace email addresses with an empty string
                    line = re.sub(email_regex, ' ', line)

                    # 1b. Removing phone numbers
                    mobile_regex = r"\+?[0-9]{0,2}[-. (][0-9]{3}[-. )][0-9]{3}[-. ][0-9]{4}"
                    # replace phone numbers with an empty string
                    line = re.sub(mobile_regex, ' ', line)

                    # 1c. Regular expression to remove hyperlink
                    hyperlink_regex = r"http\S+|www\.\S+"
                    # replace phone numbers with an empty string
                    line = re.sub(hyperlink_regex, '  ', line)

                    # 2. Remove extra leading & trailing whitespace characters
                    trailing_space_regex = r"\s{2,}"
                    match = re.search(trailing_space_regex, line)
                    if match:
                        line = re.sub(trailing_space_regex, '', line)
                    line = line.replace("\n", " ")




                # Write the modified line to the output file
                output_file.write(line)

        file = open(cleaned_resume_path, 'r')

        # Loop through each line in the file and append it to the list
        for line in file:
            self.__cleaned_resume_txt.append(line)

        # Close the file
        file.close()

    def get_cleaned_resume(self):
        return self.__cleaned_resume_txt

