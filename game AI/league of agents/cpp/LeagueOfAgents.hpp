#ifndef LEAGUEOFAGENTS_HPP
#define LEAGUEOFAGENTS_HPP

class LeagueOfAgents
{

private:

    bool gg_flag;

    Champion r_player_1;
    Champion r_player_2;
    Minion* r_minions;

    Champion b_player_1;
    Champion b_player_2;
    Minion* b_minions;

public:

    LeagueOfAgents();
    ~LeagueOfAgents();

    void update_terminal();

    Champion* game_loop();
    Champion* create_teams();

};

#endif
