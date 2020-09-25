package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"os/exec"
	"strings"
)

func main() {
	fmt.Println("[\033[94mDEBUG\033[0m] Starting debugger...") // This will be the debugger output
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

	if string(finalout) == "[\033[92m*\033[0m] Response: {\"username\": \"wantyapps\", \"password\": \"oao\"}" {
		fmt.Println("[\033[92mDEBUG\033[0m] DONE")
	} else {
		fmt.Println("[\033[91mDEBUG\033[0m] ERROR")
	}
}

