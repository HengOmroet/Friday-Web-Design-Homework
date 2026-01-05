print("+++welcome BacII Grading Analyzer +++")
print("")
ch=input("Choose Major class (science or social) ")
if ch=="science":
    print("You are Science Class")
    print("+++ Enter subject Score +++")
    kh=float(input("1.Khmer(0-75): "))
    math=float(input("2.Math(0-125): "))
    bio=float(input("3.Biology(0-75): "))
    chem=float(input("4.Chemistry(0-50): "))
    phy=float(input("5.Physics(0-75): "))
    his=float(input("6.History(0-50): "))
    eng=float(input("7.English(0-50): "))
    if eng>=25: eng=eng-25
    total=kh+math+bio+chem+phy+his+eng
    print("Total:",total)
    if total>= 428: grade="A"
    if total>= 380: grade="B"
    if total>= 333: grade="C"
    if total>= 285: grade="D"
    if total>= 237.5: grade="E"
    else: grade="F"
    print("Total Score ",total)
    print("Grade:",grade)