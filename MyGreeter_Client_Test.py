import unittest
import MyGreeter

class MyGreeter_Client_Test(unittest.TestCase):
    def setUp(self):
        self.greeter = MyGreeter.Client()
        
  
    def test_Instance(self):
        self.assertTrue(isinstance(self.greeter, MyGreeter.Client))
        
     
    def test_getGreeting(self):
        self.assertTrue(len(self.greeter.getGreeting()) > 0)
        

if __name__ == '__main__':
    unittest.main()