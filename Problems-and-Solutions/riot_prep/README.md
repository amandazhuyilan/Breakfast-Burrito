This repo contains questions prepped for the Riot games interview. 
0. [shape_factory.cpp](./src/shape_factory.cpp)

We are building a system to represent various geometric shapes. You are tasked with implementing a Shape Factory that creates objects for different types of shapes. One of the shapes will be a Rectangle, and we want you to implement a hierarchy where all shapes inherit from a common base class Shape. Additionally, we want the Shape Factory to handle object creation.

Requirements:
- Base Class Shape:
Define a base class Shape that has the following methods:
- A pure virtual method `area()` that computes the area of the shape.
- A pure virtual method `perimeter()` that computes the perimeter of the shape.
 - A virtual destructor (to ensure proper cleanup of derived classes).

Derived Class Rectangle:
- Implement the class `Rectangle` that inherits from `Shape`.
- The Rectangle class should have the following properties:
    - Two private member variables: `length` and `width`.
    - A constructor to initialize the `length` and `width`.
    - The `area()` method that returns the area of the rectangle.
    - The `perimeter()` method that returns the perimeter of the rectangle.

Also make a Class `Circle`.

Factory Class ShapeFactory:
Implement a Shape Factory that creates and returns objects of `Shape` type. The factory should be able to create different types of shapes, starting with `Rectangle`. Later, we might add more shapes, like `Circle` or `Triangle`, to the factory.

Testing:
Create a few test cases to demonstrate how the Shape Factory works and how objects of different shapes can be created and used.

1. [ecs_entry.cpp](./src/ecs_entry.cppecs_entry.cpp)

You are designing a system to track status effects on characters in a game. Each character can have multiple active effects that apply various modifications (like "Stunned", "Poisoned", etc.).

For simplicity, assume:

- Each character has a unique ID (integer CharacterId).
- Each status effect has a name and a duration (in milliseconds).

Implement a system in C++ that:
- Adds a status effect to a character.
- Checks if a character has a given effect (e.g., "Is the character stunned?").
- Removes expired effects once they have passed their duration.

Requirements:
- No dynamic memory allocations per effect.
- The system should support up to 1000 characters.
- Performance is important, so avoid inefficient data structures like `std::map` or `std::unordered_map` where possible.

2. Simple RPC Game
Question:
Design a simple turn-based combat system between two characters in a game. Each character has a name, health, and an attack power. Players take turns attacking each other until one of them has 0 or less health. After each attack, print the attacker, the damage dealt, and the remaining health of the opponent.

Your task is to:
- Define the character class.
- Implement the combat loop.
- Make sure the code is clean and extensible.

🧩 Sample Input/Output:
Turn 1: Alice attacks Bob for 10 damage. Bob has 90 health left.
Turn 2: Bob attacks Alice for 8 damage. Alice has 92 health left.
...
Turn 10: Bob attacks Alice for 8 damage. Alice has 0 health left.
Bob wins!
