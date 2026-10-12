from main import *


def test01():
    balance = Balance(35, [Person(300, 15), Person(200, 10), Person(7, 5)])
    balance.giving()

if __name__ == "__main__":
    test01()
