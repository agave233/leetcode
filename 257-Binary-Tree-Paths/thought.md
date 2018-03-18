# 257

* ### Problem

  Given a binary tree, return all root-to-leaf paths.

  For example, given the following binary tree:

  ```
     1
   /   \
  2     3
   \
    5

  ```

  All root-to-leaf paths are:

  ```
  ["1->2->5", "1->3"]
  ```

* ### submit一次，50%

* ### 思路

  dfs遍历问题，如果某个节点的左右孩子全为空时，那么该节点为叶子节点，所以此时产生一条路径，存放到结果list中。递归访问左右子树时，将当前的节点加入到路径向下传递。