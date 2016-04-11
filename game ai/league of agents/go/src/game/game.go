package game

import (
    "entity"
)

type Game struct {
    agents      []Agent     // slice of agents
    
}

func NewGame() *Game {
    return &Game{}
}
