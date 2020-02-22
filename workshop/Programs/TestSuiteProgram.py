import unittest
from Programs import UnitTesting
from Programs import UnitTestForFirefox


class Test_Suite(unittest.TestCase):
    def test_main(self):
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(UnitTesting.ChromeLaunch),
            unittest.defaultTestLoader.loadTestsFromTestCase(UnitTestForFirefox.FirefoxLaunch),
        ])

        runner = unittest.TextTestRunner()
        runner.run(self.suite)


if __name__ == '__main__':
    unittest.main()
