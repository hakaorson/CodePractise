#include <iostream>
#include <vector>
#include <tuple>
using namespace std;
struct Node {
    int val;
    Node* next;
    Node(int i) :val(i), next(nullptr) {};
};

Node* split(Node* target) {
    Node* left = target;
    Node* right = target;
    while (right->next != nullptr && right->next->next!= nullptr) {//通过split知道改怎么分割list
        left = left->next;
        right = right->next->next;
    }
    return left;
}

Node* sort(Node* target) {
    if (target->next == nullptr)return target;
    Node* sp = split(target);
    Node* rightpart = sp->next;
    Node* leftpart = target;
    sp->next = nullptr;

    rightpart = sort(rightpart);
    leftpart = sort(leftpart);

    Node* head = new Node(0);
    Node* cur = head;

    while (leftpart!=nullptr && rightpart!=nullptr)
    {
        if (leftpart->val <= rightpart->val) {
            cur->next = leftpart;
            cur = cur->next;
            leftpart = leftpart->next;
            cur->next = nullptr;//交割之后需要清除状态

        }
        else {
            cur->next = rightpart;
            cur = cur->next;
            rightpart = rightpart->next;
            cur->next = nullptr;

        }
    }
    if (leftpart != nullptr)
        cur->next = leftpart;
    else
        cur->next = rightpart;
    cur = head->next;
    delete head;
    return cur;
}



int main() {
    vector<int> nums = { 4,1,3,5,2,7 };
    Node* head = new Node(0);
    Node* cur = head;
    for (auto i : nums) {
        cur->next = new Node(i);
        cur = cur->next;
    }
    Node* result = sort(head->next);
    while (result != nullptr) {
        cout << result->val;
        result = result->next;
    }
    delete head;
    cout << "Hello World!" << endl;
}