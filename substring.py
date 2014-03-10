"""
Script that determines if a string is a substring of
another string.
"""


def get_strings():
    string = raw_input('Please enter a string: ')
    substring = raw_input('Please enter a substring: ')

    return string, substring

def find_the_substring(string, substring):
    for i, letter in enumerate(string):
        if letter == substring[0]:
            new_substring = string[i:(i+len(substring))]
            if new_substring == substring:
                print(substring + ' IS a substring of ' + string)
                break
    else:
        print(substring + ' is NOT a substring of ' + string)

if __name__ == '__main__':
    string, substring = get_strings()
    find_the_substring(string, substring)