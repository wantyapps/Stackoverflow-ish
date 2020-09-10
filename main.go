package main

import (
	"fmt"
	"os"
)

func run(argg string) {
	if argg == "default" {
		if len(os.Args[1:]) > 0 {
			if os.Args[1:][0] == "-c" || os.Args[1:][0] == "--control" {
				fmt.Println("Control")
				if len(os.Args[1:]) > 1 {
					if os.Args[1:][1] == "-v" || os.Args[1:][1] == "--verbose" {
						fmt.Println("Control in Verbose Mode")
						fmt.Println("Turning on Verbose mode...")
					}
				}
			}
		}
	}
}

func main() {
	run("default") // Why didn't I just make the "run()" function the main function, and then not run it from here?
}
