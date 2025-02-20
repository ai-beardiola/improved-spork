from fb import fizz_buzz
# Usage instructions: To call fizz_buzz, type fizz_buzz(3) (Don't forget to print as well!)
 # Write your tests below:
print(fizz_buzz(3))

print(fizz_buzz(5))

print(fizz_buzz(1.5))

print(fizz_buzz(15))  

print(fizz_buzz(1)) 
# Write your drill-down code here:

try:
    assert fizz_buzz(3) == "Fizz", "Did not get 'Fizz' for fizz_buzz(3)"
except AssertionError as error:
    print(f"Fail: {error}")


try:
    assert fizz_buzz(5) == "Buzz", "Did not get 'Buzz' for fizz_buzz(5)"
except AssertionError as error:
    print(f"Fail: {error}")


try:
    assert fizz_buzz(1.5) == "Invalid input", "Did not get error message for fizz_buzz(1.5)"
except AssertionError as error:
    print(f"Fail: {error}")


try:
    assert fizz_buzz(15) == "FizzBuzz", "Did not get 'FizzBuzz' for fizz_buzz(15)"
except AssertionError as error:
    print(f"Fail: {error}")


try:
    assert fizz_buzz(1) == 1, "Did not get 1 for fizz_buzz(1)"
except AssertionError as error:
    print(f"Fail: {error}")
