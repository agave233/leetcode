# 108

* ### Problem

  Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

  For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of *every* node never differ by more than 1.

  **Example:**

  ```
  Given the sorted array: [-10,-3,0,5,9],

  One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

        0
       / \
     -3   9
     /   /
   -10  5
  ```

* ### 一次submit，79.33%

* ### 思路

  把一个已排序的数组转换为一个BST，且要求平衡，所以递归建树的过程中每次选取当前传入数组的中值作为该节点的值，然后递归建立左子树和右子树，分别把分割成的两个两个数组传入