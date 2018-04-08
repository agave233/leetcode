class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def collectNum(s):
            if s == 0:
                tmp1 = sorted([each for each in tmp])
                if tmp1 not in res:
                    res.append(tmp1)
            elif s > 0:
                for num in candidates:
                    if s < num:
                        return
                    tmp.append(num)
                    collectNum(s - num)
                    tmp.pop()
        
        
        tmp, res = [], []
        candidates.sort()
        collectNum(target)
        return res

# more concise
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [[[]]] + [[] for i in range(target)]
        for i in range(1, target + 1):
            for number in candidates:
                if number > i: 
                    break
                for L in dp[i - number]:
                    if not L or number >= L[-1]: 
                        dp[i] += L + [number],
        return dp[target]

# dfs
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resList = []
        candidates = sorted(candidates)
        self.dfs(candidates,[],target,0)
        return self.resList
    def dfs(self, candidates, sublist, target, last):
        if target == 0:
            self.resList.append(sublist[:])
        if target< candidates[0]:
            return 
        for n in candidates:
            if n > target:
                return
            if n < last:
                continue
            sublist.append(n)
            self.dfs(candidates,sublist,target - n, n)
            sublist.pop()