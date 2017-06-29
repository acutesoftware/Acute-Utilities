#!/usr/bin/python3
# coding: utf-8
# test_diary.py

import unittest
import sys
import os
root_fldr = os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(__file__))), "..", "src", "diary" )
print('root_fldr = ' , root_fldr)

sys.path.append(root_fldr)

import diary_utils



class DiaryUtilsTest(unittest.TestCase):
    def test_01_str(self):
        self.assertEqual(1, 1)

 
if __name__ == '__main__':
    unittest.main()