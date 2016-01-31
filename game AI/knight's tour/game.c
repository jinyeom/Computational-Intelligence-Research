#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define X_START 0x80
#define Y_START 0x00

typedef unsigned char BYTE;

/*  .~~~~^ KNIGHT'S TOUR ^~~~~.  */
/*                               */

void move_knight(BYTE* k_x, BYTE* k_y)
{

}

void game()
{
    BYTE chess_board[8];
    BYTE i, k_x, k_y;

    k_x = X_START;
    k_y = Y_START;

    *chess_board[k_y] ^= k_x;

    for(i = 0x00; i < 63; i++)
    {
        move_knight(&k_x, &k_y);
        chess_board[k_y] ^= k_x;
    }


}

int main()
{
    game();
}
