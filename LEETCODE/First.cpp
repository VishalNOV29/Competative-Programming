#include <iostream>
int scan_count(void){
    int COL1=1,COL2=2,COL3=3,COL4=0;
    if (COL1==0){
        return 0;
    }else if(COL2==0){
        return 1;
    }else if(COL3==0){
        return 2;
    }else if(COL4==0){
        return 3;
    }
    return -1;
}

int main() {
    std::cout << scan_count();
    return 0;
}