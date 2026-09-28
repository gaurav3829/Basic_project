rent = int(input("Enter your room/flat rent amount for ruppes : ->"))
food = float(input("Enter your oveall food eexpence : ->"))
eletricity_bill = float(input("Enter your room/flat light bill amount: ->"))
person = int(input("Enter roommet/flatmeet Number : ->"))

total=(rent+food+eletricity_bill)//person

print("this amount per person : -",total)