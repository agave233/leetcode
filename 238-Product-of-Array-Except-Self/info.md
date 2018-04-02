# 238

* 问题

  Given an array of *n* integers where *n* > 1, `nums`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

  Solve it **without division** and in O(*n*).

  For example, given `[1,2,3,4]`, return `[24,12,8,6]`.

  **Follow up:**
  Could you solve it with constant space complexity? (Note: The output array **does not** count as extra space for the purpose of space complexity analysis.)

* 解决

  要考虑三种情况：

  * 数组中没有0

    直接求出总的乘积，然后output中每个元素就是总乘积除以当前元素值

  * 数组中有一个0

    除了为0的位置是其他位置的乘积，output其他位置都是0

  * 数组中有大于一个0

    output中必定全为0

  ​