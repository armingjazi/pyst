class TestCase:

    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass
    
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):

    def __init__(self, name):
        self.wasSetUp = False
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = False
        self.wasSetUp = True

    def testMethod(self):
        self.setUp()
        self.wasRun = True

