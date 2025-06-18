
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


