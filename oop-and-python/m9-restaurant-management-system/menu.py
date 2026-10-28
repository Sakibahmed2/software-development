

class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for food in self.items:
            if food.name.lower() == item_name.lower():
                return food

        return None

    def rmv_item(self, item_name):
        item = self.find_item(item_name)

        if item:
            self.items.remove(item)
            print("Item deleted successfully")
        else:
            print("Item not found!")

    def show_item(self):
        print("\n**** Menu Items ****")
        print("Name\tPrice\tQuantity")

        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.qty}")
