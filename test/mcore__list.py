import unittest
from random import choice


def get_olist():

    arr = []
    ks = ("x", "y", "z")
    for i in range(100):
        arr.append({k: choice(list(range(10))) for k in ks})
    return arr


class TestCase(unittest.TestCase):
    def test__sort_recursive(self):
        from xuse.mcore._list import sort_recursive

        arr = get_olist()
        # 必须传入 key 函数，格式为 key, key1, ...
        self.assertRaises(ValueError, lambda: sort_recursive(arr))
        self.assertRaises(ValueError, lambda: sort_recursive(arr, key_0=lambda o: o))

        for i in sort_recursive(
            arr,
            key1=lambda d: d["x"],
            key2=lambda d: d["y"],
            key99=lambda d: d["z"],
            key99_reverse=True,
        ):

            print(i)


if __name__ == "__main__":
    unittest.main()
