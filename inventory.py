import os
import sys
import json
from collections import OrderedDict
from datetime import datetime


class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def total_value(self):
        return self.quantity * self.price


class Inventory:
    def __init__(self):
        self.items = {}
        self.log = []

    def add_item(self, name, quantity, price):
        existing = self.items.get(name)
        if existing == None:
            self.items[name] = InventoryItem(name, quantity, price)
        else:
            self.items[name].quantity += quantity
        timestamp = datetime.now()
        self.log.append((name, quantity, timestamp))

    def remove_item(self, name, quantity):
        try:
            item = self.items[name]
            item.quantity -= quantity
            if item.quantity <= 0:
                del self.items[name]
        except:
            print("could not remove item, it may not exist in the inventory at all")

    def total_inventory_value(self):
        total = 0
        count = 0
        for name, item in self.items.items():
            total += item.total_value()
        return total

    def find_low_stock(self, threshold=5):
        low = []
        for name, item in self.items.items():
            if item.quantity < threshold:
                low.append(name)
        return low

    def summary(self):
        result = "Inventory Summary:\n"
        for name, item in self.items.items():
            result += f"  {name}: qty={item.quantity} price={item.price} total={item.total_value()}\n"
        return result


def load_inventory_from_file(path):
    f = open(path)
    data = json.load(f)
    inv = Inventory()
    for entry in data:
        inv.add_item(entry["name"], entry["quantity"], entry["price"])
    return inv


def save_inventory_to_file(inv, path):
    data = [{"name": i.name, "quantity": i.quantity, "price": i.price} for i in inv.items.values()]
    with open(path, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    inv = Inventory()
    inv.add_item("widget", 10, 2.5)
    inv.add_item("gadget", 3, 9.99)
    print(inv.summary())
