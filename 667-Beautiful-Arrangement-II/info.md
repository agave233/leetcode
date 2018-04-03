# 667

* 问题

  Given two integers `n` and `k`, you need to construct a list which contains `n` different positive integers ranging from `1` to `n` and obeys the following requirement: 
  Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly `k` distinct integers.

  If there are multiple answers, print any of them.

  **Example 1:**

  ```
  Input: n = 3, k = 1
  Output: [1, 2, 3]
  Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.

  ```

  **Example 2:**

  ```
  Input: n = 3, k = 2
  Output: [1, 3, 2]
  Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.

  ```

  **Note:**

  1. The `n` and `k` are in the range 1 <= k < n <= 104.

* 解决

  对于一个1~n的数组，按照相邻元素差递减的顺序可以生成满足题意的输出结果。即在list中首先放1，然后放n（差为n-1），同理为了下一个数与n差为n-2，这个数应该是2。。。按照这样的思路即可生成k-1个不同差值。后面把未放置得元素顺序放入即可（差值为1）