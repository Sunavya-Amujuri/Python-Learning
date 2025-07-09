// 1. Linear search Algorithm.

// # include <iostream>
// using namespace std;

// int linearsearch(int arr[], int size, int target) {
//     for (int i=0; i<size; i++) {
//         if (arr[i] == target) {
//             return i;
//         }
//     }
//     return -1;
// }

// int main() {
//     int arr[] = {4, 2, 7, 8, 1, 2, 5};
//     int size = 7;
//     int target = 50;

//     cout << linearsearch(arr, size, target) << endl;
//     return 0;
// }


// 2. Reverse an array, using 2 pointer approach.

// # include <iostream>
// using namespace std;

// void reverseArray(int arr[], int size) {
//     int start = 0, end = size-1;

//     while (start < end) {
//         swap(arr[start], arr[end]);
//         start++;
//         end--;
//     }
// }

// int main() {
//     int arr[] = {4, 2, 7, 8, 1, 2, 5};
//     int size = 7;

//     reverseArray(arr, size);
//     for (int i=0; i<size; i++) {
//         cout << arr[i] << " ";
//     }
//     cout << endl;
//     return 0;
// }


// 3. Pass by value and Pass by reference value.

// #include <iostream>
// using namespace std;

// // Pass by Value
// void byValue(int x) {
//     x = x + 5;
//     cout << "Inside byValue: " << x << endl;  // Output: 15
// }

// // Pass by Reference
// void byReference(int &x) {
//     x = x + 5;
//     cout << "Inside byReference: " << x << endl;  // Output: 15
// }

// int main() {
//     int a = 10;

//     byValue(a);
//     cout << "After byValue: " << a << endl;       // Output: 10 (not changed)

//     byReference(a);
//     cout << "After byReference: " << a << endl;   // Output: 15 (changed)
// }


// 4. Linear search using vector

// # include <iostream>
// # include <vector>
// using namespace std;

// int linearsearch(vector<int> &vec, int target) {
//     for (int i=0; i<vec.size(); i++) {
//         if (vec[i] == target) {
//             return i;
//         }
//     }
//     return -1;
// }

// int main() {
//     vector<int> numbers= {4, 2, 7, 8, 1, 2, 5};
//     int target;

//     cout << "Enter a number: ";
//     cin >> target;

//     cout << linearsearch(numbers, target);
//     return 0;
// }


// 5. Brute Force Approach (Maximum subarray sum).

// # include <iostream>
// using namespace std;

// int main() {
//     int n = 6;
//     int arr[] = {1, 3, 5, 2, 3, -1};
//     int maxsum = INT_MIN;

//     for(int st=0; st<n; st++) {
//         int currsum = 0;
//         for(int end=st; end<n; end++) {
//             currsum += arr[end];
//             maxsum = max(currsum, maxsum);
//         }
//     }
//     cout << "Maximum subarray sum= " << maxsum << endl;
//     return 0;
// }


// 6. Kadane's Algorithm. (Maximum subarray sum optimized way).

// # include <iostream>
// # include <vector>
// using namespace std;

// int maxSubArray(vector<int> &nums) {
//     int currsum = 0, maxsum = INT_MIN;

//     for (int val : nums) {
//         currsum += val;
//         maxsum = max(currsum, maxsum);
//         if (currsum < 0) {
//             currsum = 0;
//         }
//     }
//      return maxsum;   
// }

// int main() {
//     vector<int> nums = {3, -4, 5, 4, -1, 7, -8};

//     cout << "Maximum subarray sum = " << maxSubArray(nums) << endl;
//     return 0;
// }

// 7. Pair sum.

# include <iostream>
# include <vector>
using namespace std;

vector<int> pairSum(vector<int> &nums, int target) {
    vector<int> ans;
    int n = nums.size();

    for(int i=0; i<n; i++) {
        for (int j=i+1; j<n; j++) {
            if (nums[i] + nums[j] == target) {
                ans.push_back(i);
                ans.push_back(j);
                return ans;
            }
        }
    }
    return {};
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    vector<int> ans = pairSum(nums, target);
    if (!ans.empty()) {
        cout << ans[0] << ", " << ans[1] << endl;
    } else {
        cout << "No valid pair found." << endl;
    }
    return 0;
}


