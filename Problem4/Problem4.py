import math

class Runner:
    def IsPalindrome(self, num):
        """ Return true if number is palindromic """

        numStr = str(num)
        length = len(numStr)

        for i in range(0, math.floor(length / 2)):
            if numStr[i] != numStr[length - i - 1]:
                return False

        return True

    def Start(self):

        productMax = -1

        for i in range(100, 999):
            for k in range(100, 999):
                product = i*k
                if product > productMax and self.IsPalindrome(product):
                    productMax = product

        print("Result: {0}".format(productMax))

Runner().Start()
