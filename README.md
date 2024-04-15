# Compiler Design Project

This project is a Flask web application developed as part of our Compiler Design course. It takes an infix expression as input, calculates the postfix expression, and generates intermediate code (IC) for a simple compiler. The intermediate code follows a three-address code format with triples, indirect triples, and quadruples. 

## Features

- Converts infix expressions to postfix expressions.
- Generates intermediate code in a simple three-address code format.
- Supports basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/).
- Provides a web interface for easy interaction.

## Technologies Used

- **Python**: Used for the backend logic and Flask framework for web development.
- **HTML/CSS/JavaScript**: Used for creating the webpage interface.
- **Flask**: Micro web framework for Python used to develop the web application.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/Fawaz-Khan-R/Intermediate-Code-Generator.git
    ```

2. Navigate to the project directory:

    ```
    cd Intermediate-Code-Generator
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```
    python views.py
    ```

5. Access the application through a web browser at `http://localhost:5000`.

## Usage

1. Enter an infix expression in the input field.
2. Click on the "Convert" button.
3. The postfix expression and intermediate code will be displayed.

## Examples

- **Input**: `a+b*c` (Make sure there are no spaces in between)
  - **Postfix**: `abc*+`
  - **Intermediate Code**:
    ```
    1. t1 = b * c
    2. t2 = a + t1
    ```

- **Input**: `(a+b)*c/d`
  - **Postfix**: `ab+c*d/`
  - **Intermediate Code**:
    ```
    1. t1 = a + b
    2. t2 = t1 * c
    3. t3 = t2 / d
    ```

## Contributors

- [Fawaz Khan R](https://github.com/Fawaz-Khan-R)
- [Dibyansu Singh](https://github.com/dibyansu06)

## License

This project is licensed under the [MIT License](LICENSE).
