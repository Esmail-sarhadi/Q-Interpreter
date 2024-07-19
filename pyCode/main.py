import math

# Function to calculate the square root of a number
def my_sqrt(x):
    # Check if the number is negative, which is not allowed for square root calculation
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    # If the number is zero, the square root is zero
    if x == 0:
        return 0
    # Initial guess for the square root
    last_guess = x
    while True:
        # Compute a new guess using the average of the last guess and x divided by the last guess
        guess = (last_guess + x / last_guess) / 2
        # Check if the guess is accurate enough
        if abs(guess - last_guess) < 1e-9:
            return guess
        # Update the last guess
        last_guess = guess

# Function to calculate base raised to the power of exponent
def my_pow(base, exponent):
    result = 1
    # Multiply the base with itself 'exponent' times
    for _ in range(int(exponent)):
        result *= base
    return result

# Function to calculate the logarithm of a number (approximate value)
def my_log(x):
    # Check if the number is non-positive, which is not allowed for logarithm calculation
    if x <= 0:
        raise ValueError("Cannot calculate logarithm of non-positive number")
    # Large number to approximate the logarithm value
    n = 1000000.0
    # Compute the approximate logarithm using the formula
    return n * ((x ** (1/n)) - 1)

# Function to calculate the sine of an angle (in radians)
def my_sin(x):
    # Normalize the angle to be within the range of 0 to 2*pi
    x = x % (2 * math.pi)
    result = 0
    term = x
    n = 1
    # Calculate the sine value using the Taylor series expansion
    while abs(term) > 1e-10:
        result += term
        n += 2
        term *= -x * x / (n * (n-1))
    return result

# Function to calculate the cosine of an angle (in radians) using sine function
def my_cos(x):
    # Calculate cosine as sine of (pi/2 - x)
    return my_sin(math.pi/2 - x)

# Function to calculate the tangent of an angle (in radians)
def my_tan(x):
    s = my_sin(x)  # Sine of the angle
    c = my_cos(x)  # Cosine of the angle
    # Check for division by zero in tangent calculation
    if abs(c) < 1e-10:
        raise ValueError("Tangent is undefined for this angle")
    return s / c

# Class representing a stack (LIFO data structure)
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item of the stack
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        # Return the top item of the stack without removing it
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def __str__(self):
        # Return a string representation of the stack
        return f"[{', '.join(map(str, self.items))}]"

# Class representing a hash table (for storing variables)
class HashTable:
    def __init__(self):
        # Initialize the hash table with a fixed size
        self.size = 52
        self.table = [None] * self.size
    
    def _hash(self, key):
        # Hash function to convert a character key into an index
        if key.isupper():
            return ord(key) - ord('A')
        else:
            return ord(key) - ord('a') + 26
    
    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        index = self._hash(key)
        self.table[index] = value
    
    def search(self, key):
        # Search for a value by key in the hash table
        index = self._hash(key)
        return self.table[index]
    
    def delete(self, key):
        # Remove a key-value pair from the hash table
        index = self._hash(key)
        self.table[index] = None

# Class representing the Q+ interpreter
class QPlusInterpreter:
    def __init__(self):
        # Initialize the hash table for variables and the stack
        self.variables = HashTable()
        self.stack = Stack()

    def evaluate_postfix(self, expression):
        # Reset the stack for each new expression
        self.stack = Stack()
        print("Initial stack:", self.stack)
        
        # Check if the expression is an assignment (e.g., 'x 3 =')
        if len(expression) == 3 and expression[1].isdigit() and expression[2] == '=':
            variable = expression[0]
            value = float(expression[1])
            self.variables.insert(variable, value)
            print(f"Variable {variable} assigned value: {value}")
            return

        # Process each token in the postfix expression
        for token in expression:
            if token.isdigit():
                # If token is a digit, push it onto the stack as a float
                self.stack.push(float(token))
            elif token.isalpha() and len(token) == 1:
                # If token is a single alphabet character, it is a variable
                value = self.variables.search(token)
                if value is not None:
                    # Push the value of the variable onto the stack
                    self.stack.push(value)
                else:
                    # Raise an error if the variable is not found
                    raise ValueError(f"Unknown variable: {token}")
            else:
                # Apply the operator
                self.apply_operator(token)
            
            # Print the current state of the stack
            print(f"Stack after '{token}': {self.stack}")
        
        # Return the result (the final value on the stack) if the stack is not empty
        return self.stack.pop() if not self.stack.is_empty() else None

    def apply_operator(self, operator):
        # Apply the given operator
        if operator in {'+', '-', '*', '/', '^'}:
            # Handle binary operators
            if self.stack.is_empty():
                raise ValueError(f"Not enough operands for operator: {operator}")
            b = self.stack.pop()
            if self.stack.is_empty():
                raise ValueError(f"Not enough operands for operator: {operator}")
            a = self.stack.pop()
            if operator == '+':
                self.stack.push(a + b)
            elif operator == '-':
                self.stack.push(a - b)
            elif operator == '*':
                self.stack.push(a * b)
            elif operator == '/':
                self.stack.push(a / b)
            elif operator == '^':
                self.stack.push(my_pow(a, b))
        elif operator in {'sqrt', 'log', 'sin', 'cos', 'tan'}:
            # Handle unary operators
            if self.stack.is_empty():
                raise ValueError(f"Not enough operands for operator: {operator}")
            a = self.stack.pop()
            if operator == 'sqrt':
                self.stack.push(my_sqrt(a))
            elif operator == 'log':
                self.stack.push(my_log(a))
            elif operator == 'sin':
                self.stack.push(my_sin(math.radians(a)))
            elif operator == 'cos':
                self.stack.push(my_cos(math.radians(a)))
            elif operator == 'tan':
                self.stack.push(my_tan(math.radians(a)))
        else:
            # Raise an error if the operator is unknown
            raise ValueError(f"Unknown operator: {operator}")

    def interpret(self):
        # Main loop for interpreting user input
        while True:
            try:
                # Read input from the user
                user_input = input('> ')
                # Split the input into tokens
                tokens = user_input.split()
                # Evaluate the postfix expression
                result = self.evaluate_postfix(tokens)
                if result is not None:
                    # Print the result if available
                    print(f"Result: {result}")
            except Exception as e:
                # Print any errors that occur
                print(f"Error: {e}")

# Entry point of the program
if __name__ == "__main__":
    # Create an instance of the interpreter and start interpreting
    interpreter = QPlusInterpreter()
    interpreter.interpret()
