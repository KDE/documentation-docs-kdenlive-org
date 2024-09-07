#!/usr/bin/env python3
"""
SPDX-FileCopyrightText: 2021 Julius Künzel <jk.kdedev@smartlab.uber.space>
"""
import os
import re
import unittest
from pathlib import Path

print("********* Start testing of redirects *********")

basepath: Path = Path(__file__).parent.parent


class TestRedirects(unittest.TestCase):

    outputBase = os.environ.get("TEST_HTML_OUTPUT", "build/html")
    outputPath = basepath / outputBase

    def test_redirect_exists(self):

        self.assertTrue(
            self.outputPath.is_dir(),
            f"The output dir {self.outputBase} does not exist. Make sure the test runs after the build step",
        )

        lines = (basepath / "404handler.php").read_text()

        x = re.search(r"\$redirect_rules = array\(([\s\S]*?)\);", lines)

        self.assertTrue(x)

        y = re.findall(r"\"(.*?)\"\s*?=>\s*?\"(.*?\.html).*\"", x.group(1))

        for redirect, target in y:
            tartgetFile = self.outputPath / target

            self.assertTrue(
                tartgetFile.is_file(),
                f"The target {target!r} for redirect {redirect!r} does not exist",
            )


if __name__ == "__main__":
    unittest.main()
