# Number to Words Converter
ones = ["","one","two","three","four","five","six","seven","eight","nine","ten",
        "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def to_words(n):
    if n < 20: return ones[n]
    if n < 100: return tens[n//10] + ("-" + ones[n%10] if n%10 else "")
    if n < 1000: return ones[n//100] + " hundred" + (" and " + to_words(n%100) if n%100 else "")
    return to_words(n//1000) + " thousand" + (" " + to_words(n%1000) if n%1000 else "")

num = int(input("Enter number (0-999999): "))
print(f"{num} = {to_words(num) if num else 'zero'}")
