
import heapq


# Problem 1: Jump Game
def can_jump(nums):
    farthest = 0

    for index, jump in enumerate(nums):
        if index > farthest:
            return False

        farthest = max(farthest, index + jump)

        if farthest >= len(nums) - 1:
            return True

    return len(nums) <= 1


# Problem 2: Gas Station
def gas_station(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    total_tank = 0
    start = 0

    for index in range(len(gas)):
        total_tank += gas[index] - cost[index]

        if total_tank < 0:
            start = index + 1
            total_tank = 0

    return start


# Problem 3: Minimum Platforms
def minimum_platforms(arrival, departure):
    if not arrival:
        return 0

    arrival = sorted(arrival)
    departure = sorted(departure)

    platforms_needed = 0
    max_platforms = 0
    i = 0
    j = 0
    n = len(arrival)

    while i < n:
        if arrival[i] <= departure[j]:
            platforms_needed += 1
            max_platforms = max(
                max_platforms,
                platforms_needed
            )
            i += 1
        else:
            platforms_needed -= 1
            j += 1

    return max_platforms


# Problem 4: Huffman Coding
class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def huffman_codes(frequencies):
    if not frequencies:
        return {}

    heap = []

    for char, frequency in frequencies.items():
        node = HuffmanNode(char, frequency)
        heapq.heappush(heap, (frequency, len(heap), node))

    if len(heap) == 1:
        only_node = heap[0][2]
        return {only_node.char: "0"}

    while len(heap) > 1:
        _, _, left = heapq.heappop(heap)
        _, _, right = heapq.heappop(heap)

        merged = HuffmanNode(
            None,
            left.frequency + right.frequency
        )
        merged.left = left
        merged.right = right

        heapq.heappush(
            heap,
            (merged.frequency, len(heap), merged)
        )

    root = heap[0][2]
    codes = {}

    def generate_codes(node, code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = code
            return

        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    generate_codes(root, "")
    return codes


if __name__ == "__main__":
    print("Problem 1: Jump Game")
    print(can_jump([2, 3, 1, 1, 4]))
    print(can_jump([3, 2, 1, 0, 4]))

    print("\nProblem 2: Gas Station")
    print(gas_station(
        [1, 2, 3, 4, 5],
        [3, 4, 5, 1, 2]
    ))
    print(gas_station([2, 3, 4], [3, 4, 3]))

    print("\nProblem 3: Minimum Platforms")
    print(minimum_platforms(
        [900, 940, 950, 1100, 1500, 1800],
        [910, 1200, 1120, 1130, 1900, 2000]
    ))

    print("\nProblem 4: Huffman Coding")
    frequencies = {
        "a": 5,
        "b": 9,
        "c": 12,
        "d": 13,
        "e": 16,
        "f": 45
    }

    codes = huffman_codes(frequencies)

    for char in sorted(codes):
        print(f"{char}: {codes[char]}")
