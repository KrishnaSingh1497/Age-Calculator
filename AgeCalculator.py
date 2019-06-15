"""  Create a program that asks the "USER" to enter their
    "NAME" and "AGE". Print out a message addressed to them
   that tells them the "YEAR" that they will turn "100 years old". """

name=input("Enter your name: ")
age=int(input("Enter your age: "))
PresentYear=int(input("Enter your running year: "))  #current year running
Difference=100-age                                   # getting difference of current age from 100                            
Year=PresentYear+Difference                         #age after calculating
print("Name is ",name,"and Age is ",age," after 100 year the age will be ",Year,"YEARS.")
