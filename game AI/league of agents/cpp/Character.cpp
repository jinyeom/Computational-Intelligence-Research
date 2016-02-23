

// check if this minion is dead
bool Character::is_dead()
{
    return (this.hp == 0);
}

// move the minion to (x, y)
void Character::move(int x, int y)
{

}

// getters
int Character::get_m_num()              {   return this.m_num;              }
double Character::get_dir()             {   return this.dir;                }
int Character::get_speed()              {   return this.speed;              }
double Character::get_atk_damage()      {   return this.atk_damage;         }
double Character::get_atk_range()       {   return this.atk_range;          }
double Character::get_atk_speed()       {   return this.atk_speed;          }

// setters
void Character::set_atk_damage(double atk_damage)
{   this.atk_damage = atk_damage;   }
