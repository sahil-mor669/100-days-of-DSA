n = 5438 
num = n 
count = 0 
def count_digit(num,count):
    while num > 0:
        count += 1
        num = num // 10 
    return count  

print(count_digit(num , count ))   
