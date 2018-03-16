# 404

* ### Problem

  Find the sum of all left leaves in a given binary tree.

  **Example:**

  ```
      3
     / \
    9  20
      /  \
     15   7

  There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
  ```

* ### 两次submit，75.85%

* ### 思路

  求的是所有作为左子树的叶之和，所以在dfs递归遍历过程中要注意判定是否为一个“左叶”，即满足“左子树”和“叶节点”两个条件。所以要把父节点作为参数传入以判断是否左孩子。

  参考的代码是从每一个节点来判断其左孩子是否为叶节点，这样就不用传入其父节点了。