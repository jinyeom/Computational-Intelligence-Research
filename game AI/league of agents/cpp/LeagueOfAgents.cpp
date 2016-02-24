#include "LeagueOfAgents.hpp"

#define N_CHAMPIONS 2
#define N_MINIONS 5

LeagueOfAgents::LeagueOfAgents()
{
    this.gg_flag    = false;

    this.r_nexus    = new Nexus();
    this.r_team     = create_team();
    this.r_minions  = create_minions();

    this.b_nexus    = new Nexus();
    this.b_team     = create_team();
    this.b_minions  = create_minions();
}

LeagueOfAgents::~LeagueOfAgents()
{
    delete this.r_team;
    delete this.r_minions;
    delete this.b_team;
    delete this.b_minions;
}

Champion* LeagueOfAgents::game_loop()
{
    register int i;

    // loop until one team loses (main structure destroyed)
    while (gg_flag)
    {
        // update red players
        for (i = 0; i < N_CHAMPIONS; i++)
            this.r_team[i].update();

        // update blue players
        for (i = 0; i < N_CHAMPIONS; i++)
            this.b_team[i].update();

        // update red minions
        for (i = 0; i < N_MINIONS; i++)
            this.r_minions[i].update();

        // update blue minions
        for (i = 0; i < N_MINIONS; i++)
            this.b_minions[i].update();

        if ()


        this.update_terminal();
    }
}

Champion* LeagueOfAgents::create_team()
{
    Champion* team = new Champion[N_CHAMPIONS];

    team[0] = new Champion();
    team[1] = new Champion();

    return team;
}

Minion* LeagueOfAgents::create_minions()
{
    return new Minion[N_MINIONS];
}

// update the terminal as the game progresses
void LeagueOfAgents::update_terminal()
{

}
