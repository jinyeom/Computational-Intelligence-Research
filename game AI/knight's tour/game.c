#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define X_START 0x80
#define Y_START 0x00

typedef unsigned char BYTE;

/*   .~~~^ KNIGHT'S TOUR ^~~~.   */
/*                               */

// for debugging
void print_chess_board(BYTE* chess_board)
{

}

void move_knight(BYTE dna_slice, BYTE* k_x, BYTE* k_y)
{
    switch (dna_slice)
    {
        case 0x01:  *k_x >>= 1;
                    *k_y -= 2;
        case 0x02:  *k_x >>= 2;
                    *k_y -= 1;
        case 0x04:  *k_x >>= 2;
                    *k_y += 1;
        case 0x08:  *k_x >>= 1;
                    *k_y += 2;
        case 0x10:  *k_x <<= 1;
                    *k_y += 2;
        case 0x20:  *k_x <<= 2;
                    *k_y += 1;
        case 0x40:  *k_x <<= 2;
                    *k_y -= 1;
        case 0x80:  *k_x <<= 1;
                    *k_y -= 2;
    }
}

int game(char* dna)
{
    int score;

    BYTE chess_board[8];
    BYTE i, k_x, k_y;

    k_x = X_START;
    k_y = Y_START;

    *chess_board[k_y] ^= k_x;

    for (i = 0x00; i < 63; i++)
    {
        move_knight(dna[i], &k_x, &k_y);
        chess_board[k_y] ^= k_x;
    }

    for (i = 0x00; i < 0x08; i++)
    {
        score += chess_board[i];
    }

    return score;
}

int main()
{
    BYTE dna;



    printf("score: %d\n", game(&dna));
}
