#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))












"""
#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sys = sys.argv[1:]
    arg_count = len(argv)

    if arg_count == 0:
        print(f"{arg_count} arguments.)
    elif arg_cout == 1:
        print(f"{arg_count} argument.)
    else:
        print(f"{arg_count} arguments)

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
"""
