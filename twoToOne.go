package kata
import (

	"sort"
	"strings"
)
func TwoToOne(s1 string, s2 string) string {
  uniqueLetters := make(map[rune]bool)

	// Add each character from s1 and s2 to the map
	for _, char := range s1 + s2 {
		uniqueLetters[char] = true
	}

	// Collect the keys (unique letters) in a slice
	letters := make([]string, 0, len(uniqueLetters))
	for char := range uniqueLetters {
		letters = append(letters, string(char))
	}

	// Sort the slice alphabetically
	sort.Strings(letters)

	// Join the sorted slice into a single string and return it
	return strings.Join(letters, "")
}


