from problem1 import *

if __name__ == "__main__":
    p1 = Point(1, 1)
    p2 = Point(3, 0)
    p3 = Point(4, 1)
    p4 = Point(3, 3)
    p5 = Point(2, 3)

    print("---------Testing the Point class---------\n")

    print("p1: ", p1)
    print("p2: ", p2)
    print("Distance b/w p1 and p2: ", p1.distance(p2))

    p1.rotate(45)
    print("p1 rotated by 45 degrees: ", p1)

    p1.rotate(-45)
    print("p1 rotated by -45 degrees: ", p1)

    p2.translate(-2, 3)
    print("p2 translated by (-2, 3): ", p2)

    p2.translate(2, -3)
    print("p2 translated back by (2, -3): ", p2)
    print()

    print("---------Testing the SimplePoly class---------\n")

    S = SimplePoly(p2, p3, p4, p5)
    print("Simple polygon S has been created as follows: ")
    print(S)

    print("The perimeter of S is ", S.perimeter())

    print("---------Testing the ConvPoly class---------\n")

    P = ConvPoly(p1, p2, p3, p4, p5)
    print("Convex polygon P has been created as follows: ")
    print(P)

    print("The perimeter of P is ", P.perimeter())

    P.translate(-2, 3)
    print("P translated by (-2, 3): ")
    print(P)

    P.rotate(45)
    print("Now P is rotated by 45 degrees: ")
    print(P)

    print("The perimeter of P is ", P.perimeter())
    print("(The answer should be the same as the previous one.)")

    print("The vertices of P are (this checks __getitem__ and __len__): ")
    for i in range(len(P)):
        print(P[i])

    print("Checking iter and next: ")
    i = iter(P)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    try:
        print(next(i))
    except StopIteration: 
        print("A StopIteration was (correctly) caught.")

    newp5 = Point(2, 1.75)
    try:
        P = ConvPoly(p1, p2, p3, p4, newp5)
    except:
        print("\nEXCEPTION CAUGHT: ConvPoly __init__ checking for convexity.")
    else:
        print("\nConvPoly __init__ NOT CHECKING FOR CONVEXITY.")

    print("---------Testing EquiTriangle, Rectangle, and Square---------\n")

    print()
    E = EquiTriangle(3)
    print("An equilateral triangle E with side length 3 has been created: ")
    print(E)

    print("The perimeter of E is ", E.perimeter())
    print("The area of E is ", E.area())

    E.rotate(90)
    print("E, after it has been rotated by 90 degrees: ")
    print(E)

    print()

    R = Rectangle(3, 4)
    print("A rectangle R with width 3 and height 4 has been created.")
    print("Its vertices are: ")
    for v in R:
        print(v)

    print("The perimeter of R is ", R.perimeter())
    print("The area of R is ", R.area())

    R.translate(-1, 2)
    print("R has been translated by (-1, 2). Its vertices are: ")
    for v in R:
        print(v)

    print()
    S = Square(5)
    print("A square S of side length 5 has been created: ")

    print("Its vertices are: ")
    for i in range(len(S)):
        print(S[i])

    print("The perimeter of S is ", S.perimeter())
    print("The area of S is ", S.area())

    print()
    print("That's all for now. Goodbye!")
