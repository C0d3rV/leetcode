class Solution:
    def romanToInt(self, s: str) -> int:
        manual = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        value = 0
        prev_value = 0
        for i in s[::-1]:
            current_value = manual[i]

            if current_value < prev_value:
                value-=current_value
            else:
                value+=current_value
            prev_value = current_value
        return value

        