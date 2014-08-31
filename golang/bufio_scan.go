package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)

	for sc.Scan() {
		fmt.Printf("%s\n", sc.Text())
	}

}
