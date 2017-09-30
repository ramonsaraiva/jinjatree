import sys

from core import JinjaTree


if __name__ == '__main__':
    try:
        JinjaTree(sys.argv[1])
    except IndexError:
        print('Please provide a starter path for the jinja templates')
