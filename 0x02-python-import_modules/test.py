#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_count = len(argv)

    if arg_count == 0:
        print(f"{arg_count} arguments.")
    elif arg_count == 1:
        print(f"{arg_count} argument:")
    else:
        print(f"{arg_count} arguments:")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}😂❤")
