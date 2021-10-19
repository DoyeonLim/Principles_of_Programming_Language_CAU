#include <stdio.h>

int i = 0;
int a[2] = { 1, 1 };

void p_reference(int* x, int* y) {
    (*x)++; i++; (*y)++;
}

main() {
    p_reference(&a[i], &a[i]);
    printf("reference : a[0]=%d, a[1]=%d\n", a[0], a[1]);
}