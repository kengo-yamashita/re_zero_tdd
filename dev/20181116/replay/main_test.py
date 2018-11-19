import unittest
from test.support import captured_stdout

BUZZ = "Buzz"
FIZZ = "Fizz"
FIZZ_BUZZ = "FizzBuzz"
fizz_buzz_date = {
    'values': [],
    'count': 100
}


def execute():
    set_count()
    set_values_by_fizz_buzz()
    print_values()


def set_count():
    # レンジは指定された値を範囲に含めないので1プラスする
    fizz_buzz_date['count'] = fizz_buzz_date['count'] + 1


def set_values_by_fizz_buzz():
    for number in range(fizz_buzz_date['count']):
        value = fizz_buzz(number)
        fizz_buzz_date['values'].append(value)


def print_values():
    for value in fizz_buzz_date['values']:
        print(value)


def fizz_buzz(number):
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


class RangeTest(unittest.TestCase):
    def test_範囲を示すレンジ(self):
        rg = range(10)
        self.assertEqual(0, rg[0])
        self.assertEqual(9, rg[-1])
        rg = range(5, 10)
        self.assertEqual(5, rg[0])
        self.assertEqual(9, rg[-1])
        rg = range(10, 20, 2)
        self.assertEqual(12, rg[1])
        self.assertEqual(18, rg[-1])

    def test_レンジのシーケンス演算(self):
        rg = range(30)
        self.assertTrue(10 in rg)
        self.assertTrue(30 not in rg)
        rg = range(50)
        self.assertEqual(range(1, 4), rg[1:4])
        self.assertEqual(50, len(rg))
        self.assertEqual(49, max(rg))
        self.assertEqual(0, min(rg))

    def test_シーケンス間の変換(self):
        list1 = [100, 200, 300]
        tpl1 = (123, 'ok', True)
        rng1 = range(10, 20)
        result = list1 + list(tpl1) + list(rng1)
        self.assertEqual([100, 200, 300, 123, 'ok', True, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], result)


if __name__ == "__main__":
    unittest.main()
