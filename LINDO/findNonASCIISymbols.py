with open("mathModel.py") as fp:
    for i, line in enumerate(fp):
        if "\xc4" in line:
            print (i, repr(line))