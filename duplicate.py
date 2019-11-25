def find_duplicate(first_string):
    new_string=''
    x = ''
    for ch in first_string:
        if ch not in new_string:
            new_string = new_string + ch
    print(new_string)
find_duplicate('SSTRING')
