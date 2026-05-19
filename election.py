voted = {}
def check_voter(name):
    if name in voted:
        print("Kick out!")
    else:
        voted[name] = True
        print("Sucessfully voted.")

check_voter("Kiara")
check_voter("Lea")
check_voter("Lea")