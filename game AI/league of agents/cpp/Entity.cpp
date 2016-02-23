#include "Entity.hpp"

Entity::Entity() {}
Entity::~Entity() {}

// getters
int Entity::get_f_hp()              {   return this.f_hp;   }
int Entity::get_hp()                {   return this.hp;     }
int Entity::get_x()                 {   return this.x;      }
int Entity::get_y()                 {   return this.y;      }

// setters
void Entity::set_f_hp(int f_hp)     {   this.f_hp = f_hp;   }
void Entity::set_hp(int hp)         {   this.hp = hp;       }
void Entity::set_x(int x)           {   this.x = x;         }
void Entity::set_y(int y)           {   this.y = y;         }
