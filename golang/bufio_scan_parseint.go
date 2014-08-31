package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)

	split := func(data []byte, atEOF bool) (advance int, token []byte, err error) {
		advance, token, err = bufio.ScanWords(data, atEOF)
		if err == nil && token != nil {
			_, err = strconv.ParseInt(string(token), 10, 32)
		}
		return
	}

	sc.Split(split)

	for sc.Scan() {
		fmt.Printf("%s\n", sc.Text())
	}

	if err := sc.Err(); err != nil {
		fmt.Printf("Invalid input: %s", err)
	}

}
