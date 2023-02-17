#Imports
import cashier_data as data
#Functions
def recipt():
    print
def main():
    #Variables
    item = []
    total = 0

    data.clear()
    data.welcome()
    while True:
        ask = (input("The name of your item: "))
        ask = ask.capitalize()
        cost = float(input("The cost of your item (please only numbers): $"))
        item.append ((ask, cost))
        total += cost
        again = input("Do you have more items? (y/n) ")
        again = again.lower()
        if again == "n":
            break
    sub_t = data.discount(total)
    t = data.gst(sub_t)
    print("""
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              Python Foods""")
    for item in item:
        print(f"""
        {item[0]}: ${item[1]:.2f}""")
    print(f"""
    =================================

    Sub (w/o disc): {total:.2f}
    Sub (w/ disc): {sub_t:.2f}
    Total: {t:.2f}

    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """)
    data.logo()
#Output
main()