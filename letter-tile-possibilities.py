class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        def dfs(cur: str, letters: list):
            res.add(cur)
            if not letters:
                return
            for i, letter in enumerate(letters):
                dfs(cur + letter, letters[:i] + letters[i + 1:])

        dfs("", list(tiles))
        return len(res) - 1
