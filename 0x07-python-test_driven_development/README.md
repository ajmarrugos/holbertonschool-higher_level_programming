## Python Test-Driven Development

### Doctest

- Creating basic example functions to test in python with Doctest
- A given .txt file will serve as input to give test cases
- The docstrings will give inputs in the comments to try as test cases

Use:

    python3 -m doctest -v ./tests/"testfile.txt"

    Tail -2 will help to give the last 2 output lines of the log 

### Unittest