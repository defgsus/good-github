import unittest
import time

from src.bagofwords import BagOfWords


class TestBags(unittest.TestCase):

    def test_bag_union(self):
        bag = BagOfWords({"a": 1, "b": 2, "c": 3, "d": 4})

        self.assertEqual(
            {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5},
            bag.union({"e": 5}).bag
        )
        self.assertEqual(
            {"a": 1, "b": 2, "c": 3, "d": 4},
            bag.union({"c": 100}).bag
        )

    def test_bag_difference(self):
        bag = BagOfWords({"a": 1, "b": 2, "c": 3, "d": 4})

        self.assertEqual(
            {"b": 2, "d": 4},
            bag.difference({"a": 1, "c": 1}).bag
        )
        self.assertEqual(
            {"a": 1, "b": 2, "c": 3, "d": 4},
            bag.difference({"e": 5}).bag
        )

    def test_bag_intersection(self):
        bag = BagOfWords({"a": 1, "b": 2, "c": 3, "d": 4})

        self.assertEqual(
            {"a": 1, "c": 3},
            bag.intersection({"a": 1, "c": 1}).bag
        )
        self.assertEqual(
            {},
            bag.intersection({"e": 23}).bag
        )

    def test_bag_subtract(self):
        bag = BagOfWords({"a": 1, "b": 2, "c": 3, "d": 4})

        self.assertEqual(
            {"b": 2, "c": 2, "d": 4},
            (bag - {"a": 1, "c": 1}).bag
        )
        self.assertEqual(
            {"c": 2, "d": 2},
            (bag - {"a": 1, "b": 5, "c": 1, "d": 2, "e": 1}).bag
        )

    def test_bag_isubtract(self):
        bag = BagOfWords({"a": 1, "b": 2, "c": 3, "d": 4})
        bag -= {"a": 1, "c": 3, "d": 1}
        self.assertEqual(
            {"b": 2, "d": 3},
            bag.bag
        )

        bag = BagOfWords({"a": 1, "b": 2, "c": 3, "d": 4})
        bag -= {"a": 1, "b": 5, "c": 1, "d": 2, "e": 1}
        self.assertEqual(
            {"c": 2, "d": 2},
            bag.bag
        )

    def test_speed(self):
        iterations = 1000

        def func_normalized(bag1, bag2):
            for i in range(iterations):
                bag1.normalized()

        def func_big_minus_small(bag1, bag2):
            for i in range(iterations):
                bag1 - bag2

        def func_small_minus_big(bag1, bag2):
            for i in range(iterations):
                bag2 - bag1

        def func_big_minus_small_inplace(bag1, bag2):
            for i in range(iterations):
                bag1 -= bag2

        def func_small_minus_big_inplace(bag1, bag2):
            for i in range(iterations):
                bag2 -= bag1

        def func_big_union_small(bag1, bag2):
            for i in range(iterations):
                bag1.union(bag2)

        def func_small_union_big(bag1, bag2):
            for i in range(iterations):
                bag2.union(bag1)

        functions = (
            func_normalized,
            func_big_minus_small,
            func_small_minus_big,
            func_big_minus_small_inplace,
            func_small_minus_big_inplace,
            func_big_union_small,
            func_small_union_big,
        )

        print()
        for bag_size in [10, 100, 10_000]:
            for func in functions:

                bag1 = BagOfWords({str(i): i for i in range(bag_size*2)})
                bag2 = BagOfWords({str(i): i for i in range(bag_size)})

                start_time = time.time()
                func(bag1, bag2)
                fps = iterations / (time.time() - start_time)
                print(f"{func.__name__:30}: bag size {bag_size:7} @ {fps:12,.0f} fps")
