class Solution(object):
    def fizzBuzz(self, m):
        n = []
        for x in range(1, m + 1):
            if x % 3 == 0 and x % 5 == 0:
                n.append("FizzBuzz")
            elif x % 3 == 0:
                n.append("Fizz")
            elif x % 5 == 0:
                n.append("Buzz")
            else:
                n.append(str(x))
        return n
