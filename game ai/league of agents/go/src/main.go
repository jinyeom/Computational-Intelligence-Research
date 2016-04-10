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

    // window setting
    w := int(c["w_width"].(float64))
    h := int(c["w_height"].(float64))
    n := "League of Agents"
    window, err := glfw.CreateWindow(w, h, n, nil, nil)
    if err != nil {
        panic(err)
    }

    window.MakeContextCurrent()

    for !window.ShouldClose() {


        window.SwapBuffers()
        glfw.PollEvents()
    }
}
