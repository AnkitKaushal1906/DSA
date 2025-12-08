class Solution(object):
    def concatHex36(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Step 1: compute n² and n³
        n2 = n * n
        n3 = n2 * n

        # Step 2: convert n² to hexadecimal (uppercase)
        hex_str = format(n2, 'X')

        # Step 3: convert n³ to base-36 (uppercase)
        base36_str = self.to_base36(n3)

        # Step 4: return concatenation
        return hex_str + base36_str

    def to_base36(self, num):
        if num == 0:
            return "0"

        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while num > 0:
            num, rem = divmod(num, 36)
            result = digits[rem] + result

        return result
