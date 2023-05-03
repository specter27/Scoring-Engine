# This class is responsible for formatting/sanitizing the resume.txt file
class Sanitisor:


    __filename = ""
    def __init__(self,filename):
        self.__filename = filename
        self.__start_sanitization()

    def __start_sanitization(self):
        print(self.__filename)
        # # Open the input file in read mode and the output file in write mode
        # with open(self.filename, 'r') as input_file, open('output_file.txt', 'w') as output_file:
        #     # Loop through each line in the input file
        #     for line in input_file:
        #
        #         # Strip the bullet (assuming it's a dash or asterisk followed by a space)
        #         stripped_line = line.replace('-*', ' ')
        #
        #         if '\t' in stripped_line:
        #             print("The string contains 'tabs'")
        #             stripped_line = line.replace('●\t', ' ')
        #
        #         # Remove extra spaces between the words
        #         # Split the string into words
        #         words = stripped_line.split()
        #         # Join the words with a single space
        #         stripped_line = ' '.join(words)
        #
        #         # Write the modified line to the output file
        #         output_file.write(stripped_line)
        #
        # file = open('output_file.txt', 'r')
        # # Initialize an empty list to store the lines
        # lines = []
        #
        # # Loop through each line in the file and append it to the list
        # for line in file:
        #     lines.append(line.strip())
        #
        # # Close the file
        # file.close()
        #
        # # Print the list of lines
        # print(lines)

