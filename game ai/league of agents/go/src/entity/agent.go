package entity

import (
    "neat"
)

// define an Agent
type Agent struct {
    x       int         // x coordinate
    y       int         // y coordinate
    dx      float64     // x speed
    dy      float64     // y speed
    hp      float64     // health point
    dmg     float64     // damage
    brain   neat.NNet   // neural network
}

func NewAgent(b neat.NNet) *Agent {
    return &Agent{}
}
