
# 初始位置 (0, 0) 处有一个机器人。给出它的一系列动作，判断这个机器人的移动路线是否形成一个圆圈，换言之就是判断它是否会移回到原来的位置。

# 移动顺序由一个字符串表示。每一个动作都是由一个字符来表示的。机器人有效的动作有 R（右），L（左），U（上）和 D（下）。输出应为 true 或 false，表示机器人移动路线是否成圈。

# 示例 1:

# 输入: "UD"
# 输出: true
# 示例 2:

# 输入: "LL"
# 输出: false

# ---------------------------------------------------------------
# solution
# 直接计数，判断左右的移动次数相等且上下移动的次数相等
# ---------------------------------------------------------------

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # h, v = 0, 0
        # for move in moves:
        #     h = h + 1 if move == 'R' else h - 1 if move == 'L' else h
        #     v = v + 1 if move == 'U' else v - 1 if move == 'D' else v
        # return True if v == 0 and h == 0 else False
        return True if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R') else False
