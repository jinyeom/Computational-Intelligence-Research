#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define L_DNA 8

/*
    Since a char in C is represented with 8 bits, it can be used a
    piece of DNA with an precision of (1 / 2^8).
*/
char mutate(char ch)
{
    char m_ch;                          /* char for mutation via xor    */

    srand((unsigned)time(NULL));        /* seed random number generator */

    m_ch = 0x00;                        /* m_ch originally 00000000     */

    int i;                              /* iterator i                   */
    for(i = 0; i < L_DNA; i++)          /* iterate through each bit     */
    {
        if(rand() % 10 < 5)             /* by chance of 0.5,            */
        {
            m_ch += pow(2, i);          /* flip a bit from 0 to 1       */
        }
    }

    printf("m_ch = %x\n", m_ch);

    ch ^= (char)m_ch;                   /* xor to mutated ch            */

    return ch;
}

int main() {
    char dna;

    dna = 0x5B;

    printf("original: %x\n", dna);
    printf("mutated: %x\n", mutate(&dna));
    printf("original: %x\n", dna);
}
