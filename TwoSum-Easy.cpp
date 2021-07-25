#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> nums{ 2, 7, 11, 15 };
vector<int> output{0, 0};
int target = 9;
int diff;
vector<int> twoSum(vector<int>& nums, int target) 
{   
    for (int i = 0; i < nums.size(); i++)
    {
        diff = target - nums[i];
        cout << "Searching for: " << diff << endl;

        auto search = find(nums.begin(), nums.end(), diff);

        if (search != nums.end()) {
            int index = search - nums.begin();
            cout << "Found " << diff << " at index " << index << endl;
            output[0] = i;
            if (index != i) {
                output[1] = index;
                sort(output.begin(), output.end());
                return output;
            }
        }
    }
    return output;
}


int main()
{
    twoSum(nums, target);
}


