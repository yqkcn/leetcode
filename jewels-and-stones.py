class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([i for i in stones if i in jewels])