package kata

func SquareSum(numbers []int) int {
    myslice := 0
    for i:= 0; i < len(numbers); i ++ {
      myslice += numbers[i] * numbers[i]
      }
    return myslice
}