class Set:
    def __init__(self):
        self.elements = set()

    def add(self, element):
        self.elements.add(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            print(f"Element{element} not found in the set.")

    def contains(self, element):
        return element in self.elements

    def size(self):
        return len(self.elements)

    def iterator(self):
        return iter(self.elements)

    def intersection(self, other_set):
        return self.elements.intersection(other_set.elements)

    def union(self, other_set):
        return self.elements.union(other_set.elements)

    def difference(self, other_set):
        return self.elements.difference(other_set.elements)

    def subset(self, other_set):
        return self.elements.issubset(other_set.elements)

    def display(self):
        print("Set elements:", self.elements)


def menu():
    print("\nSet ADT Operations Menu:")
    print("1. Add an element to the set")
    print("2. Remove an element from the set")
    print("3. Check if an element is in the set")
    print("4. Display the size of the set")
    print("5. Iterate over the set")
    print("6. Find the intersection of two sets")
    print("7. Find the union of two sets")
    print("8. Find the difference between two sets")
    print("9. Check if one set is a subset of another")
    print("10. Display the set")
    print("0. Exit")

def main():
    set1 = Set()
    set2 = Set()

    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            element = int(input("Enter element to add to the set: "))
            set1.add(element)
        elif choice == 2:
            element = int(input("Enter element to remove from the set: "))
            set1.remove(element)
        elif choice == 3:
            element = int(input("Enter element to check if it is in the set: "))
            if set1.contains(element):
                print(f"Element {element} is in the set.")
            else:
                print(f"Element {element} is not in the set.")
        elif choice == 4:
            print(f"Size of the set: {set1.size()}")
        elif choice == 5:
            print("Iterating over the set:")
            for element in set1.iterator():
                print(element, end=" ")
            print()
        elif choice == 6:
            print("Find intersection of two sets.")
            # Input for second set
            set2_elements = input("Enter elements for second set (comma separated): ").split(",")
            set2_elements = set(map(int, set2_elements))
            set2 = Set()
            for elem in set2_elements:
                set2.add(elem)
            print("Intersection of the sets:", set1.intersection(set2))
        elif choice == 7:
            print("Find union of two sets.")
            # Input for second set
            set2_elements = input("Enter elements for second set (comma separated): ").split(",")
            set2_elements = set(map(int, set2_elements))
            set2 = Set()
            for elem in set2_elements:
                set2.add(elem)
            print("Union of the sets:", set1.union(set2))
        elif choice == 8:
            print("Find difference between two sets.")
            # Input for second set
            set2_elements = input("Enter elements for second set (comma separated): ").split(",")
            set2_elements = set(map(int, set2_elements))
            set2 = Set()
            for elem in set2_elements:
                set2.add(elem)
            print("Difference of the sets:", set1.difference(set2))
        elif choice == 9:
            print("Check if one set is a subset of another.")
            # Input for second set
            set2_elements = input("Enter elements for second set (comma separated): ").split(",")
            set2_elements = set(map(int, set2_elements))
            set2 = Set()
            for elem in set2_elements:
                set2.add(elem)
            if set1.subset(set2):
                print("The first set is a subset of the second set.")
            else:
                print("The first set is not a subset of the second set.")
        elif choice == 10:
            set1.display()
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
