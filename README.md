# 🐍 Python Game Development Masterclass

This repository tracks my journey through the [FreeCodeCamp Python for Beginners](https://www.freecodecamp.org) course. The focus is on mastering core programming concepts and applying them to game development logic.

---

## 📂 Repository Structure

The project is organised into logical phases to reflect the progression from basic syntax to advanced object-oriented programming.

```
.
├── 01_Fundamentals/          # Variables, Operators, Strings, and Numbers
├── 02_Data_Structures/       # Lists, Tuples, Sets, and Dictionaries
├── 03_Logics_and_Functions/  # Control Flow, Functions, and Closures
├── 04_Object_Oriented_Programming/  # Classes, Inheritance, and Overloading
├── 05_Advanced_Python/       # Lambdas, Map/Filter/Reduce, and Exceptions
└── Projects/
    └── monster_battle_arena/ # Custom Game Development Project
```

---

## 🚀 Module Details

### Phase 1: Fundamentals (`01_Fundamentals/`)

Focuses on the basic building blocks of Python.

- **Variables:** Using `snake_case` naming conventions and the assignment operator (`=`)
- **Casting:** Converting data types using constructors like `int()`, `float()`, or `str()`
- **Arithmetic:** Implementing mathematical operations, including floor division (`//`) for rounding down results

### Phase 2: Data Structures (`02_Data_Structures/`)

Explores Python's powerful built-in collections.

- **Lists & Tuples:** Using ordered collections and understanding the immutability of tuples
- **Dictionaries:** Storing data in key-value pairs for efficient retrieval
- **Sets:** Managing unique, unordered collections of data

### Phase 3: Logic and Functions (`03_Logics_and_Functions/`)

Implementing program flow and reusable code.

- **Control Flow:** Utilising `if`, `elif`, and `else` statements alongside logical operators (`and`, `or`)
- **Functions:** Defining blocks of code with `def` and understanding indentation-critical logic
- **Variable Scope:** Managing `global` and `nonlocal` variables within nested functions and closures

### Phase 4: Object-Oriented Programming (`04_Object_Oriented_Programming/`)

Building complex systems through objects.

- **Classes:** Creating blueprints with the `class` keyword and the `__init__` constructor
- **Inheritance:** Extending functionality from parent classes to child classes
- **Operator Overloading:** Customising how objects interact with standard operators like `>` or `+`

### Phase 5: Advanced Python (`05_Advanced_Python/`)

Diving into more powerful Python features.

- **Lambdas:** Writing concise anonymous functions
- **Map / Filter / Reduce:** Applying functional programming patterns to collections
- **Exceptions:** Handling errors gracefully with `try/except` blocks

---

## 🎮 Featured Project: Monster Battle Arena

Instead of the standard course projects, this repository features a **Monster Battle Arena** game. This project demonstrates the practical application of:

- **Inheritance:** Different monster types (`Fire`, `Water`) inheriting from a base `Monster` class
- **State Management:** Using `Enum` to track game states like `BATTLE`, `VICTORY`, and `GAME_OVER`
- **Randomised Logic:** Using the `random` library to calculate varied attack damage
- **Error Handling:** Using `try/except` blocks to ensure the game handles invalid user input gracefully

---

## 🛠️ Usage

To run any of the fundamental scripts or the main game project:

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/Py-arcade.git
cd Py-arcade
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run a script:**

```bash
python 01_Fundamentals/basics.py
```

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
