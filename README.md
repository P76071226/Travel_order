# Travel_order

This project is a simple hotel order service built with FastAPI. It includes validation for order inputs using Pydantic and demonstrates the use of design patterns and SOLID principles.

## Table of Contents

- [Setup](#setup)
- [Folder Structure](#folder-structure)
- [Design Patterns and SOLID Principles](#design-patterns-and-solid-principles)
- [Testing](#testing)

## Setup

### Prerequisites

- Docker

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/P76071226/Travel_order.git
    cd Travel_order
    ```

2. **Build and run the Docker container:**

    ```sh
    docker build -t myfastapi .
    docker run -d -v ./app:/app -p 8000:8000 myfastapi
    ```

3. **Access the application:**

    The application will be accessible at `http://localhost:8000`.

## Folder Structure

    ```sh
    Travel_order/
    ├── main.py
    ├── models/
    │ └── order.py
    ├── validators/
    │ └── order_validator.py
    ├── interfaces/
    │ └── validator_interface.py
    ├── services/
    │ └── order_service.py
    ├── custom_exceptions.py
    └── tests/
      └── test_main.py
    ```

## Design Patterns and SOLID Principles


### SOLID Principles

1. **Single Responsibility Principle (SRP):**
   - Each class has a single responsibility. For example, `OrderValidator` handles validation, while `OrderService` handles business logic related to orders.

2. **Open/Closed Principle (OCP):**
   - The `OrderValidator` class is open for extension but closed for modification. New validation rules can be added by extending the class.

3. **Liskov Substitution Principle (LSP):**
   - The `OrderValidator` class can be replaced with any other validator that implements the `ValidatorInterface`.

4. **Interface Segregation Principle (ISP):**
   - The `ValidatorInterface` defines a contract that any validator should follow, promoting interface segregation.

5. **Dependency Inversion Principle (DIP):**
   - High-level modules (e.g., `OrderService`) do not depend on low-level modules but on abstractions (`ValidatorInterface`).

## Testing

    ```sh
    docker run -it -v $(pwd)/app:/app -w /app fastapi pytest
    ```
