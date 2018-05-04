# 419 甲板上的战舰
# 给定一个二维的甲板， 请计算其中有多少艘战舰。 战舰用 'X'表示，空位用 '.'表示。 你需要遵守以下规则：

# 给你一个有效的甲板，仅由战舰或者空位组成。
# 战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列)组成，其中N可以是任意大小。
# 两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰。
# 示例 :

# X..X
# ...X
# ...X
# 在上面的甲板中有2艘战舰。

# 无效样例 :

# ...X
# XXXX
# ...X
# 你不会收到这样的无效甲板 - 因为战舰之间至少会有一个空位将它们分开。

# 进阶:

# 你可以用一次扫描算法，只使用O(1)额外空间，并且不修改甲板的值来解决这个问题吗？

# ---------------------------------------------------------------------------------
# Solution
# 采用一次遍历，并且只需要O(1)的空间，遍历时遇到一个'X'根据其左边和上边是否为'X'来判断是否count + 1
# ---------------------------------------------------------------------------------

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if board == [[]]:
            return 0
        m, n = len(board), len(board[0])
        count = 1 if board[0][0] == 'X' else 0
        
        for i in range(1, n):
            if board[0][i - 1] == '.' and board[0][i] == 'X':
                count += 1
            
        for i in range(1, m):
            count = count + 1 if board[i][0] == 'X' and board[i - 1][0] == '.' else count
            for j in range(1, n):
                if board[i][j] == 'X' and board[i - 1][j] == '.' and board[i][j - 1] == '.':
                    count += 1
        
        return count