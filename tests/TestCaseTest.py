if __name__ == '__main__':
    import sys
    from os import path
    sys.path.append(path.join(path.dirname(__file__), '..'))
    from Pyst import TestCase, WasRun

class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun('testMethod')
        
    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)


TestCaseTest('testSetUp').run()
TestCaseTest('testRunning').run()

