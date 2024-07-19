Q+ Interpreter
Q+ Interpreter is a Python-based calculator that uses postfix notation (Reverse Polish Notation) to perform various mathematical operations. This project implements a custom stack-based interpreter for a simple language called Q+.
Features

Basic arithmetic operations: addition, subtraction, multiplication, division, and exponentiation
Mathematical functions: square root, logarithm, sine, cosine, and tangent
Variable assignment and usage
Custom implementations of mathematical functions without relying on external libraries
Stack-based evaluation of postfix expressions
Simple hash table for variable storage

How It Works
The Q+ Interpreter uses a stack to evaluate postfix expressions. It supports the following operations:

Pushing numbers onto the stack
Performing operations on the top elements of the stack
Assigning values to variables
Using variables in expressions

The interpreter processes input token by token, either pushing values onto the stack or applying operators to the values on top of the stack.
Usage
To use the Q+ Interpreter:

Run the script
Enter expressions in postfix notation at the prompt
The interpreter will evaluate the expression and display the result

Example usage:
Copy> 3 4 +
Stack after '3': [3.0]
Stack after '4': [3.0, 4.0]
Stack after '+': [7.0]
Result: 7.0

> x 5 =
Variable x assigned value: 5.0

> x 3 *
Stack after 'x': [5.0]
Stack after '3': [5.0, 3.0]
Stack after '*': [15.0]
Result: 15.0

> 90 sin
Stack after '90': [90.0]
Stack after 'sin': [1.0]
Result: 1.0
Implementation Details

Stack: A custom implementation of a stack data structure
HashTable: A simple hash table for storing variables
QPlusInterpreter: The main interpreter class that handles input processing and expression evaluation
Custom implementations of mathematical functions: my_sqrt, my_pow, my_log, my_sin, my_cos, my_tan

Limitations

The interpreter assumes well-formed input and may not handle all error cases gracefully
Trigonometric functions use radians internally but expect input in degrees
The hash table for variables has a fixed size and uses a simple hashing function

Future Improvements

Implement error handling for malformed expressions
Add support for multi-character variable names
Extend the set of supported mathematical functions
Implement a more sophisticated variable storage system

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please fork the repository and submit a pull request. Ensure your changes are well-documented and tested.

## Author
This project was created by Esmail Sarhadi . You can find more of my work on my GitHub profile: https://github.com/Esmail-sarhadi
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

<h2 id="donation">Donation</h2>

<p>If you find this project helpful, consider making a donation:</p>
<p><a href="https://nowpayments.io/donation?api_key=REWCYVC-A1AMFK3-QNRS663-PKJSBD2&source=lk_donation&medium=referral" target="_blank">
     <img src="https://nowpayments.io/images/embeds/donation-button-black.svg" alt="Crypto donation button by NOWPayments">
</a></p>
