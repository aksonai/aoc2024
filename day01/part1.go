package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	file, _ := os.Open("test.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		l, _ := strconv.Atoi(parts[0])
		r, _ := strconv.Atoi(parts[1])
		fmt.Println(l)
		fmt.Println(r)
		fmt.Printf("Type: %T\n", l)
		fmt.Println(line)
	}
}
