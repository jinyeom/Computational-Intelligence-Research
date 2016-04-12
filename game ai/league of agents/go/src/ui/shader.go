package ui

import (
    // "os"
    "fmt"
    // "image"
    "strings"
    "github.com/go-gl/gl/v4.1-core/gl"
)

// vertex shader C source code
const VERTEX_SHADER_SRC string =
`
# version 330

uniform mat4 projection;
uniform mat4 camera;
uniform mat4 model;

in vec3 vert;
in vec2 vertTexCoord;
out vec2 fragTexCoord;

void main() {
    fragTexCoord = vertTexCoord;
    gl_Position = projection * camera * model * vec4(vert, 1);
}
`

// fragment shader C source code
const FRAG_SHADER_SRC string =
`
# version 330

uniform sampler2D tex;

in vec2 fragTexCoord;
out vec4 outputColor;

void main() {
    outputColor = texture(tex, fragTexCoord);
}
`

// new OpenGL program
func NewProgram(vertShaderSrc, fragShaderSrc string) (uint32, error) {
    // vertex shader
    vertexShader, err := CompileShader(vertShaderSrc, gl.VERTEX_SHADER)
    if err != nil {
		return 0, err
	}

    // fragment shader
	fragShader, err := CompileShader(fragShaderSrc, gl.FRAGMENT_SHADER)
	if err != nil {
		return 0, err
	}

    program := gl.CreateProgram()

    gl.AttachShader(program, vertexShader)
    gl.AttachShader(program, fragShader)
    gl.LinkProgram(program)

    var status int32
	gl.GetProgramiv(program, gl.LINK_STATUS, &status)
	if status == gl.FALSE {
		var logLength int32
		gl.GetProgramiv(program, gl.INFO_LOG_LENGTH, &logLength)

		log := strings.Repeat("\x00", int(logLength + 1))
		gl.GetProgramInfoLog(program, logLength, nil, gl.Str(log))

		return 0, fmt.Errorf("FAILED TO LINK PROGRAM: %v", log)
	}

	gl.DeleteShader(vertexShader)
	gl.DeleteShader(fragShader)

	return program, nil
}

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
        gl.GetShaderInfoLog(shader, logLength, nil, gl.Str(log))

        return 0, fmt.Errorf("FAILED TO COMPILE %v: %v", src, log)
    }

    return shader, nil
}

// // load new sprite
// func NewSprite(file string) (uint32, error) {
//     // open an image file
//     imgFile, err := os.Open(file)
//     if err != nil {
//         return 0, err
//     }
//
//     // decode the image file
//     img, _, err := image.Decode(imgFile)
//     if err != nil {
//         return 0, err
//     }
//
//     var sprite uint32
//
//
//
//
//
//
//
//
//     return sprite, nil
// }
