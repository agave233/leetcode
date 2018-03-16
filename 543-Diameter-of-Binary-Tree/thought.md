# 543

- ### Problem

  Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the **longest**path between any two nodes in a tree. This path may or may not pass through the root.

  **Example:**
  Given a binary tree 

  ```
            1
           / \
          2   3
         / \     
        4   5    

  ```

  Return **3**, which is the length of the path [4,2,1,3] or [5,2,1,3].

  **Note:** The length of path between two nodes is represented by the number of edges between them.

- ###2次submit，53.85%

- ###思路

  转化为求深度问题，并且要求每一个节点作为根节点的子树的深度，求得每一个节点对应子树的深度后，其“路径长度”即为左右深度之和，并且在递归的过程中每次要取当前求得路径和最长路径的最大值作为最大值。