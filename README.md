# 🧮 CalCulus v0.2.0

**A high-performance C++ calculus and mathematics engine for Python, built with pybind11.**

[Go back](https://github.com/LegedsDaD/CalCulus)
to main page for version information and many more.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![C++](https://img.shields.io/badge/C%2B%2B-17-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
![PyPI Version](https://img.shields.io/pypi/v/calculus?style=flat-square)
![PyPI Downloads](https://img.shields.io/pypi/dm/calculus?style=flat-square)
![Wheel](https://img.shields.io/pypi/wheel/calculus?style=flat-square)
![Code Size](https://img.shields.io/github/languages/code-size/LegedsDaD/CalCulus?style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/LegedsDaD/CalCulus?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/LegedsDaD/CalCulus?style=flat-square)
![Math Library](https://img.shields.io/badge/domain-mathematics-purple?style=flat-square)
![Physics Ready](https://img.shields.io/badge/physics-ready-red?style=flat-square)
![Robotics](https://img.shields.io/badge/robotics-supported-blueviolet?style=flat-square)

---

## 📌 Overview

**CalCulus** is a **fast, lightweight scientific computing library** written in **C++** and exposed to **Python** using **pybind11**.

It is designed for:
- 🚀 Robotics projects  
- 📐 Engineering calculations  
- 🔬 Physics simulations  
- 🧠 Educational & research use  

CalCulus provides **C++-level performance** while keeping a **simple Python interface**.

---

## ✨ Features

- ⚡ High-performance C++ backend
- 🧮 Scalar & vector mathematics
- 📐 Numerical integration (Simpson’s Rule)
- 🧱 Clean object-oriented API
- 🔗 Python bindings via pybind11
- 🧪 Ideal for robotics & simulation
- 📦 Easy `pip install .` workflow

---
## 🔬 NumPy vs CalCulus Comparison

| Feature | NumPy | CalCulus |
|------|------|---------|
| Core Language | C + Python | Pure C++ (pybind11) |
| Focus | Array-based numerical computing | Scientific math, physics & robotics |
| Scalar Operations | `numpy.float64` | `Scalar` C++ class |
| Trigonometric Functions | ✔ Vectorized | ✔ High-precision scalar |
| Vector Algebra | Limited (manual) | ✔ Built-in `Vec3` |
| Dot Product | ✔ | ✔ |
| Cross Product | ✔ (via `np.cross`) | ✔ Native |
| Numerical Integration | Limited | ✔ Simpson’s Rule |
| Physical Constants | Partial | ✔ Built-in |
| Robotics Use | Medium | ✔ High |
| Physics Simulations | Medium | ✔ High |
| C++ Performance | ❌ | ✔ |
| SIMD / Low-level Control | ❌ | ✔ |
| Learning Curve | Easy | Moderate |
| Best Use Case | Data science, ML | Robotics, physics engines |
| Python Dependency | Heavy | Minimal |
| Custom Math Engine | ❌ | ✔ |
| Real-Time Applications | ❌ | ✔ |

---

### 📝 When to Use Which?

- Use **NumPy** when:
  - Working with large datasets
  - Doing machine learning or statistics
  - Needing array broadcasting

- Use **CalCulus** when:
  - Building robotics or physics engines
  - Needing C++-level performance
  - Working with vectors, forces, motion, integration
 

## 📂 Project Structure
```
CalCulus_CPP/
│
├── calculus/
│   ├── __init__.py
│   ├── _core.py
│
├── calculus_core.cpp
├── pyproject.toml
├── setup.py
├── README.md
├── LICENSE
```
## 📦 Installation

### 🔧 Requirements

- Python **3.8+**
- C++17 compatible compiler (MSVC / GCC / Clang)
- **Windows only:** Visual Studio with C++ Desktop development
- pybind11 (`pip install pybind11`)

---

### ▶ Install from Source

Run from project root:

```bash
pip install .
```


---

### **8️⃣ API Overview**
## 🧮 API Overview

### 🔢 Scalar

Represents a single numeric value.

| Method / Operator | Description |
|------------------|------------|
| `+ - * /` | Arithmetic operations |
| `sin()` | Sine |
| `cos()` | Cosine |
| `tan()` | Tangent |
| `asin()` | Inverse sine |
| `acos()` | Inverse cosine |
| `atan()` | Inverse tangent |
| `sinh()` | Hyperbolic sine |
| `cosh()` | Hyperbolic cosine |
| `tanh()` | Hyperbolic tangent |
| `exp()` | Exponential |
| `log()` | Natural logarithm |
| `log10()` | Base-10 logarithm |
| `pow(n)` | Power (auto-converts floats to Scalar) |
| `sqrt()` | Square root |
| `cbrt()` | Cube root |
| `abs()` | Absolute value |

---

### 📐 Vec3 (3D Vector)

| Method | Description |
|------|------------|
| `+ -` | Vector addition / subtraction |
| `*` | Scalar multiplication |
| `dot(v)` | Dot product |
| `cross(v)` | Cross product |
| `magnitude()` | Vector length |
| `normalize()` | Unit vector |

---

### 🧠 Solver

| Method | Description |
|------|------------|
| `integrate(func, a, b, n)` | Simpson’s Rule integration (n must be even) |

---

### 🌌 Constants

| Constant | Description |
|--------|------------|
| `pi` | π |
| `e` | Euler’s number |
| `g` | Gravity |

## Ultimate Test Code
```python
import calculus as c

print("===== CalCulus Library Test =====\n")

# ---------------- Scalar Tests ----------------
print("-> Testing Scalar class")
a = c.Scalar(5)
b = c.Scalar(3)

print("a =", a.value)
print("b =", b.value)
print("Addition: a + b =", (a + b).value)
print("Subtraction: a - b =", (a - b).value)
print("Multiplication: a * b =", (a * b).value)
print("Division: a / b =", (a / b).value)

print("Trigonometric: sin(a) =", a.sin())
print("Trigonometric: cos(a) =", a.cos())
print("Trigonometric: tan(a) =", a.tan())
print("Inverse trig: asin(0.5) =", c.asin(0.5))
print("Inverse trig: acos(0.5) =", c.acos(0.5))
print("Inverse trig: atan(1) =", c.atan(1))
print("Hyperbolic: sinh(a) =", a.sinh())
print("Hyperbolic: cosh(a) =", a.cosh())
print("Hyperbolic: tanh(a) =", a.tanh())
print("Exponential: exp(a) =", a.exp())
print("Logarithm: log(a) =", a.log())
print("Log base 10: log10(a) =", a.log10())
print("Square root: sqrt(a) =", a.sqrt())
print("Cube root: cbrt(a) =", a.cbrt())
print("Absolute: abs(-a) =", c.abs(-5))
print("Power: a^3 =", c.pow(a, 3))
print()

# ---------------- Vec3 Tests ----------------
print("-> Testing Vec3 class")
v1 = c.Vec3(1, 2, 3)
v2 = c.Vec3(4, 5, 6)

print("v1 =", v1)
print("v2 =", v2)
print("Addition: v1 + v2 =", v1 + v2)
print("Subtraction: v1 - v2 =", v1 - v2)
print("Scalar multiplication: v1 * 2 =", v1 * 2)
print("Dot product: v1 · v2 =", v1.dot(v2))
print("Cross product: v1 × v2 =", v1.cross(v2))
print("Magnitude of v1:", v1.magnitude())
print("Normalized v1:", v1.normalize())
print()

# ---------------- Solver Tests ----------------
print("-> Testing Solver integration")
f = lambda x: x**2
area = c.Solver.integrate(f, 0, 3, 1000)
print("Integral of x^2 from 0 to 3 =", area)

# Example: center of mass
density = lambda x: x + 1
numerator = c.Solver.integrate(lambda x: x*density(x), 0, 5, 1000)
denominator = c.Solver.integrate(density, 0, 5, 1000)
center_of_mass = numerator / denominator
print("Center of mass from 0 to 5:", center_of_mass)
print()

# ---------------- Constants Tests ----------------
print("-> Testing Constants")
print("pi =", c.Constants.pi)
print("e =", c.Constants.e)
print("g =", c.Constants.g)
print("c =", c.Constants.c)
print("h =", c.Constants.h)
print("k =", c.Constants.k)
print()

# ---------------- Physics / Robotics Examples ----------------
print("-> Testing Physics/Robotics Examples")

# Torque
r = c.Vec3(0,2,0)
F = c.Vec3(10,0,0)
torque = r.cross(F)
print("Torque vector:", torque)

# Work
force = c.Vec3(10,0,0)
displacement = c.Vec3(5,0,0)
work = force.dot(displacement)
print("Work done:", work)

# Angle between vectors
v1 = c.Vec3(1,0,0)
v2 = c.Vec3(1,1,0)
cos_theta = v1.dot(v2) / (v1.magnitude() * v2.magnitude())
angle = c.acos(cos_theta)
print("Angle between v1 and v2 (rad):", angle)

# Projectile distance
g = c.Constants.g
velocity = lambda t: 20 - g*t
distance = c.Solver.integrate(velocity, 0, 2, 1000)
print("Projectile distance (2s):", distance)

# Electric field via cross product
velocity_vec = c.Vec3(0,1,0)
magnetic_field = c.Vec3(0,0,1)
electric_field = velocity_vec.cross(magnetic_field)
print("Electric field vector:", electric_field)

print("\n✅ All tests completed successfully!")
```

⏫ This is the Main test code of all the features if calculus other examples given below may or may not work.

## 🧪 Examples

###  Example 1 – Basic Scalar Arithmetic

```python
import calculus as c

x = c.Scalar(5)
y = c.Scalar(3)

print(x + y)
print(x * y)
```
### Example 2: Distance Between Two Points (Robot Movement)

```python
import calculus as c

p1 = c.Vec3(1, 2, 3)
p2 = c.Vec3(4, 6, 3)

distance = (p2 - p1).magnitude()
print("Distance:", distance)
```
📌 Use case:
Robot path planning, obstacle distance calculation

### Example 3: Robot Arm Direction Vector (Normalization)

```python
import calculus as c

direction = c.Vec3(10, 5, 0)
unit_direction = direction.normalize()

print("Unit direction:", unit_direction)
```
📌 Use case:
Motor direction control, inverse kinematics
### Example 4: Work Done by a Force (Physics)

```python
import calculus as c

force = c.Vec3(10, 0, 0)     # Newtons
displacement = c.Vec3(5, 0, 0)  # meters

work = force.dot(displacement)
print("Work done (J):", work)
```
📌 Use case:
Physics engines, mechanical simulations

### Example 5: Torque Calculation (Cross Product)

```python
import calculus as c

r = c.Vec3(0, 2, 0)   # position vector
F = c.Vec3(10, 0, 0)  # force

torque = r.cross(F)
print("Torque vector:", torque)
```

📌 Use case:
Robot joints, rotational mechanics

### Example 6: Projectile Motion – Area Under Velocity Curve

```python
import calculus as c

g = c.Constants.g

velocity = lambda t: 20 - g * t

distance = c.Solver.integrate(
    velocity,
    0,
    2,
    1000
)

print("Distance traveled:", distance)
```

📌 Use case:
Ballistics, drone drop calculations

### Example 7: Center of Mass (Simple 1D Integration)

```python
import calculus as c

mass_density = lambda x: x + 1

numerator = c.Solver.integrate(
    lambda x: x * mass_density(x),
    0,
    5,
    1000
)

denominator = c.Solver.integrate(
    mass_density,
    0,
    5,
    1000
)

center_of_mass = numerator / denominator
print("Center of Mass:", center_of_mass)
```

📌 Use case:
Mechanical design, robotics balance control

### Example 8: Angle Between Two Vectors (Robot Orientation)

```python
import calculus as c

v1 = c.Vec3(1, 0, 0)
v2 = c.Vec3(1, 1, 0)

cos_theta = v1.dot(v2) / (v1.magnitude() * v2.magnitude())
angle = c.acos(cos_theta)

print("Angle (rad):", angle)
```
📌 Use case:
Robot heading, orientation correction

### Example 9: Energy Stored in a Spring

``` python
import calculus as c

k = 100  # spring constant

force = lambda x: k * x

energy = c.Solver.integrate(
    force,
    0,
    0.5,
    1000
)

print("Spring Energy:", energy)
```

📌 Use case:
Shock absorbers, suspension modeling

### Example 10: Gravitational Force Calculation

```python
import calculus as c

G = 6.674e-11
m1 = 5.97e24
m2 = 1000
r = 6.4e6

force = G * m1 * m2 / (r * r)
print("Gravitational force:", force)
```
📌 Use case:
Astro-robotics, satellite simulation

### Example 11: Path Length Using Integration (Robot Trajectory)

```python
import calculus as c

speed = lambda t: (3*t*t + 2*t + 1)

path_length = c.Solver.integrate(
    speed,
    0,
    4,
    1000
)

print("Path length:", path_length)
```
📌 Use case:
Autonomous vehicle motion planning

### Example 11: Electric Field Direction (Cross Product)

```python
import calculus as c

velocity = c.Vec3(0, 1, 0)
magnetic_field = c.Vec3(0, 0, 1)

electric_field = velocity.cross(magnetic_field)
print("Electric field direction:", electric_field)
```
📌 Use case:
Physics simulation, EM field modeling

## 🔫 Trouble shooting
 If the steps parameter is missing, Python will raise:
 ```python
TypeError: integrate(): incompatible function arguments
```
### ✅ Correct Usage (IMPORTANT)
```python
area = c.Solver.integrate(
    lambda x: x * x,
    0,
    3,
    1000   # <-- REQUIRED number of steps
)
```
### ❌ Incorrect Usage
```python
# This will FAIL
c.Solver.integrate(lambda x: x*x, 0, 3)
```

### 📌 Recommendation
Always use at least 1000 steps for accurate results
Steps must be an even number (Simpson’s Rule requirement)
Higher steps = higher accuracy but slower computation

### 🛠 Why This Happens
The integration is implemented in C++ using Simpson’s Rule, which:
Requires a fixed number of subdivisions
Cannot infer the step count automatically
This design ensures high performance and numerical stability.

## 📖Project Wiki
Click[here](https://github.com/LegedsDaD/CalCulus/wiki)
## ⭐Star
Star the repo if you find this helpful for performing HIGH GRADE SCIENTIFIC CALCULATIONS.

tell me which sections to this 
