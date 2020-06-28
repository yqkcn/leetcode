class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        for char in ["--", "++", "-+", "+-", "..", ".+", ".-"]:
            if char in s:
                return False
        _s = s.replace("e", "").replace("-", "").replace("+", "").replace(".", "")
        if not _s.isdigit():
            return False
        if "e" not in s:
            s = s.lstrip("+")
            print(s)
            try:
                float(s)
                return True
            except Exception:
                return False
        if s.count("e") > 1:
            return False
        nums = list(filter(None, s.split("e")))
        if len(nums) != 2:
            return False
        first, second = nums
        first = first.lstrip("+")
        second = second.lstrip("+")
        if "." in second:
            return False
        try:
            float(first)
            int(second)
        except Exception:
            return False
        return True


if __name__ == '__main__':
    test_cases = [
        ("0", True),
        (" 0.1 ", True),
        ("abc", False),
        ("1 a", False),
        ("2e10", True),
        (" -90e3", True),
        (" 1e", False),
        ("e3", False),
        (" 6e-1", True),
        (" 99e2.5", False),
        ("53.5e93", True),
        (" --6", False),
        ("-=3", False),
        ("95a54e53", False),
        (".1", True),
        ("1.", True),
        (". 1", False),
        ("4e+", False),
        ("+.8", True),
        ("e.7e5", False),
    ]
    s = Solution()
    for case, expected in test_cases[-1:]:
        print(case)
        assert s.isNumber(case) == expected