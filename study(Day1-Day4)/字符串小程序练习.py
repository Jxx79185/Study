while True:
    msg = input('>:').strip()
    if not msg:
        continue
    str_count=0
    int_count=0
    space_count=0
    special_count=0
    for i in msg:
        if i.isalpha():
            str_count+=1
    
        elif i.isdigit():
            int_count+=1

        elif i.isspace():
            space_count+=1

        else:
            special_count+=1

    print(str_count,int_count,space_count,special_count)