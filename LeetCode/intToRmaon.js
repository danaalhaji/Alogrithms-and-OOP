var intToRoman = function (num, rom = "") {
    if ((num / 1000) >= 1) return intToRoman(num - 1000, rom + 'M')
    else if (num / 100 >= 9) return intToRoman(num - 900, rom + 'CM')
    else if (num / 100 >= 5) return intToRoman(num - 500, rom + 'D')
    else if (num / 100 >= 4) return intToRoman(num - 400, rom + 'CD')
    else if (num / 100 >= 1) return intToRoman(num - 100, rom + 'C')
    else if (num / 10 >= 9) return intToRoman(num - 90, rom + 'XC')
    else if (num / 10 >= 5) return intToRoman(num - 50, rom + 'L')
    else if (num / 10 >= 4) return intToRoman(num - 40, rom + 'XL')
    else if (num / 10 >= 1) return intToRoman(num - 10, rom + 'X')
    else if (num / 1 >= 9) return intToRoman(num - 9, rom + 'IX')
    else if (num / 1 >= 5) return intToRoman(num - 5, rom + 'V')
    else if (num / 1 >= 4) return intToRoman(num - 4, rom + 'IV')
    else if (num / 1 >= 1) return intToRoman(num - 1, rom + 'I')
    else return rom
};