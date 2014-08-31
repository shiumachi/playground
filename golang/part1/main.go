// Solution to part 1 of the Whispering Gophers code lab.
// This program reads from standard input and writes JSON-encoded messages to
// standard output. For example, this input line:
//	Hello!
// Produces this output:
//	{"Body":"Hello!"}
//
package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"os"
)

type Message struct {
	Body string
}

func main() {
	// TODO: Create a new bufio.Scanner reading from the standard input.
	sc := bufio.NewScanner(os.Stdin)

	// TODO: Create a new json.Encoder writing into the standard output.
	for sc.Scan() {
		// TODO: Create a new message with the read text.
		// TODO: Encode the message, and check for errors!
	}
	// TODO: Check for a scan error.

	if err := sc.Err(); err != nil {
		fmt.Printf("Scan error: %s", err)
	}
}
