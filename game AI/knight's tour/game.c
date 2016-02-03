#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define X_START 0x80
#define Y_START 0x00

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
    register int r, t;

    srand((unsigned) time(NULL));

    for (r = rand() % 63; r < 64; r++)
    {
        t = p_1[r];
        p_1[r] = p_2[r];
        p_2[r] = t;
    }
}

/* -------------------------- KNIGHT'S TOUR GAME ---------------------------- */

void move_knight(BYTE dna_slice, BYTE* k_x, BYTE* k_y)
{
    switch (dna_slice)
    {
        case 0x01:
            *k_x >>= 1;
            *k_y -= 2;
            break;

        case 0x02:
            *k_x >>= 2;
            *k_y -= 1;
            break;

        case 0x04:
            *k_x >>= 2;
            *k_y += 1;
            break;

        case 0x08:
            *k_x >>= 1;
            *k_y += 2;
            break;

        case 0x10:
            *k_x <<= 1;
            *k_y += 2;
            break;

        case 0x20:
            *k_x <<= 2;
            *k_y += 1;
            break;

        case 0x40:
            *k_x <<= 2;
            *k_y -= 1;
            break;

        case 0x80:
            *k_x <<= 1;
            *k_y -= 2;
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

    printf("%x\n", chess_board);

    return score;
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
