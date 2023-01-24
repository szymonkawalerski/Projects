print("Podaj login lub zarejestruj się \n")

usersDataBase = {}
notebook = []

from enum import IntEnum


def main():
    control = True

    while control == True:

        Menu_Main = IntEnum('Menu_Main', "Register Login Exit")

        print("""        1. Zarejestruj się
        2. Zaloguj się
        3. Zakończ
        """)

        choice = int(input("Wybierz odpowiednią cyfrę \n"))

        if choice == Menu_Main.Register:

            print("Witaj w panelu rejestracji \n")
            username1 = input("Podaj login")
            password1 = input("Podaj hasło")
            password2 = input("Powtórz hasło")

            lowercase_letters_counter = 0
            uppercase_letters_counter = 0
            special_characters_counter = 0
            number_counter = 0
            special_characters = "!@#$%^&*()"

            """for char in password1:
                if char.islower():
                    lowercase_letters_counter += 1
                if char.isupper(): 
                    uppercase_letters_counter += 1
                if char.isnumeric():
                    number_counter += 1
                if char in special_characters:
                    special_characters_counter += 1"""
            """len(password1) <= 8 and lowercase_letters_counter <= 5 and uppercase_letters_counter == 1 and number_counter == 1 and special_characters_counter == 1 and"""

            if password1 == password2:
                usersDataBase.update({username1:password1})
                print("Zarejestrowano poprawnie \n")
            else:
                print("Hasło musi zawierać jeden znak specjalny, jedną dużą literę, jedną cyfrę i pięć małych liter. (max. 8 znaków) \n")


        elif choice == Menu_Main.Login:

            username1 = input("Podaj login")
            password1 = input("Podaj hasło")

            if username1 in usersDataBase and password1 in usersDataBase:
                print("Zalogowano poprawnie \n")
                user_panel()
            else:
                print("Zły login lub hasło - masz jeszcze 2 próby.\n")

                control = False

                while control == False:

                    username1 = input("Podaj login")
                    password1 = input("Podaj hasło")

                    if username1 in usersDataBase and password1 in usersDataBase:
                        print("Zalogowano poprawnie \n")
                        user_panel()
                        break
                    else:
                        print("Zły login lub hasło - masz jeszcze 1 próbę.\n")
                        username1 = input("Podaj login")
                        password1 = input("Podaj hasło")

                        if username1 in usersDataBase and password1 in usersDataBase:
                            print("Zalogowano poprawnie \n")
                            user_panel()
                            break
                        else:
                            usersDataBase.popitem()
                            print("Twoje konto zostało usunięte ze względu na wpisanie 3x niepoprawnie hasła lub loginu \n")
                            break

        elif choice == Menu_Main.Exit:
            print("Cześć!")
            control = False
        else:
            print("Podałeś złą wartość")

def user_panel():

    User_Panel = IntEnum("User_Panel", "Notebook Logout DeleteAccount")

    control1 = True
    while control1 == True:

        print("""WITAJ W PANELU UŻYTKOWNIKA
                        
        1. Notatnik
        2. Wyloguj
        3. Usuń konto
        """)

        choice2 = int(input("Wybierz odpowiednią cyfrę \n"))

        if choice2 == User_Panel.Notebook:
            notebook_panel()
        elif choice2 == User_Panel.Logout:
            print("Pomyślnie wylogowano")
            control1 = False
        elif choice2 == User_Panel.DeleteAccount:
            usersDataBase.popitem()
            print("Pomyślnie usunięto konto")
            control1 = False
        else:
            print("Podałeś złą wartość")





def notebook_panel():

    Notebook_Panel = IntEnum("Notebook_Panel", "AddTask DeleteTask DisplayNotebook ExitNotebook")

    control2 = True
    while control2 == True:
        print("""NOTATNIK
    
            1. Dodaj zadanie
            2. Usuń zadanie
            3. Wyświetl notatnik
            4. Wyjście z notatnika
            """)
        choice3 = int(input("Podaj co chcesz zrobić"))

        if choice3 == Notebook_Panel.AddTask:
            addTask = input("Jakie zadanie chciałbyś dodać?")
            notebook.append(addTask)

        elif choice3 == Notebook_Panel.DeleteTask:
            print(notebook)
            print("Który index chcesz usunąć? Pierwszy element przyjmuje wartość 0, drugi - 1, itd.")
            indexRemove = int(input())
            notebook.pop(indexRemove)
        elif choice3 == Notebook_Panel.DisplayNotebook:
            print("ZADANIA DO WYKONANIA \n", notebook)
        elif choice3 == Notebook_Panel.ExitNotebook:
            control2 = False
        else:
            print("Podałeś złą wartość")

# wartosci w slowniku maja sie przypisywac do siebie



main()
# poprawi
