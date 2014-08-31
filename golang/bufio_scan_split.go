package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)

	for sc.Scan() {
		splitted := strings.SplitN(sc.Text(), " ", -1)
		fmt.Printf("%q\n", splitted)
	}

}
