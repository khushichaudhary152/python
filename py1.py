print("Welcome to the Interactive personal Data Collector!")


name= input("\nplease enter your name:")
age= int(input("please enter your age:"))
height= float(input("please enter height in meters:"))
number= int(input("please enter your favourite number:"))


print("\nThank you! here is the information we collected:")
      

print("\nname:",name,"(type:",type(name),",Memory Address:",id(name),")")
print("age:",age,"(type:",type(age),",Memory address:",id(age),")")
print("height:",height,"(type:",type(height),",Memory address:",id(height),")")
print("number:",number,"(type:",type(number),",Memory address:",id(number),")")

birth_year= 2026 - age
        
print("\nyour birth year is approximately:",birth_year, "(based on your age of",age,")")

print("\nThank you for using the personal data collector. Goodbye!")        

