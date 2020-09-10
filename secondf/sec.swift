func calculatenumber(_ num: Int) -> String {
	if num >= 10 {
		return("BYTE 10")
	}
	return String(num * 10/2)
}

func run() -> Bool {
	if calculatenumber(4) == "25" {
		return true
	} else {
		return false
	}
}

print(run())
