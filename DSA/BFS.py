from collections import deque

def bfs_level_aggregate(root, aggregate='sum', return_level=False):
    """
    Generic BFS template for level-based aggregates.

    Parameters:
    - root: TreeNode
    - aggregate: 'sum', 'average', 'max', 'min'
    - return_level: if True, return the level number with max/min sum instead of values

    Returns:
    - List of per-level aggregates OR level number (if return_level=True)
    """
    if not root:
        return [] if not return_level else 0

    queue = deque([root])
    level = 1
    res = []
    best_value = float('-inf') if aggregate in ['sum', 'max'] else float('inf')
    best_level = 1

    while queue:
        level_sum = 0
        level_count = len(queue)

        # Process all nodes at the current level
        for _ in range(level_count):
            node = queue.popleft()
            level_sum += node.val  # for sum/average/max/min calculations

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Compute aggregate
        if aggregate == 'sum':
            value = level_sum
        elif aggregate == 'average':
            value = level_sum / level_count
        elif aggregate == 'max':
            value = max(node.val for node in range(level_count))  # example, rarely used
        elif aggregate == 'min':
            value = min(node.val for node in range(level_count))  # example, rarely used
        else:
            value = level_sum

        res.append(value)

        # Track best level for sum (used in Max Level Sum problem)
        if return_level:
            if value > best_value:
                best_value = value
                best_level = level

        level += 1

    return best_level if return_level else res



#1. Level Averages
averages = bfs_level_aggregate(root, aggregate='average')
print(averages)  # e.g., [3.0, 14.5, 11.0]

#2. Maximum Level Sum (Return Level Number)
max_level = bfs_level_aggregate(root, aggregate='sum', return_level=True)
print(max_level)  # e.g., 2
