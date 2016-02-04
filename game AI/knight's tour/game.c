#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define X_START         0x80
#define Y_START         0x00
#define N_POPULATION    100
#define P_MUTATION      20

typedef unsigned char BYTE;

/* ------------------- GENETIC ALGORITHM IMPLEMENTATION --------------------- */

BYTE* gen_dna()
{
    BYTE dna[63] = "";
    BYTE i, ch;

    srand((unsigned) time(NULL));

    for (i = 0; i < 63; i++)
    {
        ch = 0x01;
        ch <<= (rand() % 8);

        dna[i] = ch;
    }

    return *dna;
}

void mutation(BYTE* dna)
{
    register int i, r;

    srand((unsigned) time(NULL));

    for (i = 0; i < 63; i++)
    {
        r = rand() % 100;

        if (r < P_MUTATION)
        {
            if (r % 2 == 0)
            {
                dna[i] <<= 1;
            }

            else
            {
                dna[i] >>= 1;
            }
        }
    }
}

void p1_crossover(BYTE* p_1, BYTE* p_2)
{
    BYTE t;
    register int r,

    srand((unsigned) time(NULL));

    for (r = rand() % 63; r < 64; r++)
    {
        t = p_1[r];
        p_1[r] = p_2[r];
        p_2[r] = t;
    }
}

void genetic_algorithm()
{
    register int i, s;
    int b_score;
    BYTE dna, b_dna;

    BYTE *population[N_POPULATION];
    BYTE *children[N_POPULATION];

    for (i = 0; i < N_POPULATION; i++)
    {
        dna = gen_dna();
        population[i] = &dna;
    }

    while (best_score < 2040)
    {
        for (i = 0; i < N_POPULATION; i++)
        {
            s = game(population[i]);

            if (s > b_score)
            {
                b_score = s;
                b_dna = population[i];
            }
        }

        
    }
}

/* -------------------------- KNIGHT'S TOUR GAME ---------------------------- */

void move_knight(BYTE dna_slice, BYTE* k_x, BYTE* k_y)
{
    switch (dna_slice)
    {
        case 0x01:          /* 00000001         */
            *k_x >>= 1;     /* move one right   */
            *k_y -= 2;      /* move two up      */
            break;

        case 0x02:          /* 00000010         */
            *k_x >>= 2;     /* move two right   */
            *k_y -= 1;      /* move one up      */
            break;

        case 0x04:          /* 00000100         */
            *k_x >>= 2;     /* move two right   */
            *k_y += 1;      /* move one down    */
            break;

        case 0x08:          /* 00001000         */
            *k_x >>= 1;     /* move one right   */
            *k_y += 2;      /* move two down    */
            break;

        case 0x10:          /* 00010000         */
            *k_x <<= 1;     /* move one left    */
            *k_y += 2;      /* move two down    */
            break;

        case 0x20:          /* 00100000         */
            *k_x <<= 2;     /* move two left    */
            *k_y += 1;      /* move one down    */
            break;

        case 0x40:          /* 01000000         */
            *k_x <<= 2;     /* move two left    */
            *k_y -= 1;      /* move one up      */
            break;

        case 0x80:          /* 10000000         */
            *k_x <<= 1;     /* move one left    */
            *k_y -= 2;      /* move two up      */
            break;
    }
}

int game(BYTE* dna)
{
    unsigned int score;

    BYTE i, k_x, k_y;

    BYTE chess_board[8] = {0x00, 0x00, 0x00, 0x00,
                            0x00, 0x00, 0x00, 0x00};

    k_x = X_START;
    k_y = Y_START;

    chess_board[k_y] ^= k_x;

    for (i = 0; i < 63; i++)
    {
        printf("x = %3d, y = %3d\n", k_x, k_y);
        move_knight(dna[i], &k_x, &k_y);

        chess_board[k_y] ^= k_x;

    }

    score = 0;

    for (i = 0; i < 8; i++)
    {
        score += (unsigned int) chess_board[i];
    }

    return score;
}

void print_chess_board(BYTE* chess_board)
{

}

int main()
{
    // a solution
    BYTE dna[63] = {0x08, 0x10, 0x08, 0x04, 0x02, 0x04, 0x80, 0x01,
                    0x80, 0x40, 0x20, 0x20, 0x08, 0x10, 0x04, 0x02,
                    0x04, 0x01, 0x80, 0x01, 0x40, 0x20, 0x40, 0x08,
                    0x20, 0x08, 0x10, 0x02, 0x04, 0x02, 0x01, 0x80,
                    0x01, 0x20, 0x40, 0x20, 0x08, 0x08, 0x02, 0x80,
                    0x10, 0x04, 0x80, 0x20, 0x20, 0x08, 0x02, 0x04,
                    0x02, 0x80, 0x01, 0x80, 0x20, 0x40, 0x20, 0x08,
                    0x08, 0x02, 0x01, 0x20, 0x08, 0x01, 0x40};

    printf("score: %d\n", game(dna));
}
