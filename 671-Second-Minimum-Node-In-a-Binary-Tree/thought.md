# 671

* ### Problem

  Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly `two` or `zero` sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

  Given such a binary tree, you need to output the **second minimum** value in the set made of all the nodes' value in the whole tree.

  If no such second minimum value exists, output -1 instead.

  **Example 1:**

  ```
  Input: 
      2
     / \
    2   5
       / \
      5   7

  Output: 5
  Explanation: The smallest value is 2, the second smallest value is 5.

  ```

  **Example 2:**

  ```
  Input: 
      2
     / \
    2   2

  Output: -1
  Explanation: The smallest value is 2, but there isn't any second smallest value.

  ```

* ###submit一次，37.01%

* ###思路

  这个题的关键在于要利用给定树的特性，从而避免遍历一些不必要搜索的路径。

  * 搜索路径筛选

    如果该节点的一个孩子比当前节点大（而不是相等），那么该节点的值必定为第二小节点的候选

  * ​

    当在某个节点时，左右子树返回的都是其第二小的节点（如果有的话），所以从该节点向上返回的时候有两种可能：

    * 左右子树返回的值均与父节点不同（大于父节点），那么返回两者的较小者
    * 如果至少有一个节点与父节点相同（那么该节点之下必定全是这个树的最小值），所以应当返回不相同的节点值，即返回两者的较大者