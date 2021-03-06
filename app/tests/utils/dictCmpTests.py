from modules.utils.dictUtil import DictUtil

__author__    = "Copyright (c) 2017, LEP>"
__copyright__ = "Licensed under GPLv2 or later."

import unittest


class DictCmpTests(unittest.TestCase):
        
    def test_two_flat_dicts_equal(self):

        dict_1 = {
            "project": "lepv"
        }

        dict_2 = {
            "project": "lepv"
        }

        comp_result = DictUtil.compare(dict_1, dict_2)
        self.assertEqual(comp_result, 0, 'The comparison result of two identical flat dicts should be 0')

    def test_two_empty_dicts_should_equal(self):
        
        dict_1 = {}
        dict_2 = {}

        comp_result = DictUtil.compare(dict_1, dict_2)
        self.assertEqual(comp_result, 0, 'The comparison result of two empty dicts should be 0')

    def test_empty_dict_being_contained(self):
        dict_1 = {
            "project": "lepv"
        }
        dict_2 = {}

        comp_result = DictUtil.compare(dict_1, dict_2)
        self.assertEqual(comp_result, 1, 'Empty dict should be considered "contained" by any non-empty dict')

    def test_two_null_dicts_should_equal(self):
        dict_1 = None
        dict_2 = None

        comp_result = DictUtil.compare(dict_1, dict_2)
        self.assertEqual(comp_result, 0, 'The comparison result of two null dicts should be 0')

    def test_two_flat_dicts_contains(self):
        
        dict_1 = {
            "project1": "lepv1",
            "project2": "lepv2",
            "project3": "lepv3"
        }
        
        dict_2 = {
            "project1": "lepv1",
            "project2": "lepv2"
        }

        comp_result = DictUtil.compare(dict_1, dict_2)
        self.assertEqual(comp_result, 1, 'If the first flat dict contains the second, the result should be 1')

    def test_two_deep_dicts_contains(self):

        dict_1 = {
            "project1": {"k1": "v1", "k2": "v2"},
            "project2": "lepv2"
        }

        dict_2 = {
            "project1": {"k1": "v1" },
            "project2": "lepv2"
        }

        comp_result = DictUtil.compare(dict_1, dict_2)
        self.assertEqual(comp_result, 1, 'If the first deep dict contains the second, the result should be 1')

    def test_two_deep_dicts_with_list_contains(self):

        dict_actual = {
            "data1": [
              {
                "Overhead": "45.17%",
                "Command": "uwsgi",
                "Shared Object": "libpython3.5m.so.1.0",
                "Symbol": "[.] 0x000000000011c525"
              },
              {
                "Overhead": "1.25%",
                "Command": "uwsgi",
                "Shared Object": "_socket.cpython-35m-x86_64-linux-gnu.so",
                "Symbol": "[.] 0x0000000000006b00"
              }
            ],
            "data2": "lepv"
        }

        dict_expected = {
            "data1": [
                {
                    "Overhead": "45.17%",
                    "Command": "uwsgi",
                    "Shared Object": "libpython3.5m.so.1.0",
                    "Symbol": "[.] 0x000000000011c525"
                }
            ],
        }

        comp_result = DictUtil.compare(dict_actual, dict_expected)
        self.assertEqual(comp_result, 1, 'If the first deep dict with list contains the second, the result should be 1')

    def test_two_flat_dicts_contained(self):
        
        dict_1 = {
            "project1": "lepv1",
            "project2": "lepv2"
        }

        dict_2 = {
            "project1": "lepv1",
            "project2": "lepv2",
            "project3": "lepv3"
        }

        comp_result = DictUtil.compare(dict_1, dict_2)
        self.assertEqual(comp_result, -1, 'If the second flat dict contains the first, the result should be -1')

    def test_two_deep_dicts_contained(self):
        
        dict_1 = {
            "project1": {"k1": "v1"},
            "project2": "lepv2"
        }

        dict_2 = {
            "project1": {"k1": "v1", "k2": "v2"},
            "project2": "lepv2"
        }

        comp_result = DictUtil.compare(dict_1, dict_2)
        self.assertEqual(comp_result, -1, 'If the second deep dict contains the first, the result should be -1')

    def test_two_deep_dicts_with_list_contained(self):

        dict_actual = {
            "data1": [
                {
                    "Overhead": "45.17%",
                    "Command": "uwsgi",
                    "Shared Object": "libpython3.5m.so.1.0",
                    "Symbol": "[.] 0x000000000011c525"
                }
            ],
        }

        dict_expected = {
            "data1": [
              {
                "Overhead": "45.17%",
                "Command": "uwsgi",
                "Shared Object": "libpython3.5m.so.1.0",
                "Symbol": "[.] 0x000000000011c525"
              },
              {
                "Overhead": "1.25%",
                "Command": "uwsgi",
                "Shared Object": "_socket.cpython-35m-x86_64-linux-gnu.so",
                "Symbol": "[.] 0x0000000000006b00"
              }
            ],
            "data2": "lepv"
        }

        comp_result = DictUtil.compare(dict_actual, dict_expected)
        self.assertEqual(comp_result, -1, 'If the second deep dict with list contains the first, the result should be -1')
    
    def test_two_flat_dicts_not_equal_not_contains_not_contained(self):

        dict_1 = {
            "project1": "lepv1",
            "project2": "lepv2"
        }

        dict_2 = {
            "project3": "lepv3",
            "project4": "lepv4"
        }

        comp_result = DictUtil.compare(dict_1, dict_2)
        self.assertEqual(comp_result, 2, 'If two flat dicts are no inclusion relationship, the result should be 2')    
        
    def test_two_deep_dicts_not_equal_not_contains_not_contained(self):

        dict_1 = {
            "project1": {"k1": "v1"},
            "project2": "lepv2"
        }

        dict_2 = {
            "project1": {"k1": "v2", "k2": "v1"},
            "project2": "lepv2"
        }

        comp_result = DictUtil.compare(dict_1, dict_2)
        self.assertEqual(comp_result, 2, 'If two deep dicts are no inclusion relationship, the result should be 2')    

    def test_two_deep_dicts_with_list_not_equal_not_contains_not_contained(self):
        
        dict_actual = {
            "data1": [
             {
                "Overhead": "45.17%",
                "Command": "uwsgi",
                "Shared Object": "libpython3.5m.so.1.0",
                "Symbol": "[.] 0x000000000011c525"
             },
            ],
            "data2": "lepv"
        }

        dict_expected = {
            "data1": [
             {
                "Overhead": "1.25%",
                "Command": "uwsgi",
                "Shared Object": "_socket.cpython-35m-x86_64-linux-gnu.so",
                "Symbol": "[.] 0x0000000000006b00"
             }
            ],
            "data2": "lepv"
        }

        comp_result = DictUtil.compare(dict_actual, dict_expected)
        self.assertEqual(comp_result, 2, 'If two deep dicts with list are no inclusion relationship, the result should be 2')    

if __name__ =='__main__':
    unittest.main()

