package main

import (
	"fmt"
	"os"
)

func usage() {
	var script = os.Args[0]
	fmt.Println("Usage:")
	fmt.Println("--------------------------")
	fmt.Println(script + " [-c] / [--control]")
	fmt.Println(script + " [-c] / [--control] [-v] / [--verbose]")
}

func run(argg string) {
	if argg == "default" {
		if len(os.Args[1:]) > 0 {
			if os.Args[1:][0] == "-c" || os.Args[1:][0] == "--control" {
				fmt.Println("Control")
				if len(os.Args[1:]) > 1 {
					if os.Args[1:][1] == "-v" || os.Args[1:][1] == "--verbose" {
						fmt.Println("Control in Verbose Mode")
						fmt.Println("Turning on Verbose Mode...")
					}
				}
			}
		} else {
			usage()
		}
	}
}

func main() {
	run("default") // Why didn't I make the "run()" function the "main()" function, and then not run it from here?
}
