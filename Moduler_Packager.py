import datetime, time, math, random, string, uuid, importlib


def date_time():
    print("\n1. Current Date & Time")
    print("2. Date Difference")
    print("3. Stopwatch")
    print("4. Countdown")

    c = input("Choice: ")

    if c == "1":
        print("Date & Time:", datetime.datetime.now())

    elif c == "2":
        a = datetime.datetime.strptime(
            input("First date (YYYY-MM-DD): "), "%Y-%m-%d")
        b = datetime.datetime.strptime(
            input("Second date (YYYY-MM-DD): "), "%Y-%m-%d")

        if a > b:
            a, b = b, a

        days = (b - a).days
        years = days // 365
        months = (days % 365) // 30
        days = (days % 365) % 30

        print("\nDifference:")
        print("Years :", years)
        print("Months:", months)
        print("Days  :", days)

    elif c == "3":
        input("Press Enter to start...")
        s = time.time()
        input("Press Enter to stop...")
        print("Time:", round(time.time() - s, 2), "seconds")

    elif c == "4":
        n = int(input("Seconds: "))
        while n:
            print(n)
            time.sleep(1)
            n -= 1
        print("Time Up!")


def math_menu():
    print("\n1. Factorial")
    print("2. Compound Interest")
    print("3. Trigonometry")
    print("4. Area")

    c = input("Choice: ")

    if c == "1":
        n = int(input("Number: "))
        print("Factorial:", math.factorial(n))

    elif c == "2":
        p = float(input("Principal: "))
        r = float(input("Rate: "))
        t = float(input("Time: "))
        amount = p * (1 + r / 100) ** t
        print("Amount:", round(amount, 2))

    elif c == "3":
        x = float(input("Angle: "))
        print("Sin:", round(math.sin(math.radians(x)), 4))
        print("Cos:", round(math.cos(math.radians(x)), 4))

    elif c == "4":
        r = float(input("Radius: "))
        print("Circle area:", round(math.pi * r * r, 2))


def random_menu():
    print("\n1. Number")
    print("2. List")
    print("3. Password")
    print("4. OTP")

    c = input("Choice: ")

    if c == "1":
        print("Random Number:", random.randint(1, 100))

    elif c == "2":
        n = int(input("Size: "))
        print([random.randint(1, 100) for i in range(n)])

    elif c == "3":
        n = int(input("Length: "))
        x = string.ascii_letters + string.digits + "@#$"
        print("Password:", ''.join(random.choice(x) for i in range(n)))

    elif c == "4":
        print("OTP:", random.randint(100000, 999999))


def files():
    print("\n1. Create")
    print("2. Write")
    print("3. Read")
    print("4. Append")

    c = input("Choice: ")
    name = input("File name: ")

    if c == "1":
        open(name, "w").close()
        print("File created")

    elif c == "2":
        with open(name, "w") as f:
            f.write(input("Data: "))
        print("File written")

    elif c == "3":
        try:
            with open(name) as f:
                print(f.read())
        except FileNotFoundError:
            print("File not found")

    elif c == "4":
        with open(name, "a") as f:
            f.write("\n" + input("Data: "))
        print("Data added")


def main():
    while True:
        print("""
========================
   MULTI UTILITY TOOL
========================
1. Date & Time
2. Mathematics
3. Random Data
4. UUID
5. File Operations
6. Explore Module
7. Exit
""")

        c = input("Enter choice: ")

        if c == "1":
            date_time()

        elif c == "2":
            math_menu()

        elif c == "3":
            random_menu()

        elif c == "4":
            print("UUID:", uuid.uuid4())

        elif c == "5":
            files()

        elif c == "6":
            try:
                m = importlib.import_module(input("Module name: "))
                print(dir(m))
            except ModuleNotFoundError:
                print("Module not found")

        elif c == "7":
            print("Thank you!")
            break

        else:
            print("Wrong choice")


if __name__ == "__main__":
    main()