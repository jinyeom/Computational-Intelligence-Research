package main

import (
    "tool"
    "runtime"
    "github.com/veandco/go-sdl2/sdl"
)

// initialize
func mainInit() {
    // main() as main thread
    runtime.LockOSThread()

    // initialize SDL
    sdl.Init(sdl.INIT_EVERYTHING)

}

// add an agent
func addAgent() {
    // to be implemented
}

// update the game lop
func update() {
    // to be implemented
}

func main() {
    mainInit()

    // get configurations
    c := tool.Config("tool/conf.json")

    // setup SDL

    // window setting
    w := int(c["w_width"].(float64))
    h := int(c["w_height"].(float64))
    t := "League of Agents"
    window, err := sdl.CreateWindow(t, sdl.WINDOWPOS_UNDEFINED,
        sdl.WINDOWPOS_UNDEFINED, w, h, sdl.WINDOW_SHOWN)
    if err != nil {
        panic(err)
    }
    defer window.Destroy()

    surface, err := window.GetSurface()
    if err != nil {
        panic(err)
    }

    // game loop
    for true {
        rect := sdl.Rect{0, 0, 200, 200}
        surface.FillRect(&rect, 0xffff0000)

        window.UpdateSurface()
        sdl.Delay(1000)
    }


    sdl.Quit()
}
