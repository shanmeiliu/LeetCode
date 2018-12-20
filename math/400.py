class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        1 digit: 1-9, total: 9, number of chr: 1*9
        2 digits: 10-99, total: 90, number of chr: 2*(90)
        3 digits: 100-999, total: 900, number of chr: 3*(900)
        ...
        ...
        n digits: 10^(n-1)-(10^n-1), total: 9 * 10^(n-1), number of chr: n*(9*10^(n-1))
        """
        num = n
        count = 0 # number of digits of val
        base = 0
        while (num >0):
            num = num - (count+1)*9*(10**count)
            print(num)
            base = 10**count-1
            count = count +1
            
            
        print(count)    
        num = num + count*9*10**(count - 1)
        print(num)
        print(base)
        val = base + (num//count)
        print(val)
        rem = num%count
        print(rem)
        if rem == 0:
            return int(str(val)[-1])
        else:
            return int(str(val+1)[rem-1])
