# 746

* ### Problem

  On a staircase, the `i`-th step has some non-negative cost `cost[i]` assigned (0 indexed).

  Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

  **Example 1:**

  ```
  Input: cost = [10, 15, 20]
  Output: 15
  Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

  ```

  **Example 2:**

  ```
  Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
  Output: 6
  Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

  ```

  **Note:**

  1. `cost` will have a length in the range `[2, 1000]`.
  2. Every `cost[i]` will be an integer in the range `[0, 999]`.

* ### submit 3次，90%

* ### 思路

  使用DP时注意避免重复访问节点！！否则将是指数级别的复杂度。采用自底向上的动态规划，从数组的最后一个元素开始向前遍历，某一个节点的最短路可以分解为子问题，走一步或者走两步。所以每个状态下要保存两个元素，分别代表当前这个位置被走过或者没走过，然后最后返回的是两者的最小值。