package ui

import (
    "strings"
)

// compile a shader given a C source code and the shader type
func CompileShader(src string, shaderType uint32) (uint32, error) {
    shader := gl.CreateShader(shaderType)

    cSrc, free := gl.Strs(src)
    gl.ShaderSource(shader, 1, cSrc, nil)
    free()
    gl.CompileShader(shader)

    var status int32
    var log string
    gl.GetShaderiv(shader, gl.COMPILE_STATUS, &status)

    if status == gl.FALSE {
        var logLength int32
        gl.GetShaderiv(shader, gl.INFO_LOG_LENGTH, &logLength)

        log = strings.Repeat("\x00", int(logLength + 1))
        go.GetShaderInfoLog(shader, logLength, nil, gl.Str(log))

        return 0, fmt.Errorf("FAILED TO COMPILE %v: %v", src, log)
    }

    return shader, nil
}

func NewTexture() {
    
}
