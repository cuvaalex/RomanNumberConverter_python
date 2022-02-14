class RomanNumber:
    specialRomanNumber = {90: "XC", 50: "L", 40: "XL"}

    def parse(self, n):
        roman = ""
        pad = n

        if pad > 99:
            numbers_of_100 = pad // 100
            roman = roman.ljust(len(roman) + numbers_of_100, "C")
            pad -= 100 * numbers_of_100

        for key in sorted(self.specialRomanNumber.keys()
                , key=lambda x: x
                , reverse=True):
            if pad > (key - 1):
                roman += self.specialRomanNumber[key]
                pad -= key

        if pad > 9:
            number_of_10 = pad // 10
            roman = roman.ljust(len(roman) + number_of_10, "X")
            pad -= 10 * number_of_10

        if pad == 9:
            roman += "IX"
            return roman

        if pad > 4:
            roman += "V"
            pad -= 5

        if pad == 4:
            roman += "IV"
            return roman

        if pad > 0:
            return roman.ljust(len(roman) + pad, "I")

        return roman
