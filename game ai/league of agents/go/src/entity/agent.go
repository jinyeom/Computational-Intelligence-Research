package entity

import (

)

// define an Agent
type Agent struct {
    x       int         // x coordinate
    y       int         // y coordinate
    dx      float64     // x speed
    dy      float64     // y speed
    hp      float64     // health point
    dmg     float64     // damage
    brain   NNet        // neural network
}

func NewAgent() *Agent {
    return &Agent{}
}
