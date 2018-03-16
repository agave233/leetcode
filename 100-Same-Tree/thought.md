# 100

- ### Problem

  Given two binary trees, write a function to check if they are the same or not.

  Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

  **Example 1:**

  ```
  Input:     1         1
            / \       / \
           2   3     2   3

          [1,2,3],   [1,2,3]

  Output: true

  ```

  **Example 2:**

  ```
  Input:     1         1
            /           \
           2             2

          [1,2],     [1,null,2]

  Output: false

  ```

  **Example 3:**

  ```
  Input:     1         1
            / \       / \
           2   1     1   2

          [1,2,1],   [1,1,2]

  Output: false
  ```

- ### 一次submit，59.40%

- ### 思路

  判断两个树是否相同，那么就是一个很基本的遍历问题，只是增加了对当前节点是否相等的判断，注意为空节点时。