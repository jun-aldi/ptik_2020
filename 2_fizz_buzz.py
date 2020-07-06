def fizz_buzz(num):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num %3==0:
        print ("Fizz")
    elif num %5==0:
        print ("Buzz")
    else:
        print(str(num))


fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(4)