#!/usr/bin/env python3
"""
SPDX-FileCopyrightText: 2021 Julius Künzel <jk.kdedev@smartlab.uber.space>
"""
import os
import unittest

print("********* Start testing of file names *********")

SRC_DIR: str = "./"

class TestFilenames(unittest.TestCase):

    def test_blankInFilename(self):
        self.maxDiff = None
        for dirpath, dirnames, filenames in os.walk(SRC_DIR):
            for f in filenames:

                # Filter out files
                if not f.endswith('.rst'):
                    continue

                self.assertNotIn(' ', f)

                pass

    def test_bracketsInFilename(self):
        self.maxDiff = None
        for dirpath, dirnames, filenames in os.walk(SRC_DIR):
            for f in filenames:

                # Filter out files
                if not f.endswith('.rst'):
                    continue

                self.assertNotIn('(', f)
                self.assertNotIn(')', f)

                pass


if __name__ == "__main__":
    unittest.main()

