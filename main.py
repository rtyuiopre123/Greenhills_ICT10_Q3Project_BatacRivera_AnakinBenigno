from pyscript import display, document


# ===============================
# SIGN UP FUNCTION
# ===============================
def verify_account(e):
    document.getElementById("output").innerHTML = ""

    username = document.getElementById("username").value
    password = document.getElementById("password").value

    if username == "" or password == "":
        display("Please complete all required fields.", target="output")

    elif len(username) < 7:
        display("Username must contain at least 7 characters.", target="output")

    else:
        has_letter = False
        has_number = False

        for character in password:
            if character.isalpha():
                has_letter = True
            elif character.isdigit():
                has_number = True

        if len(password) < 10:
            display("Password must be at least 10 characters long.", target="output")

        elif not has_letter:
            display("Password must contain at least one letter.", target="output")

        elif not has_number:
            display("Password must contain at least one number.", target="output")

        else:
            display("Account successfully created!", target="output")


# ===============================
# TEAM CHECKER FUNCTION
# ===============================
def intrams_qualifications(e):
    document.getElementById("output").innerHTML = ""

    registration = document.querySelector('input[name="reg"]:checked')
    medical = document.querySelector('input[name="med"]:checked')

    grade_value = document.getElementById("grade").value
    section = document.getElementById("section").value

    if registration is None or medical is None or grade_value == "" or section == "":
        display("Please complete all required fields.", target="output")
        return

    grade = int(grade_value)

    if registration.value != "yes":
        display("Please register online to join the intramurals.", target="output")

    elif medical.value != "cleared":
        display("Please secure a medical clearance.", target="output")

    elif grade < 7 or grade > 10:
        display("Only Grades 7 to 10 are eligible.", target="output")

    elif grade == 10 and section == "Sapphire":
        display("Congratulations! Grade 10 Sapphire is part of the Yellow Tigers 🐯", target="output")

    else:
        display("You are eligible. Please wait for official team confirmation.", target="output")


# ===============================
# PLAYERS PAGE (LOOP REQUIRED)
# ===============================
def show_players(e):
    document.getElementById("output").innerHTML = ""

    players = [
        "Aseo, Tessa",
        "Batac, Anakin",
        "Shrestha, Ishan",
        "De Guzman, Vito",
        "Uy, Jennifer",
        "Rivera, Benigno",
        "Ngo, Seth",
    ]

    display("Class: Grade 10 Sapphire", target="output")
    display("---------------------------", target="output")

    for number, name in enumerate(players, start=1):
        display(f"{number}. {name}", target="output")