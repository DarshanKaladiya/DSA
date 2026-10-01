class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Invalid position!")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position!")
            return

        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


l1 = SLL()

while True:
    print("\n----- MENU -----")
    print("1. Insert")
    print("2. Display")
    print("3. Terminate")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            data = int(input("Enter data: "))
            position = int(input("Enter position where you want to insert: "))

            l1.insert(data, position)

        case 2:
            l1.display()

        case 3:
            print("Program terminated.")
            break

        case _:
            print("Invalid choice!")
