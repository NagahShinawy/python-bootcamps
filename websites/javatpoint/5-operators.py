"""
The operator can be defined as a symbol which is responsible for a particular operation between two operands. Operators are the pillars of a program on which the logic is built in a specific programming language. Python provides a variety of operators, which are described as follows.

Arithmetic operators
Comparison operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators
"""

# 1- Arithmetic operators ( + , _ , * , / , //, **, %)
# add +

print(5 + 6)

# sub -
print(10 - 3)

#  Multiplication

print(4 * 3)

# divide

print(20 / 4)  # 5.0


duration = 70

# floor division
months = 70 // 30

# reminder
days = 70 % 30

print("Months", months)
print("Days", days)


# ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ######

print("#" * 50)

# 2- Comparison operators (==, >, <, !=, <=, >=)
# Comparison operators are used to comparing the value of the two operands
# and returns Boolean true or false accordingly.

UNDERAGE = 18
MAX_SPEED = 120

age = 23
speed = 140
print(20 > UNDERAGE)

if age < 18 or speed > 120:
    print("Capture")

PENDING = "Pending"
APPROVED = "Approved"
REJECTED = "Rejected"
STATUS = (PENDING, APPROVED, REJECTED)

user_status = REJECTED

if user_status != REJECTED:
    print("Allow to pass")

else:
    print("Not allow to enter")


# # ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ######

print("#" * 50)

# 3- Assignment Operators ( =, +=, -=, *=, /=, //=, **=)

salary = 1000

salary += 500

print(salary)  # 1500 ==> means : new salary = old salary + 500


# # ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ######

print("#" * 50)

"""
The bitwise operators perform bit by bit operation on the values of the two operands. Consider the following example.
&, |,  ^, ~, << left shift, >> right shift
 
"""

"""
if a = 7   
   b = 6     
then, binary (a) = 0111    
    binary (b) =   0110    
    
hence, a & b = 0011    
      a | b = 0111    
             a ^ b = 0100    
       ~ a = 1000
"""

print(~1)  # -2


# # ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ######

print("#" * 50)


"""
Logical Operators
The logical operators are used primarily in the expression evaluation to make a decision.
Python supports the following logical operators.
and, or, not, 
"""


FEMALE = "female"
PREGNANT = "pregnant"

user = "female"
status = "pregnant"

if user == FEMALE and status == PREGNANT:
    print("Show Female Profile")


# # ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ######

print("#" * 50)

# priority (Precedence)


"""
**	The exponent operator is given priority over all the others used in the expression.
~ + -	The negation, unary plus, and minus.
* / % //	The multiplication, divide, modules, reminder, and floor division.
+ -	Binary plus, and minus
>> <<	Left shift. and right shift
&	Binary and.
^ |	Binary xor, and or
<= < > >=	Comparison operators (less than, less than equal to, greater than, greater then equal to).
<> == !=	Equality operators.
= %= /= //= -= +=
*= **=	Assignment operators
is is not	Identity operators
in not in	Membership operators
not or and	Logical operators
"""

"""
Identity Operators

The identity operators are used to decide whether an element certain class or type.

- if obj is immutable(tuple, str, int , ..) ==> the same obj reference
- if obj mutable (list, dict, ..) ==> NOT THE SAME REFERENCE
"""

backend_salary = 1000
frontend_salary = 1000

names = []
emails = []

print(backend_salary is frontend_salary)  # True  => because string is immutable
print(names is emails)  # False  => because list is mutable


# priority (Precedence)


"""
**	The exponent operator is given priority over all the others used in the expression.
~ + -	The negation, unary plus, and minus.
* / % //	The multiplication, divide, modules, reminder, and floor division.
+ -	Binary plus, and minus
>> <<	Left shift. and right shift
&	Binary and.
^ |	Binary xor, and or
<= < > >=	Comparison operators (less than, less than equal to, greater than, greater then equal to).
<> == !=	Equality operators.
= %= /= //= -= +=
*= **=	Assignment operators
is is not	Identity operators
in not in	Membership operators
not or and	Logical operators
"""