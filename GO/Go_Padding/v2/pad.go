package padstring 

func PadRight(s string, totalLength int) string {
	padding := totalLength - len(s)
	var i = 0
	if padding > 0{
		for i < padding{
			s = s + " " 
			i++
		}
	}

	return s 
}

func PadLeft(s string, totalLength int) string {
	padding := totalLength - len(s)
	var i = 0
	if padding > 0{
		for i < padding{
			s = " " + s
			i++
		}
	}
	return s
}
