#include<iostream>
using namespace std;
int count = 0;
 
 void add(int& count)
 {
     count++;
 }

 int main()
 {
    add(count);
    return 0;
 }