#include "LeagueOfAgents.hpp"
#include "Champion.hpp"
#include "Minion.hpp"

// game test
void game_test()
{
    // create a new game object
    LeagueOfAgents game = new LeagueOfAgents();
    game.game_loop();
    game.update_terminal();
}

int main()
{
    game_test();
}
