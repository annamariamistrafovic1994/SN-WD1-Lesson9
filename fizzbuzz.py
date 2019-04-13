print("This is a game called 'FizzBuzz'! ")

end = input("Pleease enter a number between 1 and 100: ")
end = int(end)  #convert string into number

for num in range(1, end+1):
    if num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    else:
        print("num")





