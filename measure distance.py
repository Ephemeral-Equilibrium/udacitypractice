added = int(input("How far did you go?"))
#when the distance is less than 20
if added < 20 and added >=0:
    print("No charge")
#when the distance is more than 20 and less than 200
elif added >=20 and added<200:
    print ((added - 20)*1.2)
#When the distance is more than 200
elif added >=200:
    print ((((added-20)-(added-200))*1.2)+(added-200)*0.8)
#WHEN IT'S NEITHER 
else:
    print("please redo")
    added = int(input("How far did you go?"))
