class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        L = {1 : 'I',4 : 'IV',5 : 'V',9 : 'IX',10 : 'X',40 : 'XL',50 : 'L',90 : 'XC',100 : 'C',400 : 'CD',500 :'D',900 :'CM',1000 : 'M'}
        k = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        a = num
        s = ''
        while a>0:
            u = sorted(([a]+k), reverse = True)
#             print(u)
            n = u[u.index(a)+1]
            s += L[n]
            a -= n
        return s