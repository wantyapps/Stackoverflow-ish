package main

import (
	"fmt"
	"os"
	"os/exec"
	"log"
	"bufio"
)

func main() {
	fmt.Println("[DEBUG] Starting debugger...") // This will be the debugger output
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("DEBUG KEY: ")
	key, _ := reader.ReadString('\n')

	out, err := exec.Command("python3", "api/api.py", "-d", key).Output()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(out))
}
