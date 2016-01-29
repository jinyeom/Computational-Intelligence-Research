#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define L_DNA 8
#define P_P1_XOVER 20
#define P_P2_XOVER 20
#define P_MUTATION 20

void p1_xover(unsigned char* p1, unsigned char* p2)
{
    unsigned char i, s_p1, s_p2;

    srand((unsigned) time(NULL));

    for(i = 0x00; i < L_DNA &&
        rand() % 100 >= P_P1_XOVER; i++);

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

    printf("%x\n", i);
}

void p2_xover(unsigned char* p1, unsigned char* p2)
{

}

void u_xover(unsigned char* p1, unsigned char* p2)
{

}

void mutate(unsigned char* ch)
{
    unsigned char i, m_ch;

    srand((unsigned)time(NULL));

    m_ch = 0x00;

    for(i = 0x01; i > 0x00; i <<= 1)
    {
        if(rand() % 100 < P_MUTATION)
        {
            m_ch += i;
        }
    }

    *ch ^= m_ch;
}

int main() {
    unsigned char dna_1, dna_2;

    dna_1 = 0x6D;
    dna_2 = 0xB1;

    printf("dna_1 = %x\n", dna_1);

    mutate(&dna_1);

    printf("dna_1 = %x\n", dna_1);

    printf("dna_2 = %x\n", dna_2);

    p1_xover(&dna_1, &dna_2);

    printf("dna_1 = %x\n", dna_1);

    printf("dna_2 = %x\n", dna_2);
}
