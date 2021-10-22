#include <stdio.h>

int i = 0;
int a[2] = { 1, 1 };

void p_name(int* x, int* y) {
    int temp1 = *x;
    temp1++;
    *x = temp1;

    x = x + i;
    i++;
    y = y + i;

    int temp2 = *y;
    temp2++;
    *y = temp2;
}

main() {
    p_name(&a[i], &a[i]);
    printf("reference : a[0]=%d, a[1]=%d\n", a[0], a[1]);
}