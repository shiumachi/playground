package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Message struct {
	Body string
}

func main() {
	msg := Message{
		Body: "hello",
	}

	b, err := json.Marshal(msg)
	if err != nil {
		fmt.Println("err: %s", err)
	}

	encoder := json.NewEncoder(os.Stdout)
	encoder.Encode(msg)

	os.Stdout.Write(b)
	fmt.Println("")
}
