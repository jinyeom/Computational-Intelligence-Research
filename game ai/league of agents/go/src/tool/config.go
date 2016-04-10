package tool

import (
    "os"
    "io"
    "fmt"
    "log"
    "bytes"
    "encoding/json"
)

// return the configuration
func Config(path string) (conf map[string]interface{}) {
    // read a json file from given path
    buf := bytes.NewBuffer(nil)
    file, err := os.Open(path)
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    // copy json file in a string
    io.Copy(buf, file)
    str := string(buf.Bytes())
    fmt.Println(str)

    // create map with string
    var f interface{}
    err = json.Unmarshal([]byte(str), &f)
    if err != nil {
        log.Fatal(err)
    }

    // define config and return
    conf = f.(map[string]interface{})
    return
}
