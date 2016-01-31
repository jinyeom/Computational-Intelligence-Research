#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define L_DNA 8
#define P_P1_XOVER 20
#define P_P2_XOVER 20
#define P_MUTATION 20

typedef unsigned char BYTE;

void p1_xover(BYTE* p1, BYTE* p2)
{
    BYTE i, s_p1, s_p2;

    srand((unsigned) time(NULL));

    for (i = 0x00; i < L_DNA &&
        rand() % 100 >= P_P1_XOVER; i++);

    if (i == 0)
    {
        return;
    }

    s_p1 = *p1;
    s_p1 <<= L_DNA - i;
    s_p1 >>= L_DNA - i;

    s_p2 = *p2;
    s_p2 <<= L_DNA - i;
    s_p2 >>= L_DNA - i;

    *p1 >>= i;
    *p1 <<= i;

    *p2 >>= i;
    *p2 <<= i;

    *p1 += s_p2;
    *p2 += s_p1;
}

void p2_xover(BYTE* p1, BYTE* p2)
{
    BYTE i_1, i_2, s_p1, s_p2;

    srand((unsigned) time(NULL));

    for (i_1 = 0x00; i_1 < L_DNA &&
        rand() % 100 >= P_P2_XOVER; i_1++);

    for (i_2 = i_1; i_2 < L_DNA &&
        rand() % 100 >= P_P2_XOVER; i_2++);

    if (i_1 == i_2)
    {
        return;
    }

    s_p1 = *p1;
    s_p1 <<= L_DNA - i_2;
    s_p1 >>= L_DNA - i_2 + i_1;
    s_p1 <<= i_1;

    s_p2 = *p2;
    s_p2 <<= L_DNA - i_2;
    s_p2 >>= L_DNA - i_2 + i_1;
    s_p2 <<= i_1;

    *p1 ^= s_p1;
    *p1 += s_p2;

    *p2 ^= s_p2;
    *p2 += s_p1;
}

void mutate(BYTE* ch)
{
    BYTE i, m_ch;

    srand((unsigned) time(NULL));

    for (i = 0x01; i > 0x00; i <<= 1)
    {
        if (rand() % 100 < P_MUTATION)
        {
            m_ch += i;
        }
    }

    *ch ^= m_ch;
}

void test()
{
    BYTE dna_1, dna_2;

    dna_1 = 0x6D;
    dna_2 = 0xB1;

    printf("dna_1 = %x\n", dna_1);

    mutate(&dna_1);

    printf("dna_1 = %x\n", dna_1);

    printf("dna_2 = %x\n", dna_2);

    p1_xover(&dna_1, &dna_2);

    printf("dna_1 = %x\n", dna_1);

    printf("dna_2 = %x\n", dna_2);

    p2_xover(&dna_1, &dna_2);

    printf("dna_1 = %x\n", dna_1);

    printf("dna_2 = %x\n", dna_2);
}

int main()
{
    test();
    return 0;
}
