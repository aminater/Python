"collect command-line options in a dictionary"

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts

if __name__ == "__main__":
    from sys import argv
    myargs = getopts(argv)
    if '-1' in myargs:
        print(myargs['-1'])
    print(myargs)