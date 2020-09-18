package main

import "fmt" // For the debugging output

import "os/exec"

import "log"

func main() {
	fmt.Println("[DEBUG] Starting debugger...") // This will be the debugger output
	out, err := exec.Command("python3", "api/api.py", "-d").Output()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(out))
}
