//#include <iostream>
//using namespace std;
//// Forward declarations
//class B;
//class C;
//
//// Class A
//class A {
//private:
//    int privateVarA;
//
//public:
//    A() : privateVarA(0) {}
//
//    // Friend class declarations
//    friend class B;
//};
//
//// Class B
//class B {
//private:
//    int privateVarB;
//
//public:
//    B() : privateVarB(0) {}
//
//    // Friend class declaration
//    friend class C;
//
//    // Function to access private member of class A
//    void displayA(A &objA) {
//        cout << "Accessing private variable of A from B: " << objA.privateVarA << endl;
//    }
//};
//
//// Class C
//class C {
//private:
//    int privateVarC;
//
//public:
//    C() : privateVarC(0) {}
//
//    // Function to access private member of class B
//    void displayB(B &objB) {
//        cout << "Accessing private variable of B from C: " << objB.privateVarB << endl;
//    }
//    void dis(A &objA)
//    {
//    	cout << "Accessing private variable of A from B: " << objA.privateVarA << endl;
//	}
//};
//
//int main() {
//    A objA;
//    B objB;
//    C objC;
//
//    // Accessing private member of class A from friend class B
//    objB.displayA(objA);
//
//    // Accessing private member of class B from friend class C
//    objC.displayB(objB);
//
//    return 0;
//}
#include <stdio.h>

 

void func(int arr[], int size) {

    for (int i = 0; i < size; i++) {

        arr[i] += 5;

    }

}

 

int main() {

    int arr[] = {1, 2, 3, 4, 5};

    int size = sizeof(arr) / sizeof(arr[0]);

    func(arr, size);

    for (int i = 0; i < size; i++) {

        printf("%d ", arr[i]);

    }

    return 0;

}

