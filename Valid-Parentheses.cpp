#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stck;
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                stck.push(c);
            } else {
                if (stck.empty()) {
                    return false; // Closing bracket found with no matching opener
                }
                if ((c == ')' && stck.top() == '(') || 
                    (c == '}' && stck.top() == '{') || 
                    (c == ']' && stck.top() == '[')) {
                    stck.pop();
                } else {
                    return false; // Mismatched brackets
                }
            }
        }
        return stck.empty(); // True only if the stack is empty after all characters are processed
    }
};
