#include <stdio.h>

int main(){
    int myNum = 15;

    int myOtherNum;
    myOtherNum = 30;

    int one = 1, two = 2, three = 3;

    int john, noah, smith;
    john = noah = smith = 40;

    myNum = 20;

    int sum = one + two;

    printf("1 + 2 = %d \n", sum);
    
    float myFloatNum = 20.1;
    double myDoubleNum = 2.3;

    printf("%f\n", myFloatNum);
    printf("%.1f\n", myFloatNum);
    printf("%.2f\n", myFloatNum);
    printf("%.3f\n", myFloatNum);
    printf("%.4f\n", myFloatNum);
    printf("%lf\n", myDoubleNum);

    return 0;

}