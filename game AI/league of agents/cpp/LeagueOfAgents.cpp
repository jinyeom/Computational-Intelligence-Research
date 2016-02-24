#include "LeagueOfAgents.hpp"

LeagueOfAgents::LeagueOfAgents()
{
    this.gg_flag = false;

    this.r_player_1 = Champion();
    this.r_player_2 = Champion();
    this.r_minions = 

    this.b_player_1 = Champion();
    this.b_player_2 = Champion();
    this.b_minions =

}

LeagueOfAgents::~LeagueOfAgents()
{

}

void update_terminal()
{

}

Champion* LeagueOfAgents::game_loop()
{
    // loop until one team loses (main structure destroyed)
    while (gg_flag)
    {
        // update red players
        this.r_player_1.update();
        this.r_player_2.update();

        // update blue players
        this.b_player_1.update();
        this.b_player_2.update();

        update_terminal();
    }
}

Champion*
