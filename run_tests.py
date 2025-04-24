#!/usr/bin/env python3
"""
Run tests for Space Adventure game with custom output formatting.
"""
import sys
import os
import unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tests.test_game import TestSpaceAdventure, CustomTestRunner

if __name__ == "__main__":
    # Create the test suite with all tests from TestSpaceAdventure
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestSpaceAdventure)
    
    # Run the tests with our custom runner
    runner = CustomTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Return appropriate exit code
    sys.exit(not result.wasSuccessful())
