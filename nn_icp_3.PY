#program for grading scheme


inputscore=float(input("enter the score:"))
if(inputscore>=90 and inputscore<=100):
    print("GRADE A")
elif(inputscore>=80 and inputscore<=89.9):
    print("GRADE B")
elif(inputscore>=70 and inputscore<=79.9):
    print("GRADE C")
elif(inputscore>=60 and inputscore<=69.9):
    print("GRADE D")
else:
    print("GRADE F")