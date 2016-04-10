package main

import (
    "os"
    "encoding/json"
    "runtime"
    "github.com/go-gl/glfw/v3.1/glfw"
)

func init() {
    // main() runs on main thread
    runtime.LockOSThread()

}

func main() {
    err := glfw.Init()
    if err != nil {
        panic(err)
    }
    defer glfw.Terminate()

    window, err := glfw.CreateWindow(W_WIDTH, W_HEIGHT, "Testing", nil, nil)
    if err != nil {
        panic(err)
    }

    window.MakeContextCurrent()

    for !window.ShouldClose() {


        window.SwapBuffers()
        glfw.PollEvents()
    }
}
