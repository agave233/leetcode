# 101

* ### Problem

  Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

  For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:

  ```
      1
     / \
    2   2
   / \ / \
  3  4 4  3

  ```

  But the following `[1,2,2,null,3,null,3]` is not:

  ```
      1
     / \
    2   2
     \   \
     3    3
  ```


* ### submit一次，%52.7

* ### 思路

  bfs问题。每个层次下依次保存节点值，然后利用python的list切片取逆序看看是否相等（回文问题）

  referrence给出了dfs的解法