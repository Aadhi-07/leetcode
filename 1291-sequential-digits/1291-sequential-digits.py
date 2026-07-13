class Solution(object):
    def sequentialDigits(self, low, high):
        res = []

        for start in range(1, 10):
            num = start
            next_digit = start + 1

            while next_digit <= 9:
                num = num * 10 + next_digit

                if low <= num <= high:
                    res.append(num)

                next_digit += 1

        return sorted(res)