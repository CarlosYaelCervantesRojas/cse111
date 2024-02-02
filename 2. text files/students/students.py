import csv

KEY_INDEX = 0

def main():
    compound_dictionary = read_dictionary('students.csv', KEY_INDEX)

    number_user = input('Please enter an I-Number (xxxxxxxxx):')

    if number_user in compound_dictionary:
        student = compound_dictionary[number_user]
        print(student)
    else:
        print('No such student')

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dictionary = {}
    with open(filename) as students_file:
        reader = csv.reader(students_file)
        next(reader)
        for row in reader:
            # if len(row) != 0:
                key = row[key_column_index]
                compound_dictionary[key] = row[1]
    return(compound_dictionary)


if __name__ == '__main__':
    main()