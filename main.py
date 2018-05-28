from classes import *

def main():
    data = Database("data")
    usr  = User_Input(data)

    # Main loop
    loop = "Main Loop"
    print("Welcome to Keep Track. Type \"help\" for options.")
    while loop != "QUIT":
        loop = usr.get_user_input()
main()
