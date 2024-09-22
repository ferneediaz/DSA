package kata

import "strconv"

func SumMix(arr []any) int {
    sum := 0
    for _, val := range arr {
        switch v := val.(type) {
        case int:
            sum += v
        case string:
            num, _ := strconv.Atoi(v)
            sum += num
        }
    }
    return sum
}
