#ifndef LEAGUEOFAGENTS_HPP
#define LEAGUEOFAGENTS_HPP

class LeagueOfAgents
{

private:

    bool        gg_flag;        /* game over indicator  */

    Nexus*      r_nexus;        /* red team Nexus       */
    Champion*   r_team;         /* red team Champions   */
    Minion*     r_minions;      /* red team Minions     */

    Nexus*      b_nexus;        /* blue team Nexus      */
    Champion*   b_team;         /* blue team Champions  */
    Minion*     b_minions;      /* blue team Minions    */

public:

    LeagueOfAgents();
    ~LeagueOfAgents();

    Champion* game_loop();
    Champion* create_team();
    Minion* create_minions();

};

#endif
