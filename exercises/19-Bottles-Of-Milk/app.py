# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for bottles in range(99, 0, -1):
        if bottles > 1:
            print(f"{bottles} bottles of milk on the wall, {bottles} bottles of milk. Take one down and pass it around, {bottles - 1} {'bottles' if bottles - 1 > 1 else 'bottle'} of milk on the wall.")
        else: 
            print(f"{bottles} bottle of milk on the wall, {bottles} bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
    print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")

number_of_bottles()