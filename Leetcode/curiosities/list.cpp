
#include <iostream>
#define SIZE 100
using namespace std;

class List{
public:
    int* head;
    int size;
    List(int val) {
        head = new int[SIZE];
    }

};

int main() {
    List temp = new List();
    return 0;
}