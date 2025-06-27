# test suite
import unittest


class TestStringMethods(unittest.TestCase):
    
    # positive test function to test if 
    # values are almost equal with place
    def test_positiveForLess(self):
        first = 20
        second = 30
        
        # error message in case if test case got failed
        message = "first value is not less that second value."
        
        # assert function() to check if values1 is
        # less than value2
        self.assertLess(first, second, message)
        
        # positive test function to test if values
    # are almost equal with place
    def test_positiveForGreater(self):
        first = 4
        second = 3
        
        # error message in case if test case got failed
        message = "first value is not greater that second value."
        
        # assert function() to check if values1 is
        # greater than value2
        self.assertGreater(first, second, message)
        
    # negative test function to test if values1 is greater or equal than value2
    def test_negativeForGreaterEqual(self):
        first = 5
        second = 5
        
        # error message in case if test case got failed
        message = "first value is not greater or equal than second value."
        
        # assert function() to check if values1 is greater or equal than value2
        self.assertGreaterEqual(first, second, message)
        
     # positive test function to test if value1 is less or equal than value2
    def test_positiveForLessEqual(self):
        first = 4
        second = 4
        
        # error message in case if  test case got failed
        message = "first value is not less than or equal to second value."
        
        # assert function() to check if values1 is less or equal than value2
        self.assertLessEqual(first, second, message)
        
    # negative test function to test if values are almost not-equal with place
    def test_negativeWithPlaces(self):
        first = 4.4555
        second = 4.4556
        decimalPlace = 2
        # error message in case if test case got failed
        message = "first and second are almost equal."
        # assert function() to check if values are almost not-equal
        self.assertNotAlmostEqual(first, second, decimalPlace, message)

    # positive test function to test if values are almost not-equal with place
    def test_positiveWithPlaces(self):
        first = 4.4555
        second = 4.4556
        decimalPlace = 3
        # error message in case if test case got failed
        message = "first and second are almost equal."
        # assert function() to check if values are almost not-equal
        self.assertNotAlmostEqual(first, second, decimalPlace, message)

    # negative test function to test if values are almost not-equal with delta
    def test_negativeWithDelta(self):
        first = 4.4555
        second = 4.4555
        delta = 0.002
        # error message in case if test case got failed
        message = "first and second are almost equal."
        # assert function() to check if values are almost equal
        self.assertNotAlmostEqual(first, second, None, message, delta)

    # positive test function to test if values are almost not-equal with delta
    def test_positiveWithDelta(self):
        first = 4.4555
        second = 4.4556
        delta = 0.0001
        # error message in case if test case got failed
        message = "first and second are almost equal."
        # assert function() to check if values are almost not-equal
        self.assertNotAlmostEqual(first, second, None, message, delta)


# main for function call
if __name__ == '__main__':
    unittest.main()