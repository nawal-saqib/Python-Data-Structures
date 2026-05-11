#Question 1
class Array:
    def __init__(self, size=1):
        self.number = 0 
        self.capacity_of_array = size 
        self.array = [None] * self.capacity_of_array 

    def append(self, element):
        if self.number == self.capacity_of_array: 
            self.resize()
        self.array[self.number] = element
        self.number += 1
    
    def resize(self):
        new_capacity = self.capacity_of_array * 2
        new_array = [None] * new_capacity
        for i in range(self.number):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity_of_array = new_capacity

    def get(self, index):
        if not 0 <= index < self.number:
            raise IndexError("Invalid index")
        return self.array[index]

    def set(self, index, value):
        if not 0 <= index < self.number:
            raise IndexError("Invalid index")
        self.array[index] = value

    def size(self):
        return self.number

    def capacity(self):
        return self.capacity_of_array

    def display(self):
        for i in range(self.number):
            print(self.array[i])
        print()

class Stack:
    def __init__(self):
        self.stack = Array(9)
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if self.stack.size() == 0:
            return "This stack is empty."
        top_element = self.stack.get(self.stack.size() - 1)
        self.stack.set(self.stack.size() - 1, None) 
        self.stack.number -= 1 
        return top_element
    def peek(self):
        if self.stack.size() == 0:
            return "This stack is empty."
        else:
            top_element = self.stack.get(self.stack.size() - 1)
            return top_element
    def is_empty(self):
        return self.stack.size() == 0

def solve_equation(equation):
    stack = Stack()
    operators = ["+", "-", "*", "/"]
    for i in equation.split(" "):
        if i.isdigit(): 
            stack.push(int(i))
        elif i in operators: 
            digit2 = stack.pop()
            digit1 = stack.pop()
            if i == "+":
                result = digit1 + digit2
            elif i == "-":
                result = digit1 - digit2
            elif i == "*":
                result = digit1 * digit2
            elif i == "/":
                result = digit1 // digit2
            stack.push(result)
    return stack.pop()  

expression = "5 2 + 8 3 - * 4 /"
result = solve_equation(expression)
print("Answer of expression: ")
print(result) 
stackobj1 = Stack()
stackobj1.push(1)
stackobj1.push(2)
stackobj1.push(3)
stackobj1.push(4)
stackobj1.push(5)
print(stackobj1.pop())


#Question 2
class Array:
    def __init__(self, size=1):
        self.number = 0
        self.capacity_of_array = size
        self.array = [None] * self.capacity_of_array

    def append(self, element):
        if self.number == self.capacity_of_array:
            self.resize()
        self.array[self.number] = element
        self.number += 1

    def resize(self, new_capacity=None):
        if new_capacity is None:
            new_capacity = self.capacity_of_array * 2
        new_array = [None] * new_capacity
        for i in range(self.number):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity_of_array = new_capacity

    def get(self, index):
        if not 0 <= index < self.number:
            raise IndexError("Invalid index")
        return self.array[index]

    def set(self, index, value):
        if not 0 <= index < self.number:
            raise IndexError("Invalid index")
        self.array[index] = value

    def size(self):
        return self.number

    def capacity(self):
        return self.capacity_of_array

    def display(self):
        elements = []
        for i in range(self.number):
            elements.append(str(self.array[i]))
        print(" ".join(elements))

class Dequeue:
    def __init__(self):
        self.data = Array(4)
        self.front_index = 0
        self.back_index = 0

    def is_empty(self):
        return self.data.size() == 0

    def enqueue_left(self, value):
        new_array = Array(self.data.capacity_of_array)
        new_array.append(value) 
        for i in range(self.data.size()):
            new_array.append(self.data.get(i))
        self.data = new_array

    def enqueue_right(self, value):
        self.data.append(value)

    def dequeue_left(self):
        if self.is_empty():
            print("Deque is empty.")
            return None
        value = self.data.get(0)
        new_array = Array(self.data.capacity_of_array)
        for i in range(1, self.data.size()):
            new_array.append(self.data.get(i))
        self.data = new_array
        return value

    def dequeue_right(self):
        if self.is_empty():
            print("Deque is empty.")
            return None
        value = self.data.get(self.data.size() - 1) 
        new_array = Array(self.data.capacity_of_array)
        for i in range(self.data.size() - 1): 
            new_array.append(self.data.get(i))
        self.data = new_array
        return value
    
    def display(self):
        self.data.display()

def input_restricted_deque():
    dequeueobj = Dequeue()
    while True:
        print("\n" + "1. Enqueue (Left)")
        print("2. Dequeue Right")
        print("3. Dequeue Left")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            val = input("Enter value to insert: ")
            dequeueobj.enqueue_left(val)
        elif choice == "2":
            val = dequeueobj.dequeue_right()
            if val is not None:
                print("Removed from right:", val)
        elif choice == "3":
            val = dequeueobj.dequeue_left()
            if val is not None:
                print("Removed from left:", val)
        elif choice == "4":
            dequeueobj.display()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


def output_restricted_deque():
    dequeueobj = Dequeue()
    while True:
        print("\n" + "1. Enqueue Right")
        print("2. Enqueue Left")
        print("3. Dequeue")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            val = input("Enter value to insert at right: ")
            dequeueobj.enqueue_right(val)
        elif choice == "2":
            val = input("Enter value to insert at left: ")
            dequeueobj.enqueue_left(val)
        elif choice == "3":
            val = dequeueobj.dequeue_left()
            if val is not None:
                print("Removed from left:", val)
        elif choice == "4":
            dequeueobj.display()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

def main():
    while True:
        print("\n" + "1. Input Restricted Deque")
        print("2. Output Restricted Deque")
        print("3. Exit")
        main_choice = input("Enter your choice: ")
        if main_choice == "1":
            input_restricted_deque()
        elif main_choice == "2":
            output_restricted_deque()
        elif main_choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
main()

#Question 3
class Node:
    def __init__(self, digit=0, next_node=None):
        self.digit = digit
        self.next = next_node

class BigInteger:
    def __init__(self, value=0):
        self.head = None
        if isinstance(value, int):
            value = str(value)
        for digit in reversed(value):
            if digit.isdigit():
                self.append_digit(int(digit))
    
    def append_digit(self, digit):
        if digit < 0 or digit > 9:
            raise ValueError("Digit must be between 0 and 9")
        new_node = Node(digit)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def __str__(self):
        if self.head is None:
            return "0"
        digits = []
        current = self.head
        while current:
            digits.append(str(current.digit))
            current = current.next
        return ''.join(reversed(digits))
    
    def __add__(self, other):
        result = BigInteger()
        carry = 0
        point1 = self.head
        point2 = other.head
        while point1 or point2 or carry:
            if point1:
                digit1 = point1.digit
            else:
                digit1 = 0
            if point2:
                digit2 = point2.digit
            else:
                digit2 = 0
            digit_sum = digit1 + digit2 + carry
            carry = digit_sum // 10
            result.append_digit(digit_sum % 10)
            if point1:
                point1 = point1.next
            if point2:
                point2 = point2.next
        return result

    def __sub__(self, other):
        result = BigInteger()
        borrow = 0
        point1 = self.head
        point2 = other.head
        while point1:
            if point2:
                d2 = point2.digit
            else:
                d2 = 0
            digit_diff = point1.digit - d2 - borrow
            if digit_diff < 0:
                digit_diff += 10
                borrow = 1
            else:
                borrow = 0
            result.append_digit(digit_diff)
            point1 = point1.next
            if point2:
                point2 = point2.next
        return result

def main():
    num1 = BigInteger(45389)
    num2 = BigInteger(12345)
    print("Number 1: " + str(num1))
    print("Number 2: " + str(num2))
    sum_result = num1 + num2
    print("Sum: " + str(num1) + " + " + str(num2) + " = " + str(sum_result))
    sub_result = num1 - num2
    print("Difference: " + str(num1) + " - " + str(num2) + " = " + str(sub_result))

main()

#Question 4
class Process:
    def __init__(self, name, time_required):
        self.name = name
        self.time_required = time_required
    
    def __str__(self):
        return "Process " + self.name + " Time Required: " + str(self.time_required)

class Node:
    def __init__(self, process):
        self.process = process
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def append(self, process):
        new_node = Node(process)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def remove_from_start(self):
        if self.is_empty():
            return None
        removed_process = self.head.process
        self.head = self.head.next
        return removed_process
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.head
        while current:
            print(current.process)
            current = current.next
    
    def remove_by_name(self, name):
        if self.is_empty():
            return False
        if self.head.process.name == name:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next:
            if current.next.process.name == name:
                current.next = current.next.next
                return True
            current = current.next
        return False
    

class RoundRobinScheduler:
    def __init__(self, quantum=1):
        self.process_queue = LinkedList()
        self.quantum = quantum
        self.scheduler_running = False
    
    def add_task(self, name, time_required):
        if self.scheduler_running:
            print("Cannot add tasks. Scheduler is already running.")
            return
        process = Process(name, time_required)
        self.process_queue.append(process)
        print("Added: " + str(process))
    
    def delete_task(self, name):
        if self.process_queue.remove_by_name(name):
            print("Process " + name + " removed successfully.")
        else:
            print("Process " + name + " not found.")
    
    def run_scheduler(self):
        if self.process_queue.is_empty():
            print("No processes to schedule.")
            return
        
        self.scheduler_running = True  
        print("\n" + "Starting Round Robin Scheduler with quantum = " + str(self.quantum))
        
        iteration = 1
        while not self.process_queue.is_empty():
            print("\n" + "Iteration " + str(iteration) + " :")
            self.process_queue.display()
            
            current_process = self.process_queue.remove_from_start()
            
            if current_process.time_required <= self.quantum:
                print("Executing: " + str(current_process) + " - Process Completed!")
            else:
                print("Executing: " + str(current_process) + " - " + str(self.quantum) + " time units")
                current_process.time_required -= self.quantum
                self.process_queue.append(current_process)

            iteration += 1

        print("\n" + "All processes completed. Scheduler terminated.")
        self.scheduler_running = False

def main():
    scheduler = RoundRobinScheduler(2)
    while True:
        print("1 - Add a task")
        print("2 - Delete a task")
        print("3 - Run Scheduler")
        print("4 - Exit")
        choice = input("\n" + "Enter your choice (1-4): ")

        if choice == "1":
            if scheduler.scheduler_running:
                print("Cannot add tasks. Scheduler is already running.")
                continue
            name = input("Enter process name: ")
            try:
                time_required = int(input("Enter time required: "))
                if time_required <= 0:
                    print("Time required must be a positive integer.")
                    continue
                scheduler.add_task(name, time_required)
            except ValueError:
                print("Invalid input. Time required must be an integer.")
        
        elif choice == "2":
            name = input("Enter process name to delete: ")
            scheduler.delete_task(name)
        
        elif choice == "3":
            scheduler.run_scheduler()
        
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()
