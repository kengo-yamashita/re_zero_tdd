import unittest
from test.support import captured_stdout

FIZZ_BUZZ = "FizzBuzz"
FIZZ = "Fizz"
BUZZ = "Buzz"
data = {
    'values': [],
    'count': 100
}


def execute():
    set_count()
    set_values_by_generate()
    print_values()


def set_count():
    # 配列は0から始めまるので100まで出すのに必要
    data['count'] = data['count'] + 1


def set_values_by_generate():
    for n in range(data['count']):
        value = generate(n)
        data['values'].append(value)


def print_values():
    for value in data['values']:
        print(value)


def generate(number):
    value = number

    if number % 3 == 0 and number % 5 == 0:
        value = FIZZ_BUZZ
    elif number % 3 == 0:
        value = FIZZ
    elif number % 5 == 0:
        value = BUZZ

    return value


class MainTest(unittest.TestCase):

    def setUp(self):
        with captured_stdout() as stdout:
            execute()
            self.lines = stdout.getvalue().splitlines()

    def test_1から100まで数をプリントできるようにする(self):
        self.assertEqual("1", self.lines[1])
        self.assertEqual("Buzz", self.lines[100])

    def test_3の倍数のときは数の代わりにFizzをプリントする(self):
        self.assertEqual("Fizz", self.lines[3])

    def test_5の倍数のときはBuzzとプリントする(self):
        self.assertEqual("Buzz", self.lines[5])

    def test_3と5両方の倍数の場合にはFizzBuzzとプリントする(self):
        self.assertEqual("FizzBuzz", self.lines[15])


if __name__ == "__main__":
    unittest.main()
