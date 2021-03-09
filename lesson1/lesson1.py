a = int(input("Enter integer: "))

if a % 15 == 0:
    print("Ping Pong")
elif a % 5 == 0:
    print("Pong")
elif a % 3 == 0:
    print("Ping")
else:
    print("Bad number")

print("Finish")
