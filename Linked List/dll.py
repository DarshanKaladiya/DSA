class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node

        new_node.next = self.head
        self.head = new_node
        print("Node inserted at beginning.")

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print("Node inserted at end.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp
        print("Node inserted at end.")

    def insert_position(self, data, pos):
        if pos < 1:
            print("Invalid position!")
            return

        if pos == 1:
            self.insert_begin(data)
            return

        temp = self.head

        for i in range(1, pos - 1):
            if temp is None:
                print("Invalid position!")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position!")
            return

        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node
        print("Node inserted at position", pos)

    def display(self):
        if self.head is None:
            print("Linked List is empty!")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty!")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print("Node deleted from beginning.")

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty!")
            return

        if self.head.next is None:
            self.head = None
            print("Node deleted from end.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None
        print("Node deleted from end.")

    def delete_position(self, pos):
        if self.head is None:
            print("Linked List is empty!")
            return

        if pos < 1:
            print("Invalid position!")
            return

        if pos == 1:
            self.delete_begin()
            return

        temp = self.head

        for i in range(1, pos):
            if temp is None:
                print("Invalid position!")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position!")
            return

        temp.prev.next = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

        print("Node deleted from position", pos)

    def Count(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Count =", count)

    def Search(self, sr):
        temp = self.head

        while temp is not None:
            if sr == temp.data:
                print(sr, "is available")
                return
            temp = temp.next

        print(sr, "is not available")


l1 = DLL()

while True:
    print("\n-------------------------")
    print("0  : Exit")
    print("1  : Insert At Beginning")
    print("2  : Insert At End")
    print("3  : Insert At Specific Position")
    print("4  : Display")
    print("5  : Delete From Beginning")
    print("6  : Delete From End")
    print("7  : Delete From Specific Position")
    print("8  : Count Nodes")
    print("9  : Search")
    print("-------------------------")

    choice = int(input("Enter Your Choice => "))

    if choice == 1:
        data = int(input("Enter Your Data => "))
        l1.insert_begin(data)

    elif choice == 2:
        data = int(input("Enter Your Data => "))
        l1.insert_end(data)

    elif choice == 3:
        data = int(input("Enter Your Data => "))
        pos = int(input("Enter Position => "))
        l1.insert_position(data, pos)

    elif choice == 4:
        l1.display()

    elif choice == 5:
        l1.delete_begin()

    elif choice == 6:
        l1.delete_end()

    elif choice == 7:
        pos = int(input("Enter Position => "))
        l1.delete_position(pos)

    elif choice == 8:
        l1.Count()

    elif choice == 9:
        sr = int(input("Enter Data To Search => "))
        l1.Search(sr)

    elif choice == 0:
        print("Program exited!")
        break

    else:
        print("Invalid choice! Please try again.")
