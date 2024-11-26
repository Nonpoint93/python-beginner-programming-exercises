def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for i in range(100):
        i+=1
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            if i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

        

# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
