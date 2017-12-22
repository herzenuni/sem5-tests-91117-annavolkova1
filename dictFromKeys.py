list1 = list('123456')
list2 = list('abcd')


def dictionaryFromKeys(k, v):
    try:
        res = dict.fromkeys(k, None)
        res.update(zip(k, v))
    except TypeError:
        res = 'TypeError'
    return res


result = dictionaryFromKeys(list1, list2)
print(result)


def test_normal_values(self):
    self.assertEqual(dictionaryFromKeys([1, 2, 3, 4], [2, 3, 4, 5]), {1: 2, 2: 3, 3: 4, 4: 5})
    self.assertEqual(dictionaryFromKeys([6, 7, 8, 9, 10], [1, 2, 3, 4]), {6: 1, 7: 2, 8: 3, 9: 4, 10: None})


def test_vals_float_type(self):
    self.assertTrue(dictionaryFromKeys(3, 4) is None)
    self.assertTrue(dictionaryFromKeys(5, [6]) is None)


def test_vals_bool_type(self):
    self.assertIsNone(dictionaryFromKeys(True, True), None)


def test_negative_values(self):
    self.assertEqual(dictionaryFromKeys(-1, -2), None)
    self.assertEqual(dictionaryFromKeys(-3, -4), None)