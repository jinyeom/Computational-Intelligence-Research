#include "LeagueOfAgents.hpp"

#define N_CHAMPIONS 2
#define N_MINIONS 50
#define N_SPAWN 10

LeagueOfAgents::LeagueOfAgents()
{
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

void LeagueOfAgents::game_loop()
{
    register int i;

    // loop until one team loses (main structure destroyed)
    for ( ; ; )
    {
        // update each team
        for (i = 0; i < N_CHAMPIONS; i++)
        {
            this.r_team[i].update();
            this.b_team[i].update();
        }

        // update red minions
        for (i = 0; i < N_MINIONS; i++)
        {
            this.r_minions[i].update();
            this.b_minions[i].update();
        }

        // update terminal info.
        this.update_terminal();

        // if one of the teams loses, game over.
        if (this.r_nexus.is_collapsed()|| this.b_nexus.is_collapsed())
            this.gg_flag = true;
    }
}

// create a new team with specified stats
Champion* LeagueOfAgents::create_team()
{
    Champion* team = new Champion[N_CHAMPIONS];

    team[0] = new Champion();
    team[1] = new Champion();

    return team;
}

// create total number of minions
Minion* LeagueOfAgents::create_minions()
{
    return new Minion[N_MINIONS];
}

// update the terminal as the game progresses
void LeagueOfAgents::update_terminal()
{
    register int i;

    cout << "----RED TEAM----" << endl;
    for (i = 0; i < N_CHAMPIONS; i++)
    {
        cout << "RED "
             << i + 1
             << this.r_team[i].
    }
}
