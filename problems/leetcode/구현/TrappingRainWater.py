# 21.05.11

def trap(heights):
    if not heights:
        return 0

    volume = 0
    left=0
    right = len(heights)-1
    left_max = heights[left]
    right_max = heights[right]

    while left<right:
        left_max = max(heights[left],left_max)
        right_max = max(heights[right],right_max)

        if left_max <= right_max:
            volume += left_max - heights[left]
            left+=1
        else:
            volume += right_max - heights[right]
            right -=1
    return volume


i = trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(i)