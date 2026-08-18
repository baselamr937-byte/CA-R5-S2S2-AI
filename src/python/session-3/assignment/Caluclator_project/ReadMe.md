# Console Calculator CLI Application

## 1. Project Overview
A modular and interactive Command-Line Interface (CLI) calculator built with Python. The application handles basic arithmetic operations with clear type annotations, structured docstrings, and safe input handling.

---

## 2. Key Features
* **Core Arithmetic:** Supports addition, subtraction, multiplication, and division.
* **Safe Division:** Prevents crashes by validating non-zero divisors prior to division.
* **Input Validation:** Protects against invalid numeric inputs using structured error handling.
* **Flexible Commands:** Accepts full operation names (e.g., `addition`) or mathematical symbols (e.g., `+`).

---

## 3. Function Reference

| Function | Parameters | Return Type | Description |
| :--- | :--- | :--- | :--- |
| `addition(x, y)` | `x: float, y: float` | `float` | Calculates and returns $x + y$ |
| `subtraction(x, y)` | `x: float, y: float` | `float` | Calculates and returns $x - y$ |
| `multiplication(x, y)` | `x: float, y: float` | `float` | Calculates and returns $x \times y$ |
| `division(x, y)` | `x: float, y: float` | `float` | Calculates and returns $x \div y$ (returns `None` on zero division) |
| `run_calculator()` | `None` | `None` | Manages user prompts and runs the interactive menu loop |

---

## 4. How to Run

1. Open your terminal in the project directory.
2. Run the script:
```bash
python calculator.py