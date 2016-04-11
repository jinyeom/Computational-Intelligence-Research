package game

import (
    "entity"
)

type Game struct {
    agents      []entity.Agent     // slice of agents

}

func NewGame() *Game {
    return &Game{}
}
