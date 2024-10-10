"""
BootCamp 2024
Jour 2
Partie 1
"""


def read_one_line(filename: str) -> str:
    """
    Read one line from a file
    :param filename: str
    :return: str
    """
    with open(filename, "r") as file:
        return file.readline()


# ---------------------------------------------------------------------
def write_text(filename: str, text: str):
    """
    Write the text in the file
    :param filename: str
    :param text: str
    """
    f = open(filename, "w")
    f.write(text)
    f.close()


# ---------------------------------------------------------------------
def copy_characters(input_file: str, output_file: str, nb: int):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read(nb)
            with open(output_file, 'a') as outfile:
                if content or nb == 0:
                    outfile.write(content + '\n')
    except:
        print("An error occurred while copying the file")

# ---------------------------------------------------------------------
def read_all_lines(filename: str) -> (list[str], list[str]):
    """
    Read a file and return a tuple with line list and list with 1/2 lines
    :param filename: str
    :return: (list[str], list[str])
    """
    file_lst = []
    with open(filename, "r") as file:
        for line in file:
            file_lst.append(line)
    file_one_lst = []
    for line in range(0, len(file_lst), 2):
        file_one_lst.append(file_lst[line])
    return (file_lst, file_one_lst)


# ---------------------------------------------------------------------
def write_text_better(filename: str, text: str):
    """
    Write the text in the file
    :param filename: str
    :param text: str
    """
    with open(filename, "w") as file:
        file.write(text)


def copy_characters_better(input_file: str, output_file: str, nb: int):
    """
    Copy the first nb characters from the input file to the output file
    :param input_file: str
    :param output_file: str
    :param nb: int
    """
    with open(input_file, "r") as file, open(output_file, "a") as file_output:
        text = file.read(nb)
        file_output.write(f"{text}\n")
