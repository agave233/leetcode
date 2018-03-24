# 41

* ### Problem

  Given an unsorted integer array, find the first missing positive integer.

  For example,
  Given `[1,2,0]` return `3`,
  and `[3,4,-1,1]` return `2`.

  Your algorithm should run in *O*(*n*) time and uses constant space.

* ### submit 三次，76%

* ### 思路

  找到数组里第一个miss的整数，如果用hash表进行标记的话用O(n)的时间复杂度和空间复杂度就可以完成，用O(1)的空间的话就要考虑miss一个整数到底会发生什么？先假设没有丢失的整数，那么一个数组必然是1~n存在其中，所以思路就是把i放到第i个位置上，这样不断进行交换，每一个i的归位最多交换两次就可以完成。

  需要注意的是，考虑可能存在数组元素重复和越界的情况。如果检测到一个数是重复的，直接把其中一个设为-1（相当于删除），越界的话，也是剔除，需要注意首先append原list一下