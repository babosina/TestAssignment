# Python Practice Problems Repository

A collection of programming problems and their solutions in Python, designed for learning and interview preparation.

## 📋 Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Running Tests](#running-tests)

## 🎯 Overview

This repository contains solutions to common programming problems that frequently appear in:

- Technical interviews
- Coding challenges
- Algorithm and data structure practice
- Programming contests

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/babosina/TestAssignment.git
cd TestAssignment
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (if any):

```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

### Run all tests:

```bash
python -m pytest
```

### Run tests with coverage:

```bash
python -m pytest --cov=. --cov-report=html
```

### Example Solution Format:

```python
def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers in the array that add up to the target sum.
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List containing indices of the two numbers
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    # Implementation here
    pass
```

## 📈 Difficulty Levels - in progress

[//]: # (Problems are categorized by difficulty:)

[//]: # (- 🟢 **Easy**: Basic problems, good for beginners)

[//]: # (- 🟡 **Medium**: Intermediate problems requiring some algorithmic thinking)

[//]: # (- 🔴 **Hard**: Advanced problems, often seen in competitive programming)

- [LeetCode](https://leetcode.com/) - Online platform for coding practice
- [HackerRank](https://www.hackerrank.com/) - Programming challenges and tutorials
- [GeeksforGeeks](https://www.geeksforgeeks.org/) - Computer science portal
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/) - Time and space complexity reference

**Happy Coding! 🚀**

Remember: The goal is not just to solve problems, but to understand the underlying concepts and improve your
problem-solving skills.