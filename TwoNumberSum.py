// Ques-: Two Number Sum

// Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

// Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

// You can assume that there will be at most one pair of numbers summing up to the target sum.

// Sample Input
// array = [3, 5, -4, 8, 11, 1, -1, 6]
// targetSum = 10
// Sample Output
// [-1, 11] // the numbers could be in reverse order

def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
	left = 0
	right = len(array) - 1
	while left < right:
		checkSum = array[left] + array[right]
		if checkSum == targetSum:
			return [array[left], array[right]]
		elif checkSum < targetSum:
			left = left+1
		elif checkSum > targetSum:
			right = right-1
	return []


