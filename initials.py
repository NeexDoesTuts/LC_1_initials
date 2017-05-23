def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase).
    """
    # TODO your code here

    name_list = fullname.split(" ")
    initials = ""

    for word in name_list:
        initial = word[0].upper()
        initials += initial
    print(initials)
    return initials

def main():
    test_name = input("What is your name? ")
    return_string = "Nice to meet you" + test_name +". Your initials " + get_initials(test_name) + " are chill sweet!"
    print(return_string)

if __name__ == '__main__':
    main()
