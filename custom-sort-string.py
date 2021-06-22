class Solution:
    def customSortString(self, order: str, str: str) -> str:
        def sort_key(x):
            if x in order:
                return order.index(x)
            return 200

        return "".join(sorted(str, key=sort_key))
