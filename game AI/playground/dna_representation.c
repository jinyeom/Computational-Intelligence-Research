#include <stdio.h>
#include <stdlib.h>

/*
    Since a char in C is represented with 8 bits, it can be used a
    piece of DNA with an precision of (1 / 2^8).
*/
int mutate(char d) {
    char r;
    time_t t;

    srand((unsigned) time(&t));

    r = 'A' + rand() % 10

}

int main() {

}
