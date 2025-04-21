This repo contains questions prepped for the Riot games interview. 

1. [Shape Factory](./src/shape_factory.cpp)

We are building a system to represent various geometric shapes. You are tasked with implementing a Shape Factory that creates objects for different types of shapes. One of the shapes will be a Rectangle, and we want you to implement a hierarchy where all shapes inherit from a common base class Shape. Additionally, we want the Shape Factory to handle object creation.

Requirements:
- Base Class `Shape:
Define a base class Shape that has the following methods:
- A pure virtual method `area()` that computes the area of the shape.
- A pure virtual method `perimeter()` that computes the perimeter of the shape.
 - A virtual destructor (to ensure proper cleanup of derived classes).

Derived Class `Rectangle`:
- Implement the class `Rectangle` that inherits from `Shape`.
- The Rectangle class should have the following properties:
    - Two private member variables: `length` and `width`.
    - A constructor to initialize the `length` and `width`.
    - The `area()` method that returns the area of the rectangle.
    - The `perimeter()` method that returns the perimeter of the rectangle.

Also make a Class `Circle`.

Factory Class `ShapeFactory`:
Implement a Shape Factory that creates and returns objects of `Shape` type. 

The factory should be able to create different types of shapes, starting with `Rectangle`. Later, we might add more shapes, like `Circle` or `Triangle`, to the factory.

Testing:
Create a few test cases to demonstrate how the Shape Factory works and how objects of different shapes can be created and used.

2. Simple RPC Game
Question:
Design a simple turn-based combat system between two characters in a game. Each character has a name, health, and an attack power. Players take turns attacking each other until one of them has 0 or less health. After each attack, print the attacker, the damage dealt, and the remaining health of the opponent.

Your task is to:
- Define the character class.
- Implement the combat loop.
- Make sure the code is clean and extensible.

Sample Output:
```
Turn 1: Alice attacks Bob for 10 damage. Bob has 90 health left.
Turn 2: Bob attacks Alice for 8 damage. Alice has 92 health left.
...
Turn 10: Bob attacks Alice for 8 damage. Alice has 0 health left.
Bob wins!
```

3. [Simple ECS](./src/simple_ecs.cpp)

You're building a mini ECS (Entity-Component-System) game engine to simulate objects moving around a map. Each object is an entity, and they have components like Position and Velocity. Your goal is to implement thread-safe component storage and a movement system that updates entity positions in a multithreaded environment.

ECS core concepts:
- Entity: A unique identifier (e.g., `uint32_t`) for game objects.
- Component: Pure data like Position, Velocity.
- System: Logic that processes entities with specific components (e.g., `MovementSystem`).

Implement component storage:
- `PositionComponentStorage` and `VelocityComponentStorage` should store components per entity.
- Must use RAII for lock management (`std::lock_guard` or `std::scoped_lock`).
- Must use `std::mutex` to ensure thread-safe access.

Create a `MovementSystem`:
- For each entity with both `Position` and `Velocity`, compute the new position.
- Updates should be safely handled in multithreaded execution.

Simulate the game:
- Create a few tank entities.
- Run the movement system in multiple threads.
- Print the final positions.

Sample output:
```
Entity 1 final position: (2, 0)
Entity 2 final position: (4, 6)
Entity 3 final position: (11, -1.5)
```

4. [Ticked-based Combat System](./src/tick_based_combat.cpp)

Build a combat system for a small multiplayer game that runs at 20 ticks per second. Players send inputs (e.g., move or attack commands) to the server. The server processes the inputs in discrete simulation ticks and sends back authoritative state updates.

Design a simplified system that includes the following:
- `PlayerInput` struct – represents player commands (movement/attack).
- `PlayerState` struct – stores player position, health, and unique ID.
- `GameServer` class – receives inputs, runs simulation on fixed ticks, and broadcasts updated player states
- `GameClient` class – sends inputs, receives states, and performs client-side interpolation between server snapshots.

Requirements:
- The server should process all received inputs each tick.
- Health should decrease if a player is within range of an attacker.
- Client interpolation should be based on the last two server snapshots.
- Use appropriate C++ data structures (e.g., `std::deque`, `std::map`, `std::chrono`).
    - Use `std::chrono` or a mock tick manager.
- Assume 1v1 combat only.

