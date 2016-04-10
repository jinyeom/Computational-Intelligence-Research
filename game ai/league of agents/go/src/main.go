package main

import (
    "fmt"
    "runtime"
    "tool"
    "github.com/go-gl/glfw/v3.1/glfw"
    "github.com/go-gl/gl/v4.1-core/gl"
)

// add an agent
func addAgent() {
    // to be implemented
}

// update the game lop
func update() {
    // to be implemented
}

func main() {
    // main() runs on main thread
    runtime.LockOSThread()

    // get configurations
    c := tool.Config("tool/conf.json")

    // initialize GLFW
    if err := glfw.Init(); err != nil {
        panic(err)
    }
    defer glfw.Terminate()

    // window setting
    glfw.WindowHint(glfw.Resizable, glfw.False)
	glfw.WindowHint(glfw.ContextVersionMajor, 4)
	glfw.WindowHint(glfw.ContextVersionMinor, 1)
	glfw.WindowHint(glfw.OpenGLProfile, glfw.OpenGLCoreProfile)
	glfw.WindowHint(glfw.OpenGLForwardCompatible, glfw.True)

    w := int(c["w_width"].(float64))
    h := int(c["w_height"].(float64))
    t := "League of Agents"

    window, err := glfw.CreateWindow(w, h, t, nil, nil)
    if err != nil {
        panic(err)
    }

    window.MakeContextCurrent()

    // init GL
    if err := gl.Init(); err != nil {
        panic(err)
    }

    // gl version
    version := gl.GoStr(gl.GetString(gl.VERSION))
	fmt.Println("OpenGL version", version)


    // game loop
    for !window.ShouldClose() {




        window.SwapBuffers()
        glfw.PollEvents()
    }
}
