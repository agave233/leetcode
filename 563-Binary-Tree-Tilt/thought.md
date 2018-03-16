# 563

* ### Problem

  Given a binary tree, return the tilt of the **whole tree**.

  The tilt of a **tree node** is defined as the **absolute difference** between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

  The tilt of the **whole tree** is defined as the sum of all nodes' tilt.

  **Example:**

  ```
  Input: 
           1
         /   \
        2     3
  Output: 1
  Explanation: 
  Tilt of node 2 : 0
  Tilt of node 3 : 0
  Tilt of node 1 : |2-3| = 1
  Tilt of binary tree : 0 + 0 + 1 = 1

  ```

  **Note:**

  1. The sum of node values in any subtree won't exceed the range of 32-bit integer.
  2. All the tilt values won't exceed the range of 32-bit integer.

* ### 一次submit，51.63%

* ### 思路

  求每一个节点的左子树所有节点值的和、右子树所有节点值的和，并且计算其差值的绝对值，所以递归访问树的过程，向上传递一个`tuple`，即'Tilt'和当前子树取值的和组成的元组