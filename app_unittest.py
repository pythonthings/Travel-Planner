import unittest
import app

# Note: the class must be called Test
class Test(unittest.TestCase):
  def test_if_it_runs_to_the_end(self):
    #self.assertEqual(app.testing_address(["California", "Nevada", "Illinois", "New York", "Maine"],["Nevada", "Illinois", "New York", "Maine"]), True)
    #self.assertEqual(app.testing_address(['Seattle', 'Chicago', 'Anaheim', 'Miami'], ['Chicago', 'Anaheim', 'Miami']), True)
    # self.assertEqual(app.testing_address(['San diego', 'Anaheim', 'Costa Mesa', 'Seattle'], ['Anaheim', 'Costa Mesa', 'Seattle']), True)
    # self.assertEqual(app.testing_address(['Anaheim', 'Buena Park', 'Cypress', 'Fullerton'], ['Buena Park', 'Cypress', 'Fullerton']), True)
    # self.assertEqual(app.testing_address(["California", "Nevada", "Illinois", "New York", "Washington", "Maine"], ["Nevada", "Illinois", "New York", "Washington", "Maine"]), True) #bad apple
    self.assertEqual(app.testing_address(["California", "Montana", "Wyoming", "Idaho", "Texas", "Florida", "Maine"], ["Montana", "Wyoming", "Idaho", "Texas", "Florida", "Maine"]), True)

if __name__ == '__main__':
    unittest.main()
