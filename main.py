from sympy import *
import os

							#   Get coordinates function
def input_coordinates() -> list:
    coordinates = []
    num_of_coordinates = int(input("Enter number of coordinates: "))
    for i in range(num_of_coordinates):
        first = float(input(f"x{i}: ")) 				# Input number can be float
        second = float(input(f"y{i}: "))
        coordinates.append([first, second])
    return coordinates

def findFH(coordinates) -> list:
    deltaF = []
    h = []
    for i in range(len(coordinates)):
        try:
            h.append(coordinates[i + 1][0] - coordinates[i][0])
            deltaF.append(coordinates[i + 1][1] - coordinates[i][1])
        except IndexError: 					# If it's out of range, just pass
            pass
    return deltaF, h

def findEquations(num_of_coordinates, deltaF, h) -> list:
    """
    Make equations from a list of coordinates
    """
    equations = []

    c = symbols(f"c:{num_of_coordinates}")
    for i in range(1, num_of_coordinates - 1):
        eq = Eq(
            h[i - 1] * c[i - 1] + 2 * (h[i - 1] + h[i]) * c[i] + h[i] * c[i + 1], 		# Formula for equation
            3 * ((deltaF[i]) / h[i] - deltaF[i - 1] / h[i - 1]),
        )

        equations.append(eq)

    return equations, c

def solveEquations(equations, num_of_coordinates, c) -> dict:
    """
    Before solving the equations we have to remove x0 and last x from the list
    """
    equations[0] = equations[0].subs(c[0], 0)
    equations[num_of_coordinates - 3] = equations[num_of_coordinates - 3].subs(
        c[num_of_coordinates - 1], 0
    )
    return solve(equations, c)

									#   Printing table
def printTable(coordinates, delatF, h) -> None:
    num_of_coordinates = len(coordinates)
    os.system("cls")  							# clear the screen
    print("\t \t Table 	\n")
    print("-" * 20)
    for i in range(5):
        if i == 0:
            print("i:  ", end=" ")
        elif i == 1:
            print("xi: ", end=" ")
        elif i == 2:
            print("fi: ", end=" ")
        elif i == 3:
            print("hi: ", end=" ")
        elif i == 4:
            print("dfi: ", end=" ")
        for j in range(num_of_coordinates):
            if i == 0:
                print(f"|{float(j)}|", end=" ")
            if i == 1:
                print(f"|{coordinates[j][0]}|", end=" ")
            if i == 2:
                print(f"|{coordinates[j][1]}|", end=" ")
            try:
                if i == 3:
                    print(f"|{h[j]}|", end=" ")
                if i == 4:
                    print(f"|{delatF[j]}|", end=" ")
            except Exception:
                pass

        print("\n")
    print("-" * 20)

									# Fancy printing
def printSolution(solution) -> None:
    print("\tSolution \n")
    for key in solution:
        print(f"{key} = {solution[key]} \n")

if __name__ == "__main__":
    coordinates = input_coordinates()
    deltaF, h = findFH(coordinates)
    equations, c = findEquations(len(coordinates), deltaF, h)
    solution = solveEquations(equations, len(coordinates), c)
    
    printTable(coordinates, deltaF, h)
    printSolution(solution)
