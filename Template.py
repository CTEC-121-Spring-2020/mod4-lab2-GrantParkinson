"""
CTEC 121
<Grant Parkinson>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""




from graphics import *
def main():
    # code here
    win = GraphWin("demo", 800, 800)
    win.setCoords(-4.0, -4.0, 4.0, 4.0)
    p1 = Circle(Point(2, 3), 0.5)
    p1.setFill("red")
    p1.draw(win)
    p2 = Circle(Point(-3, 1), 0.5)
    p2.setFill("black")
    p2.draw(win)
    p3 = Circle(Point(-1.5, -2.5), 0.5)
    p3.setFill("blue")
    p3.draw(win)

    input()


main()
