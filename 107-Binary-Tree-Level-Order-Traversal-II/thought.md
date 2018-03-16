# 107

* ### Problem

  Given a binary tree, return the *bottom-up level order* traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

  For example:
  Given binary tree `[3,9,20,null,null,15,7]`,

  ```
      3
     / \
    9  20
      /  \
     15   7

  ```

  return its bottom-up level order traversal as:

  ```
  [
    [15,7],
    [9,20],
    [3]
  ]
  ```


* ###一次submit，92.96%

* ###思路

  题意要求是输出每一层的节点，所以用bfs遍历搜索，用一个list表示队列，每一次循环都遍历队列中所有的节点，并把每个节点的左右孩子加入到队列进行下一轮遍历。

  需要注意的有两点：

  - 加入到新的列表时要注意筛选非空的左右节点
  - 要对list逆序返回，并pop出第一个元素（为空）