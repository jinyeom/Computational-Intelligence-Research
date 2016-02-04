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
    BYTE i, ch;
    static BYTE dna[63];

    srand((unsigned) time(NULL));

    for (i = 0; i < 63; i++)
    {
        ch = 0x01;
        ch <<= (rand() % 8);

        dna[i] = ch;
    }

    return dna;
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

    return;
}

void p1_crossover(BYTE* p_1, BYTE* p_2)
{
    BYTE t;
    register int r;

    srand((unsigned) time(NULL));

    for (r = rand() % 63; r < 64; r++)
    {
        t = p_1[r];
        p_1[r] = p_2[r];
        p_2[r] = t;
    }

    return;
}

int t_selection(int* scores)
{
    register int b, i, r;

    srand((unsigned) time(NULL));

    b = scores[rand() % N_POPULATION];

    for (i = 0; i < N_POPULATION - 1; i++)
    {
        r = scores[rand() % N_POPULATION];

        if (r > b)
        {
            b = r;
        }
    }

    return b;
}

void genetic_algorithm()
{
    register int i, j, s;                       /* ints for quick accesses  */
    int b_score;                                /* global best score        */
    int scores[N_POPULATION];                   /* array of scores          */

    BYTE b_dna[63];                             /* best dna string          */
    BYTE *pop[N_POPULATION];                    /* array of dna pointers    */
    BYTE *children[N_POPULATION];               /* population of next gen   */

    int p_1, p_2;                               /* parent 1 and 2 indices   */

    for (i = 0; i < N_POPULATION; i++)          /* initialize a population  */
    {
        pop[i] = gen_dna();
    }

    while (b_score < 2040)
    {
        for (i = 0; i < N_POPULATION; i++)
        {
            s = game(pop[i]);

            scores[i] = s;                      /* update array of scores   */

            if (s > b_score)
            {
                b_score = s;

                for (j = 0; j < 63; j++)        /* make a deep copy of the  */
                {                               /* best DNA, so that it     */
                    b_dna[j] = pop[i][j];       /* doesn't get affected by  */
                }                               /* future processing        */
            }
        }

        for (i = 0; i < N_POPULATION; i += 2)
        {
            p_1 = t_selection(scores);          /* t_select p_1 index       */
            p_2 = t_selection(scores);          /* t_select p_2 index       */

            p1_crossover(pop[p_1], pop[p_2]);

            mutation(pop[p_1]);
            mutation(pop[p_2]);
        }
    }

    printf("%s\n", b_dna);

    return;
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

    return;
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

void test()
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

int main()
{
    genetic_algorithm();
}
