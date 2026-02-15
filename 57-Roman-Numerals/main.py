# Roman Numeral Converter
def to_roman(num):
    vals = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),
            (50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    result = ""
    for val, sym in vals:
        while num >= val:
            result += sym
            num -= val
    return result

num = int(input("Enter a number (1-3999): "))
if 1 <= num <= 3999:
    print(f"{num} = {to_roman(num)}")
else:
    print("Number must be between 1 and 3999")
