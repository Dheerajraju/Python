age=int(input("enter the persons name"))
is_student = input("are you a student(yes/no):").lower() ##lower() converts into lower case

if age <=5:
    price = "free"
elif age <=12:
    price = "$10"
elif age <=17:
    if is_student == 'yes':
        price = "$12"
    else:
        price = "$20"
elif age <=60:
    if is_student == "yes":
        price = "$18"
    else:
        price = "$20"
else:
    price = "$20"

print("ticket price:",price)
