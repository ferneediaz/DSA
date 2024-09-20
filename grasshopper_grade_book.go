package kata

func GetGrade(a, b, c int) rune {
	avg := (a + b + c) / 3

	switch {
	case avg >= 90 && avg <= 100:
		return 'A'
	case avg >= 80 && avg < 90:
		return 'B'
	case avg >= 70 && avg < 80:
		return 'C'
	case avg >= 60 && avg < 70:
		return 'D'
	default:
		return 'F'
	}
}
