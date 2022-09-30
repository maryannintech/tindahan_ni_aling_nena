# making empty lists kasi dito ilalagay yung mga values(?)
grocery_bag = []
amount_list = []
subtotal = []

# displaying yung mga paninda
print("----TINDAHAN NI ALING NENA---\n Suka - P12\n Instant Noodles - P25\n Milo - P9\n Toothpaste - P33\n Candy - P1")


buying = True
while buying == True:

    # getting the item at amount sa user
    item = input("\nAnong bibilhin mo? ") 
    amount = int(input("Ilan bibilhin mo? "))
    # nilalagay yung mga ininput ng user sa respective lists
    grocery_bag.append(item)
    amount_list.append(amount)
    # checking kung alin dito yung sakto(?) sa ininput ng user
    if item.title() == 'Suka':
        total = amount * 12
    elif item.title() == 'Instant Noodle':
        total = amount * 25
    elif item.title() == 'Milo':
        total = amount * 9
    elif item.title() == 'Toothpaste':
        total = amount * 33
    elif item.title() == 'Candy':
        total = amount * 1

    else:
        print("Wala kami non")
    # nilagay yung total sa empty subtotal list
    subtotal.append(total)
    answer = input("Bibili ka pa? oo/hindi - ")
    if answer.lower() == 'hindi':
        buying = False
    # pinag sama yung grocery_bag at amount_list list na mag act as "resibo"
        res = "\n".join("{} - {}".format(x, y) for x, y, in zip(grocery_bag, amount_list))
        print(f"\nRESIBO:\n{res}\nBABAYARAN: {sum(subtotal)}\nSalamat!")
        






    

