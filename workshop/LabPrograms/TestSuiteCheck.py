import unittest
import LoginPageValidation
import CountElementsInWeb


# two test cases are run together
class Test_Suite(unittest.TestCase):
    def test_main(self):
        self.suite = unittest.TestSuite()
        self.suite.addTests([unittest.TestLoader().loadTestsFromModule(LoginPageValidation),
                             unittest.TestLoader().loadTestsFromModule(CountElementsInWeb)])

        runner = unittest.TextTestRunner()
        runner.run(self.suite)


if __name__ == "__main__":
    unittest.main()
