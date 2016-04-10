package main

import (
    "runtime"
    "tool"
    "github.com/go-gl/glfw/v3.1/glfw"
)

func init() {
    // main() runs on main thread
    runtime.LockOSThread()

}

func main() {
    // get configurations
    c := tool.Config("tool/conf.json")

    // initialize GLFW
    err := glfw.Init()
    if err != nil {
        panic(err)
    }
    defer glfw.Terminate()

    // window sizes
    w := c["w_width"].(int)
    h := c["w_height"].(int)

    window, err := glfw.CreateWindow(w, h, "LOL", nil, nil)

    if err != nil {
        panic(err)
    }

    window.MakeContextCurrent()

    for !window.ShouldClose() {


        window.SwapBuffers()
        glfw.PollEvents()
    }
}
