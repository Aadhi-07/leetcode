class Solution:
    def countSequences(self, nums, k):
        def g(a, b):
            while b:
                a, b = b, a % b
            return a
        
        dp = {(1, 1): 1}
        
        for x in nums:
            nd = {}
            for (a, b), c in dp.items():
                nd[(a, b)] = nd.get((a, b), 0) + c
                
                na, nb = a * x, b
                d = g(na, nb)
                p = (na // d, nb // d)
                nd[p] = nd.get(p, 0) + c
                
                na, nb = a, b * x
                d = g(na, nb)
                p = (na // d, nb // d)
                nd[p] = nd.get(p, 0) + c
                
            dp = nd
        
        return dp.get((k, 1), 0)