func twoSum(nums []int, target int) []int {
    hashMap := make(map[int]int)
    for i,num := range nums{
        need := target - num
        if x,isFound := hashMap[need];isFound{
            return []int{x,i}
        }
    hashMap[num] = i
    }
return []int{}
}