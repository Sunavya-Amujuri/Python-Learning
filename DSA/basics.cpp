// 1. Random basic program.

// #include <iostream>
// using namespace std;

// int main() {
//     int age = 23;
//     char grade = 'a';
//     float PI = 3.14;
//     bool issafe = false;
//     double price = 100.99;
    
//     cout << price;
//     return 0;
// }

// 2. Simple operation

/* #include <iostream>
using namespace std;

int main() {
    double num1, num2;
    char operation;

    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter an operator(+, -, *, /): ";
    cin >> operation;

    cout << "Enter second number: ";
    cin >> num2;

    switch (operation) {
        case '+':
            cout << "Result is: " << num1 + num2 << endl;
            break;
        case '-':
            cout << "Result is: " << num1 - num2 << endl;
            break;
        case '*':
            cout << "Result is: " << num1 * num2 << endl;
            break;
        case '/':
            if (num2 != 0)
                cout << "Result is: " << num1 / num2 << endl;
            else
                cout << "Error: Your division cannot be a 0!" << endl;
            break;
        default:
            cout << "Invalid Operator" << endl;
        }
    return 0;
    
} */

// 3. Vote capability

// #include <iostream>
// using namespace std;

// int main() {
//     int age;
//     cout << "Enter an age: ";
//     cin >> age;

//     if (age >= 18) {
//         cout << "You can vote\n";
//     } else {
//         cout << "You are not eligible.";
//     } 
//     return 0;
// }

// 4. whether the letter is lower or upper character.

// #include <iostream>
// using namespace std;

// int main() {
//     char ch;
//     cout << "Give char: ";
//     cin >> ch;

//     if (ch >= 'a' && ch <= 'z') {
//         cout << "Lower case.\n";
//     } else {
//         cout << "Upper case.";
//     }
//     return 0;
// }

// 5. patterns

// # include <iostream>
// using namespace std;

// int sumN(int n) {
//     int sum = 0;

//     for (int i=1; i<=n; i++) {
//         sum += i;
//     }
//     return sum;
// }

//     int main() {
//         cout << sumN(5) << endl;
//         cout << sumN(10) << endl;
//         return 0;
//     }

// 6. Sum of digits

// # include <iostream>
// using namespace std;

// int sumOfDigits(int num) {
//     int sum = 0;
    
//     while (num > 0) {
//         int lastdigit = num % 10;
//         num /= 10;
//         sum += lastdigit;
//     }
//     return sum;
// }

// int main() {
//     int number;
//     cout << "Give a number: ";
//     cin >> number;

//     cout << "Sum of digits = " << sumOfDigits(number);
//     return 0;
// }

// 7. Decimal to Binary

// # include <iostream>
// using namespace std;

// int decToBinary(int decNum) {
//     int ans = 0, pow = 1;

//     while (decNum > 0) {
//         int rem = decNum % 2;
//         decNum /= 2;

//         ans += (rem * pow);
//         pow *= 10;
//     }
//     return ans;
// }

// int main() {
//     int decNum = 50;
    
//     cout << decToBinary(decNum) << endl;

//     return 0;
// }


// 8. Basic bitwise opearator.

// # include <iostream>
// using namespace std;

// int main() {
//     int a = 4, b = 8;

//     cout << (a & b) << endl;
//     return 0;
// }

// 9. How to find if a number is power of 2.

// # include <iostream>
// using namespace std;

// bool isPowerOf2(int n) {
//     return (n>0 && ((n & (n-1)) == 0));
// }

// int main() {
//     int num = 0;
//     cout << "Enter a number: ";
//     cin >> num;

//     if (isPowerOf2(num))
//         cout << num << " is a power of 2.";
//     else
//         cout << num << " is not a power of 2.";

//     return 0;
// }

// 10. Find smallest in an array.

// # include <iostream>
// #include <climits>
// using namespace std;

// int main() {
//     int nums[] = {5, 15, 22, 1, -15, 24};
//     int size = 6;
    
//     int smallest = __INT_MAX__;   // #include <climits>
//     int largest = INT_MIN;

//     for (int i=0; i<size; i++) {
//         // smallest = min(nums[i], smallest);
//         if (nums[i] < smallest)
//         smallest = nums[i];
//         largest = max(nums[i], largest);
//     }
//     cout << "Smallest num = " << smallest << endl;
//     cout << "Largest num = " << largest << endl;
//     return 0;
// }

// 11. write a function to get index of a smallest number.

// # include <iostream>
// #include <climits>
// using namespace std;

// int getIndexOfSmallestNum(int arr[], int size) {
//     int smallest = INT_MAX;
//     int index = -1;

//     for (int i = 0; i < size; i++) {
//         if (arr[i] < smallest) {
//             smallest = arr[i];
//             index = i;
//         }
//     }
//     return index;
// }

// int main() {
//     int nums[6] = {5, 15, 22, 1, -15, 24};
//     int size = 6;

//     int index = getIndexOfSmallestNum(nums, size);
//     cout << "Index of smallest number : " << index;
//     return 0;
// }

// or

// # include <iostream>
// #include <climits>
// using namespace std;

// int main() {
// int nums[] = {5, 15, 22, 1, -15, 24};
// int size = 6;
// int index = -1;

// int smallest = __INT_MAX__; 
//     for (int i=0; i<size; i++) {
//         if (nums[i] < smallest) {
//             smallest = nums[i];
//             index = i;
//         }
//     }

// cout << "index = " << index << endl;
// return 0;
// }

// 12. Write a function to calculate sum of all numbers in an array.

// # include <iostream>
// using namespace std;

// void sumOfArray(int arr[], int size, int &sum) {
//     sum = 0;

//     for (int i=0; i<size; i++) {
//         sum += arr[i];
//     }
// }

// int main() {
//     int arr[] = {1, 3, 5, 2, 4};
//     int size = 5;
//     int sum;
    
//     sumOfArray(arr, size, sum);
//     cout << "sum = " << sum;
   
//     return 0;
// }


// 13. Write a function to calculate product of all numbers in an array.

// # include <iostream>
// using namespace std;

// void productOfArray(int arr[], int size, int &product) {
//     product = 1;

//     for (int i=0; i<size; i++) {
//         product *= arr[i];
//     }
// }

// int main() {
//     int arr[] = {1, 2, 3, 4, 5};
//     int size = 5;
//     int product;

//     productOfArray(arr, size, product);
//     cout << "Product = " << product << endl;
//     return 0;
// }


// 14.Write a function to swap the max and min number of an array.

// # include <iostream>
// using namespace std;

// void swappingMaxAndMinNum(int arr[], int size) {
//     int maxindex = 0, minindex = 0;

//     for (int i=0; i<size; i++) {
//         if (arr[i] > arr[maxindex]) {
//             maxindex = i;
//         }
//          if (arr[i] < arr[minindex]) {
//             minindex = i;
//         }

//     }
//     swap(arr[maxindex], arr[minindex]);
// }

// int main() {
//     int arr[] = {1, 5, 8, 12, 24, 15};
//     int size = 6;

//     swappingMaxAndMinNum(arr, size);
//     for (int i=0; i<size; i++){
//         cout << arr[i] << " ";
        
//     }
//     cout << endl;
//     return 0;
// }


// 15. Write a function to print all the unique values in an array.

// # include <iostream>
// using namespace std;

// void findUniqueValues(int arr[], int size) {
//     for(int i=0; i<size; i++) {
//         int count = 0;

//         for (int j=0; j<size; j++) {
//             if (arr[i] == arr[j]) {
//                 count++;    
//             }
//         }
//         if (count == 1) {
//             cout << arr[i] << " ";
//         }
//     }
//     cout << endl;
// }

// int main() {
//     int arr[] = {1, 2, 3, 1, 2, 3, 4, 5, 7};
//     int size = 9;

    
//     cout << "Unique Values are: ";
//     findUniqueValues(arr, size);
//     return 0;
// }

// 16. Write a function to print intersection of 2 arrays.

// # include <iostream>
// using namespace std;

// void printIntersectionOfArrays(int arr1[], int arr2[], int size1, int size2) {

//     for(int i=0; i<size1; i++) {
//         for(int j=0; j<size2; j++) {
//             if (arr1[i] == arr2[j]) {
//                 cout << arr1[i] << " ";
//                 break;
//             }
//         }
//     }
// }

// int main() {
//     int arr1[] = {1, 2, 4, 5};
//     int size1 = 4;
//     int arr2[] = {1, 2, 3, 7};
//     int size2 = 4;
     
//     cout << "Intersection values are: ";
//     printIntersectionOfArrays(arr1, arr2, size1, size2);
//     return 0;
    
// }


// 17. Reverse code using vectors

// # include <iostream>
// # include <vector>
// using namespace std;

// void reversecode(vector<int> &vec) {
//     int start = 0, end = vec.size()-1;

//     while (start<end) {
//         swap(vec[start], vec[end]);
//         start++;
//         end--;
//     }

// }
// int main() {
//     vector<int> numbers = {1, 4, 5, 2, 8};
    
//     reversecode(numbers);
//     for(int i=0; i<numbers.size(); i++) {
//         cout << numbers[i] << " ";
//     }
//     cout << endl;
//     return 0;
// }


// 18. Maximum subarray sum.

// # include <iostream>
// using namespace std;

// int main() {
//     int n = 5;
//     int arr[5] = {1, 2, 3, 4, 5};

//     for (int st=0; st<n; st++) {
//         for (int end=st; end<n; end++) {
//             for (int i=st; i<=end; i++) {
//                 cout << arr[i];
//             }
//             cout << " ";
//         }
//         cout << endl;
//     }
//     return 0;
// }


// 19. 




   
