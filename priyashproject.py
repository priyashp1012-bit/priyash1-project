from datetime import date

print("welcome the interactive personal data collector!")

print( 


   )


name = input("pls enter your name :-  ")
age = int(input("pls enter your age :-  "))
heigth = float(input("pls enter your heigth in meters :-  "))
favourite = int(input("pls enter your favourite number :-  "))


print( 


   )



print("thank you! here is the information we collected :")


print( 


   )



print(f"Name: {name} (type: {type(name)} , memory address: {id(name)}) ")
print(f"age: {age} (type: {type(age)} , memory address: {id(age)}) ")
print(f"heigth: {heigth} (type: {type(heigth)} , memory address: {id(heigth)}) ")
print(f"favourite: {favourite} (type: {type(favourite)} , memory address: {id(favourite)}) ")


print( 


   )




current_year = date.today().year
birth_year = current_year - age
print(f"Your birth year is approximately : {birth_year} (based on your age of {age})" )



print( 


   )




print("thank you for using the personal data collector. goodbye!")

