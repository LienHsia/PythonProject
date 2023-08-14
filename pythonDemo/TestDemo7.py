def get_new_str():
    string = input()
    str_len = len(string)
    if str_len<2:
        print('EmptyString')
    elif str_len==2:
        print(string+string)
    else:
        print(string[:2]+string[-2:])
        
get_new_str()
