while True:

    print('''
1. Register
2. Login
3. View Users
4. Exit
''')

    choice = int(input("Enter Choice: "))

    match choice:

        case 1:
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            f = open("users.txt", "a")
            f.write(username + "," + password + "\n")
            f.close()

            print("Registration Successful")

        case 2:
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            f = open("users.txt", "r")

            lines = f.readlines()

            found = False

            for line in lines:

                line = line.strip()

                stored_u, stored_p = line.split(",")

                if stored_u == username and stored_p == password:
                    print("Login Successful")
                    found = True
                    break

            if not found:
                print("Invalid Credentials")

            f.close()

        case 3:

            f = open("users.txt", "r")

            lines = f.readlines()

            print("\nRegistered Users:\n")

            count = 1

            for line in lines:

                line = line.strip()

                stored_u, stored_p = line.split(",")

                print(f"{count}. {stored_u}")

                count += 1

            f.close()

        case 4:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice!")
