#include <stdio.h>

int main() {
    int i, j;
    i = 2;

    while (i < 101) {
        j = 2;
        while (j < i) {
            if (i % j == 0) {
                break;
            } else {
                j = j + 1;
            }
        }
        if (i == j) {
            printf ("%d \n", i);
        } else {
            i = i + 1;
        }
    }
    return 0;
}