# FIZZ BUZZ   if divisible by 3 FIZZ, if divisible by 5 BUZZ, and by 15 FIZZBUZZ

def fizz_buzz(x):
    if x %3 == 0 and x %5 ==0:
       return "FIZZBUZZ"
    if x %3 == 0:
        return "FIZZ"
    if x %5 == 0:
        return "BUZZ"
    else:
        return x
print(fizz_buzz(75))
