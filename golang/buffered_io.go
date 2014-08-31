package main

import (
	"bufio"
	"fmt"
	"log"
	"strings"
)

const input = `
aaa bbb ccc
ddd eee
fff
`

func main() {
	s := bufio.NewScanner(strings.NewReader(input))
	for s.Scan() {
		fmt.Println(s.Text())
	}

	if err := s.Err(); err != nil {
		log.Fatal(err)
	}
}
