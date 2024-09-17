func removeDuplicates(nums []int) int {
    if len(nums) == 0 {
        return 0
    }

    // Using two pointers approach
    // i points to the last unique element
    // j iterates through the array
    i := 0
    for j := 1; j < len(nums); j++ {
        if nums[j] != nums[i] {
            i++
            nums[i] = nums[j]
        }
    }

    return i + 1
}