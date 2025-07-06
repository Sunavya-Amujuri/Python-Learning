
- Expressions are just values combined with operators, and they always evaluate down to a single value.
- A data type is a category for values, and every value belongs to exactly one data type.
- A single value with no operators is also considered an expression, though it evaluates only to itself.
- An indentation is the space after (if, for or Def) statements. Exact 4 spaces are needed for identation to enter manually or use tab for space or automatic space also genrated.
- Convention means single space, but it doesnot affect python, but creates readability.

# 2 + 3 will give 5, also 'alice' + 'bob' gives 'alicebob' , but 'alice' + 45 throws an error.
# 'Alice' * 3 gives 'AliceAliceAlice'
# 'Alice' * 'Bob' and 'Alice' * 5.0 gives an error
- The * operator can be used with only two numeric values (for multiplication), or one string value and one integer value (for string replication). Otherwise, Python will just display an error message.

## Variable :
- A variable is like a box in the computer’s memory where you can store a single value. Also if we give multiple values python automatically takes as a tuple and depending upon values it can also takes into list, set or dictionary automatically.
x = [10, 20, 30]     # A list
y = (1, 2, 3)        # A tuple
z = {"name": "Radha", "age": 22}   # A dictionary

| What You Do      | What Happens                         |
| ---------------- | ------------------------------------ |
| `x = 10, 20, 30` | ✅ `x` becomes a tuple `(10, 20, 30)` |
| `x = 10 20 30`   | ❌ SyntaxError                        |
| `a, b = 10, 20`  | ✅ Multiple variables assigned        |
| `a, b = 10`      | ❌ ValueError: not enough values      |

- Also in variables when a new value is assigned to a variable, the old one is forgotten.
- A good variable name describes the data it contains. You can name your variables almost anything, Python does have some naming restrictions. You can name a variable anything as long as it obeys the following three rules:

It can be only one word with no spaces.
It can use only letters, numbers, and the underscore (_) character.
It can’t begin with a number.

## Function
- A function is a block of code that does a specific task.
- When you tell Python to run (execute) the function, it's called a function call.
- A value that is passed to a function call is an argument.
### Note: You can also use this function to put a blank line on the screen; just call print() with nothing in between the parentheses.

### Note: Note that if you pass a value to int() that it cannot evaluate as an integer, Python will display an error message.
- int('99.99')   throws error.
- The int() function is also useful if you need to round a floating-point number down.
>>> int(7.7)
7     #for float it just ignore all the numbers just after the dot.
- round(7.7)     # Output: 8
round(7.3)     # Output: 7       # if u want rounding approximate use round()

- an integer can be equal to a floating point.

>>> 42 == '42'     #integer equals to string not valid
False
>>> 42 == 42.0     #integer equals to float is valid.
True
>>> 42.0 == 0042.000
True

### Note:
n % 2 == 0	Checks if number is even (divisible by 2)
n % 2 == 1	Checks if number is odd
n % 10	Gives the last digit of a number
n % 100	Gives the last two digits of a number
n // 2  Divides the number by 2 and removes the decimal part.
n // 10 Removes the last digit of the number (or) First part (without last digit)

### Methods

# String methods

| Method              | Description                          | Example                                 |  
 
| `.lower()`          | Converts all characters to lowercase |`"HELLO".lower()` -> `"hello"`           |  
| `.upper()`          | Converts all characters to uppercase |`"hello".upper()` -> `"HELLO"`           |  
| `.capitalize()`     | Capitalizes first character          |`"hello".capitalize()` -> `"Hello"`      |  
| `.title()`          |Capitalizes the 1st char of each word |`"hello world".title()`-> `"Hello World"`|  
| `.strip()`          | Removes leading/trailing whitespace  |`"  hello  ".strip()` -> `"hello"`       |  
| `.lstrip()`         | Removes leading whitespace           |`"  hello".lstrip()` -> `"hello"`        |  
| `.rstrip()`         | Removes trailing whitespace          |`"hello  ".rstrip()` -> `"hello"`        |  
| `.replace(old, new)`| Replaces occurrences of a substring  |`"hello".replace("l", "L")` -> `"heLLo"` |  
| `.find(sub)`        | Finds index of first occurrence      |`"hello".find("l")` -> `2`               |  
| `.startswith(sub)`  |Checks if string starts with substring|`"hello".startswith("h")` -> `True`      |  
| `.endswith(sub)`    | Checks if string ends with substring |`"hello".endswith("o")` -> `True`        |  
| `.split(delimiter)` | Splits string into list       |`"hello world".split()` -> `['hello', 'world']` |  
| `.join(list)`       | Joins list into string with separator|`", ".join(['a', 'b'])` -> `"a, b"`      |  


# List methods

| Method            | Description                              | Example                               |  
 
| `.append(x)`      | Adds element at the end                  | `[1, 2].append(3)` -> `[1, 2, 3]`     |  
| `.insert(i, x)`   | Inserts element at position `i`          | `[1, 3].insert(1, 2)` -> `[1, 2, 3]`  |  
| `.remove(x)`      | Removes first occurrence of `x`          |`[1, 2, 3, 2].remove(2)` -> `[1, 3, 2]`|  
| `.pop([i])`       |Removes and returns element at index `i`(last if not specified)|`[1, 2, 3].pop()` -> `3`, list -> `[1, 2]` |  
| `.clear()`        | Removes all elements                     | `[1, 2].clear()` -> `[]`              |  
| `.sort()`         | Sorts list in place                      | `[3, 1, 2].sort()` -> `[1, 2, 3]`     |  
| `.reverse()`      | Reverses list in place                   | `[1, 2, 3].reverse()` -> `[3, 2, 1]`  |  
|`.extend(iterable)`|Extends list by appending all elements from iterable|`[1, 2].extend([3, 4])` -> `[1, 2, 3, 4]`|            
| `.count(x)`       | Counts occurrences of `x`                | `[1, 2, 2, 3].count(2)` -> `2`        |  
| `.copy()`         | Returns a shallow copy of list           | `list2 = list1.copy()`                |  


# Set methods

| Method              | Description                             | Example                              |  

| `.add(x)`           | Adds element `x`                        | `{1, 2}.add(3)` -> `{1, 2, 3}`       |  
| `.remove(x)`        | Removes element `x`(error if not exists)| `{1, 2}.remove(2)` -> `{1}`          |  
| `.discard(x)`       | Removes element `x` if it exists        | `{1, 2}.discard(2)` -> `{1}`         |  
| `.pop()`            | Removes and returns an arbitrary element|`s ={1, 2}.pop()`-> example`{1}`,`{2}`|  
|`.update(iterable)`  | Adds elements from iterable             |`{1, 2}.update([2, 3])`-> `{1, 2, 3}` |  
| `.union(set2)`      | Returns union of sets                   |`{1, 2}.union({2, 3})` -> `{1, 2, 3}` |  
|`.intersection(set2)`| Intersection of sets                    |`{1, 2}.intersection({2, 3})` -> `{2}`|  
|`.difference(set2)`  | Elements in first set not in second     | `{1, 2}.difference({2, 3})` -> `{1}` |  


# Tuple methods

| Method                      | Description                       | Example                            |  
  
| `.count(x)`                 | Counts how many times `x` appears | `(1, 2, 2).count(2)` -> `2`        |  
| `.index(x[, start[, end]])` | Finds first occurrence of `x`     | `(1, 2, 2).index(2)` -> `1`        | 

# Dictionary methods

| Method                  | Description                                     | Example |  
 
| `.clear()`              |Removes all items from the dictionary |`d ={'a': 1}.clear()`->`d`becomes`{}`|  
| `.copy()`               |Returns a shallow copy of the dictionary         | `d2 = d1.copy()`         |  
|`.fromkeys(seq, value)`  | Creates a new dictionary from a sequence of keys, with all values set to `value` | `dict.fromkeys(['a', 'b'], 0)` -> `{'a':0, 'b':0}` |  
| `.get(key, default)`    | Returns the value for `key`, or `default`       | `d.get('a', 0)`          |  
                                if key not found 
| `.items()`              | Returns a view object of key-value pairs        | `d.items()`              |  
| `.keys()`               | Returns a view object of all keys               | `d.keys()`               |  
|`.pop(key, default)`     | Removes and returns the value for `key`;        | `d.pop('a', 0)`          |  
                               returns `default` if `key` not found 
| `.popitem()`            | Removes and returns an arbitrary key-value pair | `d.popitem()`            |  
|`.setdefault(key,default)`| Returns the value of `key`. If `key` is        | `d.setdefault('a', 0)`   |  
                               missing, inserts it with value `default` 
| `.update(other)`        | Updates the dictionary with key-value pairs     | `d.update({'b': 2})`     |  
                            from `other` or iterable
| `.values()`             | Returns a view object of all values             | `d.values()`             |  

# Python's built-in functions (not methods)
In addition to data type methods, Python also has many built-in functions that work on data types or are useful in general. Some examples:

len() (gets length)
sorted() (returns sorted list)
enumerate() (iterates with index)
filter(), map(), reduce()
zip()
type()
isinstance()
sum(), min(), max()


String       : 13 methods
List         : 11 methods
Set          : 9 methods
Tuple        : 2 methods
Dictionaries : 11 methods


| Method    |Collection Type| What it does                             | Can it add duplicates?       |  

| `.add()`  | **set**       | Adds a single element to the set.        |**No**; duplicates are ignored|  
|`.append()`| **list**      |Adds single element to the end of the list|**Yes**;duplicates allowed.   |  


| Bracket Type | Name             | Common Uses                                    |  
| `( )`        | Parentheses      | Tuples, function calls, grouping               |  
| `[ ]`        | Square brackets  | Lists, indexing, slicing                       |  
| `{ }`        | Curly braces     | Dictionaries, sets, set literals               |  
| `< >`        | Angle brackets   | Not standard in Python, used in other contexts |  

# To check for prime number
- Checking up to sqrt(num) is enough to determine if num is prime or composite.
- No need to check beyond sqrt(num) because any larger factor would have a corresponding smaller factor already checked.
-  If at any point num % i == 0 is True, it means:
i divides num, so num cannot be prime.
There's no need to continue checking other values of i, because we've already proven num isn't prime.
- No unneccesary checks even after proven and makes the code efficient.

### Note: 
| Feature              | `while` loop      | `for` loop              |

| Need to declare `i`? | ✅ Yes            | ❌ No (Python handles)  |
| Loop control         | Manual (`i += 1`)  | Automatic via `range()` |

| Type            | Used to Add         | Example Code                          |
| ----------------| ------------------- | ------------------------------------- |
| `list` a = []   | `.append(item)`     | `my_list.append(5)`                   |
| `dict` freq = {}| `+= 1` / assignment | `freq[char] += 1` or `freq[char] = 1` |


## Functions
A function is a reusable block of code that performs a specific task.
Instead of writing the same code again and again, we can write it once inside a function and call it whenever needed.

| Type                       | Example                          |
| -------------------------- | -------------------------------- |
| **Built-in Functions**     | `len()`, `print()`, `type()`     |
| **User-defined Functions** | Functions you create using `def` |

Parameter → Variable listed in function definition
(like a, b in def add(a, b))

Argument → Actual value passed when calling the function
(like 5, 3 in add(5, 3))

# Return Statement:
The return keyword is used to send a result back to the caller.

keyword arguments and positional arguments are ways to pass values to functions.

# Positional Arguments
- The arguments are assigned based on their position in the function call.
- The order matters.
# Keyword Arguments
- Arguments are assigned based on the parameter's name.
- The order doesn't matter, since you specify which parameter you're assigning.

# Variable Scope
- The scope of a variable defines where in the code the variable can be accessed or modified.
- Variables can have local scope (only within a function), or global scope (accessible throughout the program).
# Global Scope
- Variables declared outside of functions.
- Can be accessed or modified from anywhere in the code, including inside functions (using the global keyword if you want to modify the global variable).

# Lambda Functions
- Lambda functions, also called anonymous functions, are small, one-line functions that are defined without a formal def statement.
- They are useful for short, simple operations where defining a full function might be unnecessary.
 ## lambda arguments: expression

# Understanding map() and list():
- map() itself does not return a list; it returns a map object, which is an iterator.
- To see all the results at once, you typically convert this iterator into a list (or another collection type) using list()
- When you need a quick, throwaway function.
Often used with functions like map(), filter(), sorted(), etc.

## Why use *args and **kwargs?
1. Handling an unknown number of arguments
Sometimes, you don't know in advance how many arguments your function will receive.
For example, summing any number of values or passing a flexible set of options.
2. Creating highly flexible functions
Functions using *args and **kwargs can accept multiple optional parameters.
Useful for functions with default behaviors, customizable options, or plugins.
3. Forwarding arguments
When inheriting or wrapping functions, you can forward additional arguments dynamically.
This is common in decorators or wrapper functions.
## Simplified analogy:
Using fixed arguments: like going shopping with a specific list.
Using *args and **kwargs: like shopping with a flexible shopping list that can change.

# Additional_info: 
- Additional_info is a dictionary containing extra keyword arguments passed to the function.
- The name helps clarify what kind of data or purpose the arguments serve.

# Armstrong Numbers
- An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

# Generator Expression
- A generator expression is a short, memory-efficient way to create iterators — similar to list comprehensions, but without creating the entire list in memory.
## (expression for item in iterable if condition)

| Feature                | `.sort()`                       | `sorted()`                           |  
  
| Method or Function     | List method                     | Built-in function                    |  
| Modifies original list | Yes                             | No                                   |  
| Returns                | `None`                          | New sorted list                      |  
| Use case               | When you want to sort a list in place | When you need a sorted copy of any iterable |  

# Note:
- float('-inf') is the most straightforward way to represent the smallest value and is widely used.
- Alternative: Use None for a more explicit "not set" indicator.
- Both methods work, but using float('-inf') is common for numeric comparisons.

- ✔ If second != -inf,
→ it means we found a real second-largest number.

❌ If second == -inf,
→ it means we never updated second from -inf, so:

Either all numbers were the same, or There was only one unique number.


## Note: In both factorial and Fibonacci, we manually write the stop condition in recursion (called the base case).

- In factorial, we stop at n <= 1/n == 1 and return 1, because 0! and 1! are both 1 by rule.

- In Fibonacci, we stop at n <= 1 and return n itself, because fibonacci(0) = 0 and fibonacci(1) = 1.


| Feature    | List               | Set             | Tuple               |  Dictionary             |
| ---------- | -------------------| ----------------| ------------------- |------------------------ |
| Ordered    | ✅ Yes             | ❌ No          | ✅ Yes             |✅ Yes (Python 3.7+)     |
| Mutable    | ✅ Yes             | ✅ Yes         | ❌ No              | ✅ Yes                  |
| Duplicates | ✅ Allowed         | ❌ Not allowed | ✅ Yes             | ❌ Keys not duplicated   |
| Indexed    | ✅ Yes (0-based)   | ❌ No          | ✅ Yes             | ❌ No (use keys instead) |
| Syntax     | `[1, 2, 3]`        | `{1, 2, 3}`     | (1, 2, 3)           |`{"a": 1, "b": 2}`       |
| Use Case   | Sequence of items  | Unique items    |Fixed groups of data |Key-value paired data    |


# Lambda function: 
- Lambda is used when you need a simple function for a short time.

| Feature        | Lambda Function                         |
| -------------- | --------------------------------------- |
| Name           | Anonymous (no `def`)                    |
| Return keyword | Not used (automatically returns)        |
| Syntax         | `lambda args: expression`               |
| Limitation     | Only one expression (no multiple lines) |
| Used with      | `map()`, `filter()`, `sorted()`, etc.   |

- Some built-in functions in lambda, to work efficiently on lists or sequences.


| Function   | Purpose                           | Works with         | Example with Lambda          |
| ---------- | --------------------------------- | -------------------| -----------------------------|
| `map()`    | Transform each item               | List, Tuple        | `map(lambda x: x+1, nums)`   |
| `filter()` | Keep items that satisfy condition | List, Set          | `filter(lambda x: x>5, nums)`|
| `sorted()` | Sort items                      | List, Tuple (not Set)|`sorted(list, key=lambda x: x[1])`|

# List Comprehension
- A list comprehension is a short and cleaner way to create a new list by applying an operation or condition on an existing iterable (like list, range, etc.).
- Instead of using a for loop, we write the entire logic in one line.

| Feature  | List Comprehension                               |
| -------- | ------------------------------------------------ |
| Syntax   | `[expression for item in iterable if condition]` |
| Purpose  | Short way to create lists from other iterables   |
| Benefits | Cleaner, faster, readable                        |
| Example  | `[x for x in range(10) if x % 2 == 0]`           |

# Set Comprehension
- Set comprehension is a compact way to create a set by applying logic to an iterable.

| Feature         | **List Comprehension**                   | **Set Comprehension**                 |
| --------------- | ---------------------------------------- | ------------------------------------- |
| **Result Type** | List (allows duplicates, ordered)        | Set (no duplicates, unordered)        |
| **Syntax**      | `[expression for item in iterable]`      | `{expression for item in iterable}`   |
| **Duplicates**  | ✅ Allowed                              | ❌ Removed automatically              |
| **Order**       | ✅ Maintains original order             | ❌ Unordered (no guaranteed order)    |
| **Indexing**    | ✅ Yes (can use list\[0], list\[1]...)  | ❌ No indexing                        |
| **Use Case**    | When you need a sequence, ordered data   | When you want only unique values      |
| **Performance** | Slightly slower if you check for uniques | Faster lookup, as sets are hash-based |
| **Mutable?**    | ✅ Yes (you can modify it later)        | ✅ Yes (you can add/remove later)     |


| ✅ Use **List Comprehension** when: |  ✅ Use **Set Comprehension** when:           |   
| ----------------------------------  | ---------------------------------------------- |
| You need to **preserve order**      | You want **only unique items**                 |
| You want to **allow duplicates**    | You **don’t care about order**                 |
| You want to use **indexing** later  | You want to **avoid duplicates automatically** |


# Dictionary Comprehension
- A dictionary comprehension is a short and powerful way to create dictionaries using a single line of code.
- It's similar to list and set comprehension, but instead of just values, you provide both:
  1) a key
  2) and a value

- syntax : {key_expr: value_expr for item in iterable if condition}

-  It is used when you want to:
| Purpose                                                  | Example                                  |
| -------------------------------------------------------- | ---------------------------------------- |
| 🔹 Create a dictionary from a list or range              | Create `{x: x**2}` from numbers          |
| 🔹 Filter and transform data while building a dictionary | Keep only even numbers as keys           |
| 🔹 Swap keys and values in a dictionary                  | Convert `{"a": 1}` to `{1: "a"}`         |
| 🔹 Clean or format dictionary data                       | Capitalize all values, remove empty ones |
| 🔹 Merge, map, or manipulate items during creation       | Build dictionary with condition          |


###  What is a Pattern in Programming?
A pattern program is a type of code that prints shapes or sequences like:
- * (stars)
- Numbers (123, 321)
- Alphabets (A, AB, ABC)
- Shapes like triangles, squares, diamonds

# These are output-based logic programs that use:
- for loops (sometimes nested)
- range(), print()
- Math and string formatting

🎯 Why Are Pattern Programs Important?
Reason	                                 Explanation
🧠 Improve logic & thinking	            You learn to break down complex visuals into code
🧮 Master loops & conditions	        You’ll gain deep control over for, while, range()
💼 Asked in interviews	                Often asked in Python/C/Java coding rounds
🧪 Builds foundation for algorithms	    Recursion, matrix logic, and game logic
🚀 Builds confidence to solve unknowns	You’ll start visualizing how code becomes output

Real-World Use of Pattern Logic
Even though we don’t print stars in real-world projects, the logic you use in patterns is used in real scenarios:

🔸 1. Frontend UI & Games
- Rendering shapes and grids
- Snake game / tic-tac-toe / maze patterns

🔸 2. Matrix/Array problems
- Data visualization
- Image representation in AI
- Board games or simulations

🔸 3. Data structures
- Understanding loops inside loops (used in 2D lists, graphs, trees)
- Designing output or reports in structured format

🔸 4. Competitive coding
- Almost all coding contests include 1–2 pattern-style problems
- Helps you in TCS, Infosys, Wipro, Cognizant, etc.

🔸 5. Recursion & Backtracking
- Understanding symmetric, repeating, and layered structures
- Basis for solving puzzles like Sudoku, N-Queens, etc.

Final Thought: Pattern Programs = Visual Logic Building
You're not just printing stars — you're training your mind to:
- Visualize
- Translate that into steps
- And write loop logic to make it real 💻

| Category                         | Estimated Patterns |
| -------------------------------- | ------------------ |
| ⭐ Star patterns                 | 10–12              |
| 🔢 Number patterns               | 10–12              |
| 🔠 Alphabet patterns             | 5–7                |
| ⏹ Shape patterns (diamond, etc.) | 5–7                |
| 🧠 Logical mixed patterns        | 5–6                |

# ⭐ Star patterns

| #  | Pattern Type                 | Example Shape              |
| -- | ---------------------------- | -------------------------- |
| 1  | Square of Stars              | `*****`                    |
| 2  | Left-Aligned Triangle        | `*`, `**`, `***`           |
| 3  | Right-Aligned Triangle       | Spaced triangle            |
| 4  | Inverted Triangle (left)     | `****`, `***`              |
| 5  | Inverted Triangle (right)    | Spaced inverted            |
| 6  | Pyramid (centered)           | Symmetric rows             |
| 7  | Inverted Pyramid             | Centered down              |
| 8  | Diamond Shape                | Pyramid + inverted         |
| 9  | Hollow Square                | Stars only on border       |
| 10 | Hollow Triangle              | Stars on sides             |
| 11 | Hollow Pyramid               | Border stars only          |
| 12 | Half Diamond (upper + lower) | `*`, `**`, then `*`        |
| 13 | Right Half Diamond (spaced)  | Angled half-diamond        |
| 14 | Butterfly Pattern            | 2 halves mirrored          |
| 15 | Hourglass Pattern            | Inverted + upright pyramid |
| 16 | X Pattern                    | `*` crosses like an X      |
| 17 | Plus (+) Pattern             | Cross shape with `*`       |
