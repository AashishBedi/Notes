from collections import deque

def bfs_levels(root, mode='nodes', zigzag=False):
    """
    Generic BFS template for level-based tree problems.
a clean, reusable BFS template that covers all common level-based tree problems:

Level Order Traversal → get nodes per level

Zigzag Level Order → alternate left/right traversal

Level Sums → sum per level

Level Averages → average per level

Max Level Sum → find level with maximum sum



    Parameters:
    - root: TreeNode
    - mode: 'nodes', 'sum', 'average', 'max_level_sum'
        - 'nodes' → return list of nodes per level
        - 'sum' → return sum per level
        - 'average' → return average per level
        - 'max_level_sum' → return 1-based level number with max sum
    - zigzag: True → alternate left-right per level (Zigzag traversal)

    Returns:
    - List of per-level results or level number for max_level_sum
    """
    if not root:
        return [] if mode != 'max_level_sum' else 0

    queue = deque([root])
    res = []
    level = 1
    max_sum = root.val
    max_level = 1
    left_to_right = True  # For zigzag

    while queue:
        level_nodes = []
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_nodes.append(node.val)
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Zigzag handling
        if zigzag and not left_to_right:
            level_nodes.reverse()
        left_to_right = not left_to_right

        # Store results based on mode
        if mode == 'nodes':
            res.append(level_nodes)
        elif mode == 'sum':
            res.append(level_sum)
        elif mode == 'average':
            res.append(level_sum / len(level_nodes))
        elif mode == 'max_level_sum':
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

        level += 1

    if mode == 'max_level_sum':
        return max_level
    return res



'''
✅ Usage Examples
1️⃣ Level Order Traversal
bfs_levels(root, mode='nodes')
# Output: [[3], [9, 20], [15, 7]]

2️⃣ Zigzag Level Order
bfs_levels(root, mode='nodes', zigzag=True)
# Output: [[3], [20, 9], [15, 7]]

3️⃣ Level Sums
bfs_levels(root, mode='sum')
# Output: [3, 29, 22]

4️⃣ Level Averages
bfs_levels(root, mode='average')
# Output: [3.0, 14.5, 11.0]

5️⃣ Maximum Level Sum (Level Number)
bfs_levels(root, mode='max_level_sum')
# Output: 2


✅ Advantages

One template fits all level-based BFS problems.

Easy to toggle zigzag, sum/average/max level sum.

Very clean and readable for interviews.
'''