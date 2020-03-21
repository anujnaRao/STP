import unittest
import loginUnitTestWithClass
import countingInputTypes


# two test cases are run together
class Test_Suite(unittest.TestCase):
    def test_main(self):
        self.suite = unittest.TestSuite()
        self.suite.addTests([unittest.TestLoader().loadTestsFromModule(loginUnitTestWithClass),
                             unittest.TestLoader().loadTestsFromModule(countingInputTypes)])

        runner = unittest.TextTestRunner()
        runner.run(self.suite)


if __name__ == "__main__":
    unittest.main()
