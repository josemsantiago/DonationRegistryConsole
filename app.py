from donations_pkg.homepage import show_homepage
from donations_pkg.user import login , register , donate , show_donations

database = {
    "admin": "password123"
}
donations = []
authorized_user =  ""

while True: 
    while True:
        show_homepage()
        if not authorized_user:
            print("You must be logged in to donate\n")
        else:
            print(f"Logged in as: {authorized_user}\n")
        user_input = input("Choose an option: ")
        if not (int(user_input) > 0 and int(user_input) < 6):
            print("Incorrect Option, Please Try Again\n")
        else: 
            break
    match user_input:
        case "1":
            username = input("Username: ")
            passsword = input("Password: ")
            authorized_user = login(database, username, passsword)
            continue
        case "2":
            username = input("Username: ")
            passsword = input("Password: ")
            authorized_user = register(database,username)
            if authorized_user != "":
                database[username]=passsword
            continue
        case "3":
            if not authorized_user:
                print("You must be logged in to donate\n")
            else:
                donation_string = donate(authorized_user)
                donations.append(donation_string)
            continue
        case "4":
            show_donations(donations)
            continue
        case "5":
            print("Leaving DonateMe...")
            break

        
