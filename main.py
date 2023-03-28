inventory = []


def search():
    my_search = input("Enter the name or description of the product: ")
    for i in inventory:
        if my_search == i['name'] or my_search in i['descriptions']:
            print(i['name'])
        else:
            print(f"Product with this description {my_search} was not found")


def update():
    my_name = input("Enter the name you want to update quantity : ")
    try:
        for i in range(len(inventory)):
            if inventory[i]['name'] == my_name:
                update_quantity = int(input("Enter new quantity: "))
                inventory[i]['quantity'] = update_quantity
                break
        else:
            raise ValueError(f"No such name '{my_name}'")
    except ValueError as ex:
        print(ex)
    finally:
        print("Quantity updated.")


def delete():
    del_name = input("Enter the name you want to delete: ")
    try:
        for i in inventory:
            if del_name in i.values():
                inventory.remove(i)
                break
        else:
            raise ValueError(f"There is no such '{del_name}' product")
    except ValueError as exc:
        print(exc)
    finally:
        print("Product deleted.")


def add_inventory():
    name = input("Enter name: ")
    descriptions = input("Enter description: ")
    quantity = int(input("Enter quantity: "))
    inv = {
        "name": name,
        "descriptions": descriptions,
        "quantity": quantity
    }
    inventory.append(inv)
    print("Product added.")


def menu():
    print("1.View Inventory")
    print("2.Add Item")
    print("3.Remove Item")
    print("4.Update Quantity")
    print("5.Search Inventory")
    print("6.Quit")

    option = input("Enter your choice: ")

    return option


if __name__ == '__main__':
    while True:
        try:
            choice = menu()
            if choice == "2":
                add_inventory()
            elif choice == "1":
                print(inventory)
            elif choice == "3":
                delete()
            elif choice == "4":
                update()
            elif choice == "5":
                search()
            elif choice == "6":
                break
            else:
                raise ValueError("No such operation exists.")
        except ValueError as e:
            print(e)
