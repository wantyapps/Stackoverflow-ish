func calculatenumber(_ num: Int) -> String {
	if num >= 10 {
		return("BYTE 10")
	}
	return String(num * 10/2)
}

func run() -> Bool {
	if calculatenumber(5) == "25" {
		return true
	} else {
		return false
	}
}


// I was supposed to do a Command-Line-Argument Parser here, but there is no Internet, so I can't research about how to do this... :D
// Ha! I can do it with Go! Go: 1 Swift: 0


