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
            bag.subtracted({"a": 1, "c": 1}).bag
        )
        self.assertEqual(
            {"c": 2, "d": 2},
            bag.subtracted({"a": 1, "b": 5, "c": 1, "d": 2, "e": 1}).bag
        )

    def test_speed_subtract(self):
        iterations = 1000
        print()
        for bag_size in [10, 100, 10_000]:
            bag1 = BagOfWords({str(i): i for i in range(bag_size)})
            bag2 = bag1.copy()
            bag1["extra"] *= 1

            start_time = time.time()
            for i in range(iterations):
                bag1.normalized()
            fps = iterations / (time.time() - start_time)
            print(f"normalized  with bag size {bag_size:7} @ {fps:12,.0f} fps")

            start_time = time.time()
            for i in range(iterations):
                bag1 - bag2
            fps = iterations / (time.time() - start_time)
            print(f"big - small with bag size {bag_size:7} @ {fps:12,.0f} fps")

            start_time = time.time()
            for i in range(iterations):
                bag2 - bag1
            fps = iterations / (time.time() - start_time)
            print(f"small - big with bag size {bag_size:7} @ {fps:12,.0f} fps")
