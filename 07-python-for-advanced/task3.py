"""
Написать тесты(pytest or unittest) к предыдущим 2 заданиям, запустив которые, я бы смог бы проверить их корректность
Обязательно проверить всю критическую функциональность
"""
import unittest
import time
from task1 import SiamObj
from task2 import Message


class TestMeta(unittest.TestCase):

    def setUp(self) -> None:
        self.unit1 = SiamObj('1', '2', a=1)
        self.unit2 = SiamObj('1', '2', a=1)
        self.unit3 = SiamObj('2', '2', a=1)
        self.pool = self.unit3.pool

    def is_equal(self):
        return self.assertEqual(self.unit1, self.unit2)

    def is_not_equal(self):
        return self.assertNotEqual(self.unit1, self.unit3)

    def pool(self):
        return self.assertTrue(len(self.pool) == 1)

    def connection(self):
        self.unit3.connect('1', '2', 1).a = 2
        self.assertTrue(self.unit2.a == 2)

    def test_removal(self):
        del self.unit3
        return self.assertTrue(len(self.pool) == 1)


class TestProperty(unittest.TestCase):

    def setUp(self) -> None:
        self.m = Message()
        self.initial = self.m.msg

    def is_equal(self):
        self.assertEqual(self.initial, self.m.msg)

    def update_cache(self):
        time.sleep(3)
        self.assertNotEqual(self.initial, self.m)

    def setter(self):
        self.m.msg = 111
        self.assertEqual(self.m.msg, 111)

    def timer(self):
        self.m.msg = 'something'
        self.assertNotEqual(self.m.msg, self.initial)
        self.initial = self.m.msg
        time.sleep(2)
        self.assertEqual(self.m.msg, self.initial)


if __name__ == '__main__':
    unittest.main()