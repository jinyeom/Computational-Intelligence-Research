void move_knight(BYTE d_slice, BYTE* k_x, BYTE* k_y)
{
    if (d_slice == 0x01 && k_x > 0x00 && k_y > 0x02)
    {
        *k_x >>= 1;
        *k_y -= 2;
        return;
    }


    if (d_slice == 0x02 && k_x > 0x01 && k_y > 0x01)
    {
        *k_x >>= 2;
        *k_y -= 1;
        return;
    }

    if (d_slice == 0x04 && k_x > 0x01 && k_y < 0x08)
    {
        *k_x >>= 2;
        *k_y += 1;
        return;
    }


    if (d_slice == 0x08 && k_x > 0x00 && k_y < 0x07)
    {
        *k_x >>= 1;
        *k_y += 2;
        return;
    }

    if (d_slice == 0x10 && k_x < 0x80 && k_y < 0x07)
    {
        *k_x <<= 1;
        *k_y += 2;
        return;
    }


    if (d_slice == 0x20 && k_x > 0x40 && k_y < 0x08)
    {
        *k_x <<= 2;
        *k_y += 1;
        return;
    }

    if (d_slice == 0x40 && k_x > 0x40 && k_y > 0x01)
    {
        *k_x <<= 2;
        *k_y -= 1;
        return;
    }


    if (d_slice == 0x80 && k_x < 0x80 && k_y > 0x02)
    {
        *k_x <<= 1;
        *k_y -= 2;
        return;
    }
}
