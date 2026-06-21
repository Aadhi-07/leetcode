class Solution(object):
    def maxIceCream(self, costs, coins):
        m = max(costs)
        cnt = [0] * (m + 1)

        for c in costs:
            cnt[c] += 1

        ans = 0

        for price in range(1, m + 1):
            if cnt[price] == 0:
                continue

            can = min(cnt[price], coins // price)
            ans += can
            coins -= can * price

            if coins < price:
                break

        return ans