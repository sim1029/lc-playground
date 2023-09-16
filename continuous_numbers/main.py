# Given an array containing integers and a target number K, determine if there are continuous numbers that exist such that the sum of them equals to K.
def brute_force_solution(arr, k):
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum == k:
                return True
    return False


def solution(arr, k):
    if not arr or len(arr) == 0:
        return False

    l = 0
    total = 0
    for r in range(len(arr)):
        total += arr[r]
        while l < r and total > k:
            total -= arr[l]
            l += 1
        if total == k:
            return True
    return total == k


def test_solution(arr, k, out, number=None):
    print(f"\nStart Test {arr}")
    ret = solution(arr, k)
    if ret == out:
        if number:
            print(f"Test {number} Passed")
        else:
            print("Test Passed")
    else:
        if number:
            print(f"Test {number} Failed")
        else:
            print("Test Failed")
    print("End Test\n")


if __name__ == "__main__":
    # Test 1
    test_solution([1, 4, 5, 6, 0, 2, 3], 15, True, 1)
    # Test 2
    test_solution([1, 3, 2], 7, False, 2)
    # Test 3
    test_solution([1, 4, 5, 0, 6, 2, 3], 15, True, 3)
    # Test 4
    test_solution([4, -1, 2, -4], -2, True, 4)
    # Test 5
    test_solution([4, -1, 2, -4], 6, False, 5)
    # Test 6
    test_solution([], 10, False, 6)

# 1, 2, 3
# 1
# 3
# 2
# 6
# 5
# 3
