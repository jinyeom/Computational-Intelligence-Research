package main

import (
    "fmt"
    "runtime"
    "tool"
    "ui"
    "game"
    "github.com/go-gl/glfw/v3.1/glfw"
    "github.com/go-gl/gl/v4.1-core/gl"
)

// logo print
func logoPrint() {
    logo := `
 __        _____     _____     _____     __  __    _____
/\ \      /\  ___\  /\  __ \  /\  ___\  /\ \/\ \  /\  ___\      v.0.1.0
\\\ \     \\\ \__/  \\\ \_\ \ \\\ \  __ \\\ \ \ \ \\\ \__/      ____   ____
 \\\ \     \\\  ___\ \\\  __ \ \\\ \/\ \ \\\ \ \ \ \\\  ___\   | __ | | ___|
  \\\ \___  \\\ \__/  \\\ \/\ \ \\\ \_\ \ \\\ \_\ \ \\\ \__/   ||  || | |_
   \\\_____\ \\\_____\ \\\_\ \_\ \\\_____\ \\\_____\ \\\_____\ ||__|| | __|
    \/=====/  \/=====/  \/=/\/=/  \/=====/  \/=====/  \/=====/ |____| |_|
          _____     _____     _____    __        __    _______     ______
        / __  /\  /  ___/\  /  ___/\  /  \      / /\ /__   __/\  /  ____/\
       / /_/ /// / /\ __\/ /  /___\/ / /\ \    / /// \_/  /\_\/ /  /____\/
      / __  /// / / / /\  /  ___/\  / ///\ \  / ///   /  ///   /___   /\
     / /\/ /// / /_/ /// /  /___\/ / ///  \ \/ ///   /  ///   _\__/  ///
    /_/ /_/// /_____/// /_____/\  /_///    \ _///   /__///   /______///
    \=\/\=\/  \=====\/  \=====\/  \=\/      \=\/    \==\/    \======\/
`

    fmt.Println(logo)
}

// GL - new program
func newProgram(vertShaderSrc, fragShaderSrc string) (uint32, error) {
    vertexShader, err := ui.CompileShader()

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
    // print the logo
    logoPrint()

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

    // setup clear color
    gl.ClearColor(
        float32(c["clear_r"].(float64)),
        float32(c["clear_g"].(float64)),
        float32(c["clear_b"].(float64)),
        float32(c["clear_a"].(float64)))

    // game loop
    for !window.ShouldClose() {
        gl.Clear(gl.COLOR_BUFFER_BIT)

        // gl.BeginQuery(TRIANGLES)
        // glVertex(0.5,0.5)
        // glVertex(0.0,-0.1)
        // glVertex(-0.5,0.5)
        // glEnd();






        window.SwapBuffers()
        glfw.PollEvents()
    }
}
