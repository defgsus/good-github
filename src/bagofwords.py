import re
import json
import io
from pathlib import Path
from typing import List, Union, Optional, Dict, Tuple, Generator

Number = Union[int, float]
WordDict = Dict[str, Number]
WordBagArgument = Union[str, List[str], WordDict, "BagOfWords"]


TOKEN_SEPARATORS = set(" _.!?,;/\\\"`+-*=:()[]{}\r\n\t<>@~")
TOKEN_STRIP = "'“”&=#"


def tokenize(text: str) -> List[str]:
    tokens = []
    token = []

    def add_token(token):
        token = "".join(token).strip(TOKEN_STRIP)
        if token and not any(c.isnumeric() for c in token):
            tokens.append(token)

    for c in text:
        if c in TOKEN_SEPARATORS:
            if token:
                add_token(token)

            token = []

        elif ord(c) < 0x100:
            token.append(c)

    if token:
        add_token(token)

    return tokens


class BagOfWords:

    def __init__(self, data: Optional[WordBagArgument] = None):
        self.is_normalized = False
        if isinstance(data, dict):
            self.bag = data
        else:
            self.bag = dict()
            if data:
                self += data

    def __copy__(self) -> "BagOfWords":
        bag = BagOfWords()
        bag.bag = self.bag.copy()
        bag.is_normalized = self.is_normalized
        return bag

    def __bool__(self) -> bool:
        return bool(self.bag)

    def __iadd__(self, other: WordBagArgument) -> "BagOfWords":
        self.is_normalized = False
        for key, value in self._iter_items(other):
            self.bag[key] = self.bag.get(key, 0) + value
        return self

    def __add__(self, other: WordBagArgument) -> "BagOfWords":
        new_bag = self.__copy__()
        new_bag += other
        return new_bag

    def __isub__(self, bag: "BagOfWords") -> "BagOfWords":
        return self.subtract(bag)

    def __sub__(self, bag: "BagOfWords") -> "BagOfWords":
        return self.subtracted(bag)

    def __imul__(self, value: Number) -> "BagOfWords":
        self.is_normalized = False
        for key in self.bag:
            self.bag[key] *= value
        return self

    def __mul__(self, other: Number) -> "BagOfWords":
        new_bag = self.__copy__()
        new_bag *= other
        return new_bag

    def __itruediv__(self, value: Number) -> "BagOfWords":
        self.is_normalized = False
        for key in self.bag:
            self.bag[key] /= value
        return self

    def __truediv__(self, other: Number) -> "BagOfWords":
        new_bag = self.__copy__()
        new_bag /= other
        return new_bag

    def __str__(self):
        file = io.StringIO()
        self.dump(top=20, file=file)
        file.seek(0)
        return file.read()
    
    def __getitem__(self, item) -> Number:
        return self.bag.get(item, 0)

    def __setitem__(self, key: str, value: Number):
        self.bag[key] = value

    def copy(self) -> "BagOfWords":
        return self.__copy__()

    def size(self) -> int:
        return len(self.bag)

    def count(self) -> Number:
        return sum(self.bag.values()) if self.bag else 0
    
    def max(self) -> Number:
        return max(self.bag.values()) if self.bag else 0

    def items(self) -> Generator[Tuple[str, Number], None, None]:
        return self.bag.items()

    def normalized(self, copy: bool = False) -> "BagOfWords":
        if self.is_normalized:
            return self.__copy__() if copy else self

        bag = self.copy()
        factor = 1 / (self.count() or 1)
        bag.bag = {
            key: value * factor
            for key, value in self.bag.items()
        }
        bag.is_normalized = True
        return bag

    def n(self, copy: bool = False) -> "BagOfWords":
        return self.normalized(copy=copy)

    def adjust_count(self, count: Number) -> "BagOfWords":
        bag = BagOfWords()
        cur_count = self.count()
        if not cur_count:
            return bag
        factor = 1. / cur_count * count
        bag.bag = {
            key: value * factor
            for key, value in self.bag.items()
        }
        return bag

    def limited(self, min_count: Optional[int] = None, max_count: Optional[int] = None) -> "BagOfWords":
        bag = BagOfWords()
        for key, value in self.items():
            if min_count is None or value >= min_count:
                if max_count is None or value <= max_count:
                    bag.bag[key] = value
        return bag

    def sort(self) -> "BagOfWords":
        self.bag = {
            key: self.bag[key]
            for key in sorted(sorted(self.bag), key=lambda k: -self.bag[k])
        }
        return self

    def add_word(self, word: str, count: int = 1):
        self.bag[word] = self.bag.get(word, 0) + count

    def subtract(self, other: WordBagArgument, amount: Optional[Number] = None) -> "BagOfWords":
        """
        Subtract value of other
        :param other: text, tokens, dict or BagOfWords
        :param amount: optional number to multiply other's values
        :return: self
        """
        self.is_normalized = False
        other_dict = self._as_dict(other)

        if self.size() > len(other_dict):
            if amount is None:
                for key, value in other_dict.items():
                    if key not in self.bag:
                        continue

                    value = self.bag[key] - value
                    if value <= 0:
                        del self.bag[key]
                    else:
                        self.bag[key] = value
            else:
                for key, value in other_dict.items():
                    if key not in self.bag:
                        continue

                    value = self.bag[key] - amount * value
                    if value <= 0:
                        del self.bag[key]
                    else:
                        self.bag[key] = value
        else:
            new_dict = dict()
            self._subtract_dict(new_dict, other_dict, amount)
            self.bag = new_dict
        return self

    def subtracted(self, other: WordBagArgument, amount: Optional[Number] = None) -> "BagOfWords":
        other_dict = self._as_dict(other)
        bag = BagOfWords()
        self._subtract_dict(bag.bag, other_dict, amount)
        return bag

    def _subtract_dict(self, new_bag: dict, other: dict, amount: Optional[Number]):
        if amount is None:
            for key, value in self.items():
                if key not in other:
                    new_bag[key] = value
                else:
                    value -= other[key]

                    if value > 0:
                        new_bag[key] = value
        else:
            for key, value in self.items():
                if key not in other:
                    new_bag[key] = value
                else:
                    value -= other[key] * amount

                    if value > 0:
                        new_bag[key] = value

    def union(self, other: WordBagArgument):
        bag = self.__copy__()
        for key, value in self._iter_items(other):
            if key not in self.bag:
                bag.bag[key] = value
        bag.is_normalized = False
        return bag

    def intersection(self, other: WordBagArgument):
        bag = BagOfWords()
        bag.bag = {
            key: self.bag[key]
            for key, _ in self._iter_items(other)
            if key in self.bag
        }
        return bag

    def difference(self, other: WordBagArgument):
        other_dict = self._as_dict(other)
        bag = BagOfWords()
        bag.bag = {
            key: value
            for key, value in self.items()
            if key not in other_dict
        }
        return bag

    def get_subset(
            self,
            big_bag: "BagOfWords",
            max_freq: float = 1.,
            min_freq_mult: float = 2.,
    ) -> Dict[str, Dict[str, Number]]:
        self_norm = self.normalized()
        other_norm = big_bag.normalized()
        result = dict()
        for key, self_value in self_norm.items():
            if self_value <= max_freq:
                other_value = other_norm.bag.get(key, 0)
                if self_value >= min_freq_mult * other_value:
                    result[key] = {
                        "freq": self_value, "big_freq": other_value,
                        "ratio": self_value / (other_value or 1)
                    }

        return result

    def get_subset_bag(
            self,
            big_bag: "BagOfWords",
            max_freq: float = 1.,
            min_freq_mult: float = 2.,
    ):
        subset = self.get_subset(big_bag, max_freq=max_freq, min_freq_mult=min_freq_mult)
        bag = BagOfWords()
        bag.bag = {
            key: value["freq"]
            for key, value in subset.items()
        }
        return bag

    def get_subset_df(
            self,
            big_bag: "BagOfWords",
            max_freq: float = 1.,
            min_freq_mult: float = 2.,
    ):
        import pandas as pd

        subset = self.get_subset(big_bag, max_freq=max_freq, min_freq_mult=min_freq_mult)
        df = pd.DataFrame(subset).T
        if df.shape[0]:
            df.sort_values("ratio", ascending=False, inplace=True)
        return df

    def save_json(self, filename: Union[str, Path], sort: bool = True, indent: Optional[int] = 1):
        if sort:
            self.sort()
        Path(filename).write_text(
            json.dumps(self.bag, indent=indent)
        )

    @classmethod
    def load_json(cls, filename: Union[str, Path]) -> "BagOfWords":
        return BagOfWords(json.loads(Path(filename).read_text()))

    def dump(self, top: Optional[int] = None, file=None):
        if not self:
            return
        keys = sorted(self.bag, key=lambda k: self.bag[k], reverse=True)
        if top is not None:
            keys = keys[:top]

        max_len = max(len(k) for k in keys)
        count = self.count()
        for key in keys:
            print(f"{key:{max_len}}: {self.bag[key]:11,} {self.bag[key] / count:.5}", file=file)

    @classmethod
    def _iter_items(cls, param: WordBagArgument) -> Generator[Tuple[str, Number], None, None]:
        if isinstance(param, (str, list)):
            if isinstance(param, str):
                param = tokenize(param)
            for token in param:
                yield token, 1
        elif isinstance(param, dict):
            yield from param.items()
        elif isinstance(param, BagOfWords):
            yield from param.bag.items()
        else:
            raise TypeError(f"Unexpected type '{type(param).__name__}'")

    @classmethod
    def _as_dict(cls, param: WordBagArgument) -> Dict[str, Number]:
        if isinstance(param, (str, list)):
            return {key: value for key, value in cls._iter_items(param)}
        elif isinstance(param, dict):
            return param
        elif isinstance(param, BagOfWords):
            return param.bag
        else:
            raise TypeError(f"Unexpected type '{type(param).__name__}'")
