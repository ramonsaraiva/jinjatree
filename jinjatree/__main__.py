import sys

from core import JinjaTree


if __name__ == '__main__':
    try:
        tree = JinjaTree(sys.argv[1])
        tree.render()
    except IndexError:
        print('Please provide a starter path for the jinja templates')
