#include <stdio.h>

int i = 0;
int a[2] = { 1, 1 };

void p_value_result_return(int* x, int* y) {
    int temp1 = *x;
    int temp2 = *y;

    temp1++; i++; temp2++;

    x = x + i;
    y = y + i;

    *x = temp1;
    *y = temp2;
}

main() {
    p_value_result_return(&a[i], &a[i]);
    printf("reference : a[0]=%d, a[1]=%d\n", a[0], a[1]);
}