def findDigits(n):
     print(sum([1 for i in str(n).replace('0', '') if n % int(i) == 0]))
findDigits(12)