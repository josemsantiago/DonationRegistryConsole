def login(database, username, password):
    if username in database:
        if database[username] == password:
            print(f"Welcome back {username}!\n")
            return username
        else:
            print("Incorrect Password\n")
            return ""
    else:
        print("User not found. Please register.\n")
        return ""


def register(database, username):
    if username in database:
        print(f"{username} already registered. Please login\n")
        return ""
    else:
        print(f"{username} has been registered\n")
        return username


def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_string = f"{username} donated ${float(donation_amt):0,.2f}"
    print("Thank you for your donation!")
    return donation_string


def show_donations(donations):
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        print("\n--- All Donations ---")
        for donation in donations:
            print(donation)
