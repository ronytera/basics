import sys


def cal(x, y):
    print(x+y)


if __name__ == '__main__':
    file_name = sys.argv[0]
    params = [int(a) for a in sys.argv[1:]]
    cal(*params)