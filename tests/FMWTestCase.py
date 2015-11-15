import unittest
import ../toolbox/apis.html

class FeedMeTestCase(unittest.TestCase):
    def test_getDishes():
        assertEqual(getDishes("American"),"Cheeseburger","Error in getDishes Cheesebureger:"+str(getDishes("American")))

    def test_getCalories()
        assertEqual(getCalories("Cheeseburger"),345,"Error in getCalories 345:"+str(getCalories("Cheeseburger")))		
