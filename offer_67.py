class Solution:
    def strToInt(self, str: str) -> int:
        """
        :type str: str
        :rtype: int
        """
        s = str.lstrip()
        try:
            result =  int(re.match("^[-+]?[0-9]\d*",s).group())
            if result >  2147483647 : return 2147483647
            if result < -2147483648 : return -2147483648
            return result
        except:
            return 0
