import unittest


class TestCase(unittest.TestCase):
    def test_omit(self):
        from xuse.mcore._dict import omit

        source = {"x": 1, "y": 2}
        self.assertEqual(omit(source, ["x"]), {"y": 2})


if __name__ == "__main__":
    unittest.main()
