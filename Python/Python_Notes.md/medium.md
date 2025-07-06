## built-in modules and features that go beyond basic data types like list, set, tuple, and dict.

# 1) Collections
- collections is a built-in Python module that provides specialized data types beyond the basic list, dict, set, and tuple.

- These data types help you write cleaner, faster, and more efficient programs.

| Name          | Description                                               |
| ------------- | --------------------------------------------------------- |
| `Counter`     | Counts frequency of elements (like characters, words)     |
| `defaultdict` | Dictionary with default values                            |
| `OrderedDict` | Keeps dictionary items in the order they were added       |
| `deque`       | Double-ended queue (fast appending/removing on both ends) |
| `namedtuple`  | Tuple with named fields (like an object with attributes)  |

# 2) Heapq
- Heapq is a Python module used to implement the heap queue algorithm (a.k.a. priority queue).
It lets you work with a list like a min-heap — where the smallest element is always at the top.

- A heap is a special tree-based data structure that satisfies the heap property:

Min-Heap: parent node ≤ children → smallest element is at the top

Max-Heap: parent node ≥ children → largest element is at the top (Python doesn’t support it directly, but we can trick it)

Python’s heapq only supports min-heaps by default.

| Function                  | What it does                                |
| ------------------------- | ------------------------------------------- |
| `heapify(list)`           | Converts a normal list into a min-heap      |
| `heappush(heap, item)`    | Adds an item to the heap and reorders       |
| `heappop(heap)`           | Removes and returns the smallest item       |
| `heappushpop(heap, item)` | Push and pop in one step (faster)           |
| `heapreplace(heap, item)` | Pop and push (but slightly different logic) |