# 198

* ### Problem

  You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

  Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

* ### submit一次，72%

* ### 思路

  跟前几道动态规划问题一样，每一轮需要保存两个状态，需要特别注意不能相邻。