import re
# This class is responsible for formatting/sanitizing the resume.txt file
class Sanitisor:

    __file_path = ""
    __cleaned_file_txt = []
    __file_type = 0
    __sanitisation_check = False
    def __init__(self,file_path,filename, cleanup_check, file_type):
        self.__file_path = file_path
        self.__sanitisation_check = cleanup_check
        self.__file_type = file_type
        self.__start_sanitization(filename)


    def __start_sanitization(self, filename):
        if self.__file_type == 0:
            cleaned_file_path = "cleaned_resumes/cleaned_" + filename + "_resume.txt"
        else:
            cleaned_file_path = "cleaned_job-descriptions/cleaned_" + filename + "_job-description.txt"

        # Open the input file in read mode and the output file in write mode
        with open(self.__file_path, 'r') as input_file, open(cleaned_file_path, 'w') as output_file:
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

                    # 3. Removing the bullets from the content
                    line = line.replace("•", "").replace("*", "").replace("-", "")

                # Write the modified line to the output file
                output_file.write(line)

        file = open(cleaned_file_path, 'r')

        # Loop through each line in the file and append it to the list
        for line in file:
            # clear the file first
            self.__cleaned_file_txt.clear()
            self.__cleaned_file_txt.append(line)


        # Close the file
        file.close()

    def get_cleaned_file(self):
        return self.__cleaned_file_txt

