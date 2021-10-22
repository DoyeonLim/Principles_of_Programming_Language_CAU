#include <stdio.h>

int i = 0;
int a[2] = { 1, 1 };

void p_value_result_call(int* x, int* y) {
    int temp1 = *x;
    int temp2 = *y;

    temp1++; i++; temp2++;

    *x = temp1;
    *y = temp2;
}

main() {
    p_value_result_call(&a[i], &a[i]);
    printf("value-result(call) : a[0]=%d, a[1]=%d\n", a[0], a[1]);
}