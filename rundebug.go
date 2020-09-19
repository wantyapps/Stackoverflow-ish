package main

import (
	"fmt"
	"os"
	"os/exec"
	"log"
	"bufio"
	"strings"
)

func main() {
	fmt.Println("[DEBUG] Starting debugger...") // This will be the debugger output
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("DEBUG KEY: ")
	key, _ := reader.ReadString('\n')

	out, err := exec.Command("python3", "api/api.py", "-d", key).Output()

	var finalout string = strings.Replace(string(out), "\n", "", -1)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(finalout))

	// Let's see if we can do this...

	if string(finalout) == "[API] Response: {\"username\": \"wantyapps\", \"password\": \"oao\"}" {
		fmt.Println("YOOOO")
	} else {
		fmt.Println("Nope.")
	}
}
