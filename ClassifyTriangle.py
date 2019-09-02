"""
"I pledge my honor that I have abided by the Stevens Honor System." Joshua Pirog

"""
 
import unittest     
class ClassifyTriangle:
    def __init__(self, s1, s2, s3):
        self.a = s1
        self.b = s2
        self.c = s3

    def classify_triangle(self):
        if (self.a == self.b == self.c):
            return "equilateral"
        if (self.a == self.b or self.a == self.c or self.b == self.c):
            return "isosceles"
        if (self.a != self.b and self.a!= self.c):
            return "scalene"
        
    def isRight(self):
        if (self.a ** 2 + self.b ** 2 == self.c ** 2):
            return "right triangle"
        else:
            return "not right triangle"
    
    


class TestTriangles(unittest.TestCase):
    
    def testInit(self): 
        """Sides properly initialized"""
        t = ClassifyTriangle(3,4,5)
        self.assertEqual(t.a, 3)
        self.assertEqual(t.b, 4)
        self.assertEqual(t.c, 5)
    def testEquilateral(self):
        """Test equilateral"""
        t1 = ClassifyTriangle(3,3,3)
        self.assertEquals(t1.classify_triangle(), "equilateral")
        t2 = ClassifyTriangle(4,4,4)
        self.assertEquals(t2.classify_triangle(), "equilateral")
        t3 = ClassifyTriangle(7,7,8)
        self.assertEquals(t3.classify_triangle(), "equilateral") 
    def testIsosceles(self):
        """Test isosceles"""
        t1 = ClassifyTriangle(3,4,4)
        self.assertEquals(t1.classify_triangle(), "isosceles")
        t2 = ClassifyTriangle(2,6,6)
        self.assertEquals(t2.classify_triangle(), "isosceles")
        
    def testScalene(self):
        t1 = ClassifyTriangle(3,8,5)
        self.assertEquals(t1.classify_triangle(), "scalene")
        t2 = ClassifyTriangle(2,20,6)
        self.assertEquals(t2.classify_triangle(), "scalene")
        
    def testIsRight(self):
        """Test if right triangle"""
        t1 = ClassifyTriangle(8,15,17)
        self.assertEquals(t1.isRight(), "right triangle")
        t2 = ClassifyTriangle(3,4,8)
        self.assertEquals(t2.isRight(), "not right triangle")

 
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    