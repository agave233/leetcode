# 538

- ### Problem

  Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

  **Example:**

  ```
  Input: The root of a Binary Search Tree like this:
                5
              /   \
             2     13

  Output: The root of a Greater Tree like this:
               18
              /   \
            20     13
  ```

- ### 三次submit，56.40%

- ### 思路

  这是一个顺序搜索树的问题，很明显是先访问右子树再访问左子树的顺序，并且把右子树的节点之和返回到父节点累加，同时父节点和右子树的节点之和又要传递给左子树累加，如此递归。

  参考代码，在`_init_`方法定义了一个类变量统计该向下传递（给左子树）的累加值，可以提高代码效率。