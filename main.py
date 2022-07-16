### ALL IN ONE CALCULATOR
from distutils.command.install_scripts import install_scripts
import os
from pickle import NONE
import sys
from traceback import print_tb
import colorama
from colorama import Fore, init
from prettytable import PrettyTable

def main():
    try:
        init(autoreset=True)
        os.system('cls')
        sys.tracebacklimit = 0
    # Introduction
        print("Welcome to", Fore.CYAN + "All-in-One Calculator!", Fore.RESET + "\nVersion: 1.0\nMade by Debargha!\n")
    # Mode
        # Table
        columns = ["Number", "Applications"]
        myTable = PrettyTable()
        myTable.add_column(columns[0], ["1", "2"])
        myTable.add_column(columns[1], ["General Calculator", "Multiplication Table"])
        print(myTable)
        # / / /
        A = int(input("\nEnter the number of the application: "))
    # Functions
        def gencalc():
            os.system('cls')
            print("### General Calculator\n୨︶꒦꒷♡꒷꒦︶꒦꒷♡︶୧\n")
            gen1 = float(input("Enter your first number: "))
            genop = input("Enter your operator ('+' Add; '-' Subtract;  '*' Multiply; '/' Divide): ")
            gen2 = float(input("Enter your second number: "))
            if genop == '+':
                gens = gen1 + gen2
                print(gen1, '+', gen2, "=", + gens)
            elif genop == '-':
                gens = gen1 - gen2
                print(gen1, '-', gen2, "=", + gens)
            elif genop == '*':
                gens = gen1 * gen2
                print(gen1, 'x', gen2, "=", + gens)
            elif genop == '/':
                gens = gen1 / gen2
                print(gen1, '/', gen2, "=", + gens)
            else:
                print(Fore.RED + "ERROR: Operator is INVALID.")
            home = int(input("Go to (0: HOME, 1: RETRY, 2: EXIT): "))
            if home == 0:
                main()
            elif home == 1:
                gencalc()
            else:
                exit()
        def multab():
            os.system('cls')
            print("### Multiplication Table\n୨︶꒦꒷♡꒷꒦︶꒦꒷♡︶୧\n\nNOTE: You can enter any number between 100.")
            n = int(input("Enter your number: "))
            t = int(input("Enter number of multiplications: "))
            if t <= 100 and n <= 100:
                for a in range(1, t+1):
                    p = n * a
                    print(n, 'x', a, '=', p)
                    continue
            else:
                print(Fore.RED + "Error: Please select a number between 100!")
            home = int(input("Go to (0: HOME, 1: RETRY, 2: EXIT): "))
            if home == 0:
                main()
            elif home == 1:
                multab()
            else:
                exit()
        def areacalc():
            os.system('cls')
            print("### Area Calculator\n୨︶꒦꒷♡꒷꒦︶꒦꒷♡︶୧\n")
            # Table
            columns = ["Number", "Shapes"]
            myTable = PrettyTable()
            myTable.add_column(columns[0], ["1", "2", "3"])
            myTable.add_column(columns[1], ["Square", "Rectangle", "Triangle"])
            print(myTable)
            shape = int(input("/ / / Enter the number of your Shape: "))
            if shape == 1:
                side = int(input("Enter the side of the square: "))
                area = side * side
                print(">>> Area of Square = Side x Side")
                print("Area =", side,'x', side)
                print("\nArea =", area,'sq. unit')
            home = int(input("Go to (0: HOME, 1: RETRY, 2: EXIT): "))
            if home == 0:
                main()
            elif home == 1:
                areacalc()
            else:
                exit()
    # Modes
        if A == 1:
            gencalc()
        elif A == 2:
            multab()
        elif A == 3:
            areacalc()
        else:
            print(Fore.RED + "ERROR: Number of Application is INVALID.")
        main() if input("Do you want to run again? (y/n): ").casefold() == 'y' else exit()
    except ValueError:
        raise ValueError(Fore.RED + "INVALID input.") from None 
main()