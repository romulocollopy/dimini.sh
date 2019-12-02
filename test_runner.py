#! /usr/bin/env python

import unittest

import tests

suite = unittest.TestLoader().loadTestsFromModule(tests)

if __name__ == "__main__":
    unittest.TextTestRunner().run(suite)
