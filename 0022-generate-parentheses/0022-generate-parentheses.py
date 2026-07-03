class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def bt(cur, open_count, close_count):
            if len(cur) == 2 * n:
                res.append(cur)
                return

            if open_count < n:
                bt(cur + "(", open_count + 1, close_count)

            if close_count < open_count:
                bt(cur + ")", open_count, close_count + 1)

        bt("", 0, 0)
        return res