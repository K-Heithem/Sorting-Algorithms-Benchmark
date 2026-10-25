# ============================================================
#  Sorting algorithms in Python
#  Iterative + Recursive + Advanced (Heap, Shell, Cocktail Shaker, Comb, Random Sort)
#  Run with: python sorting_algorithms.py
# ============================================================

import time
import random
import sys
import matplotlib
matplotlib.use("Agg")          # use non-interactive backend (safe in any terminal)
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ############################################################
#  PART 1 : ITERATIVE VERSIONS (loops)
# ############################################################

# ---------- 1) Bubble sort (iterative) ----------
def bubble_sort(arr):
    T = arr[:]
    n = len(T)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
                swapped = True
        if not swapped:
            break          # already sorted
    return T


# ---------- 2) Selection sort (iterative) ----------
def selection_sort(arr):
    T = arr[:]
    n = len(T)
    for i in range(n - 1):
        m = i              # index of the minimum
        for j in range(i + 1, n):
            if T[j] < T[m]:
                m = j
        if m != i:
            T[i], T[m] = T[m], T[i]
    return T


# ---------- 3) Insertion sort (iterative) ----------
def insertion_sort(arr):
    T = arr[:]
    n = len(T)
    for i in range(1, n):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    return T


# ############################################################
#  PART 2 : RECURSIVE VERSIONS
# ############################################################

# ---------- 4) Quick sort (recursive) ----------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[0]
    rest  = arr[1:]
    left  = [x for x in rest if x <  pivot]
    right = [x for x in rest if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


# ---------- helper for merge sort ----------
def merge_arrays(A, B):
    result = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i]); i += 1
        else:
            result.append(B[j]); j += 1
    result.extend(A[i:])
    result.extend(B[j:])
    return result


# ---------- 5) Merge sort (recursive) ----------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    m = len(arr) // 2
    return merge_arrays(merge_sort(arr[:m]), merge_sort(arr[m:]))


# ---------- 6) Bubble sort (recursive) ----------
def bubble_sort_rec(arr, n=None):
    T = arr[:] if n is None else arr          # copy only on first call
    if n is None:
        n = len(T)
    if n <= 1:
        return T
    for j in range(n - 1):
        if T[j] > T[j + 1]:
            T[j], T[j + 1] = T[j + 1], T[j]
    return bubble_sort_rec(T, n - 1)


# ############################################################
#  PART 3 : ADDITIONAL ALGORITHMS
# ############################################################

# ---------- 7) Random sort / Bogo sort (randomized) ----------
def is_sorted(arr):
    """Helper function to verify if an array is sorted in non-decreasing order."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def random_sort(arr, max_attempts=500_000):
    """
    Random Sort (also known as Bogo Sort or Permutation Sort).
    Randomly shuffles the array until it is found to be in sorted order.
    Complexity: Best O(n), Average O((n+1)!), Worst Unbounded.
    Includes a safety max_attempts threshold to prevent infinite loops.
    """
    T = arr[:]
    attempts = 0
    while not is_sorted(T):
        random.shuffle(T)
        attempts += 1
        if max_attempts and attempts >= max_attempts:
            raise TimeoutError(f"Random sort exceeded {max_attempts:,} shuffles without finding a sorted permutation.")
    return T


# ---------- 8) Heap sort (iterative / heapify) ----------
def heap_sort(arr):
    """
    Heap Sort: In-place comparison sort using a max-heap binary tree structure.
    Complexity: O(n log n) best, average, and worst case.
    """
    T = arr[:]
    n = len(T)

    def heapify(data, heap_size, root_idx):
        largest = root_idx
        left = 2 * root_idx + 1
        right = 2 * root_idx + 2

        if left < heap_size and data[left] > data[largest]:
            largest = left
        if right < heap_size and data[right] > data[largest]:
            largest = right

        if largest != root_idx:
            data[root_idx], data[largest] = data[largest], data[root_idx]
            heapify(data, heap_size, largest)

    # 1. Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(T, n, i)

    # 2. Extract elements one by one from heap
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]  # Move current root to end
        heapify(T, i, 0)         # Call heapify on the reduced heap

    return T


# ---------- 9) Shell sort (diminishing gap) ----------
def shell_sort(arr):
    """
    Shell Sort: Generalization of insertion sort that compares and swaps
    elements separated by a decreasing gap sequence.
    Complexity: O(n log^2 n) to O(n^(3/2)) depending on gap sequence.
    """
    T = arr[:]
    n = len(T)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = T[i]
            j = i
            while j >= gap and T[j - gap] > temp:
                T[j] = T[j - gap]
                j -= gap
            T[j] = temp
        gap //= 2

    return T


# ---------- 10) Cocktail shaker sort (bidirectional bubble) ----------
def cocktail_shaker_sort(arr):
    """
    Cocktail Shaker Sort (Bidirectional Bubble Sort).
    Alternates passes from left-to-right and right-to-left, solving
    the 'turtles' problem (small items near the end).
    Complexity: Best O(n), Average/Worst O(n^2).
    """
    T = arr[:]
    n = len(T)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False
        # Forward pass (bubbles largest element to the end)
        for i in range(start, end):
            if T[i] > T[i + 1]:
                T[i], T[i + 1] = T[i + 1], T[i]
                swapped = True
        if not swapped:
            break

        swapped = False
        end -= 1

        # Backward pass (bubbles smallest element to the beginning)
        for i in range(end - 1, start - 1, -1):
            if T[i] > T[i + 1]:
                T[i], T[i + 1] = T[i + 1], T[i]
                swapped = True
        start += 1

    return T


# ---------- 11) Comb sort (gapped bubble sort) ----------
def comb_sort(arr):
    """
    Comb Sort: Improves bubble sort by using a shrink factor gap (1.3),
    eliminating turtles fast before falling back to gap=1.
    Complexity: Best O(n log n), Average O(n^2 / 2^p) ~ O(n log n), Worst O(n^2).
    """
    T = arr[:]
    n = len(T)
    gap = n
    shrink = 1.3
    sorted_flag = False

    while not sorted_flag:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True

        for i in range(n - gap):
            if T[i] > T[i + gap]:
                T[i], T[i + gap] = T[i + gap], T[i]
                sorted_flag = False

    return T


# ############################################################
#  DEMO FOR RANDOM SORT (BOGO SORT) & RECURSIVE BUBBLE
# ############################################################

print("=" * 60)
print(" 1) RANDOM SORT (BOGO SORT) DEMONSTRATION")
print("=" * 60)
small_demo = [random.randint(1, 99) for _ in range(6)]
print(f"Original array (n=6)   : {small_demo}")
t0_bogo = time.perf_counter()
sorted_bogo = random_sort(small_demo)
t_bogo = time.perf_counter() - t0_bogo
print(f"Bogo-sorted result     : {sorted_bogo}  (took {t_bogo:.4f} s)")
print("Note: Random sort has O((n+1)!) average complexity.")
print("      It is excluded from n=500..8000 benchmark for obvious runtime reasons.\n")


# ############################################################
#  BENCHMARK
# ############################################################

# NOTE: bubble_sort_rec is excluded because it recurses n times (stack overflow).
#       random_sort (bogo sort) is excluded because O((n+1)!) would never finish.
algorithms = {
    "Bubble Sort":          bubble_sort,
    "Selection Sort":       selection_sort,
    "Insertion Sort":       insertion_sort,
    "Cocktail Shaker Sort": cocktail_shaker_sort,
    "Comb Sort":            comb_sort,
    "Shell Sort":           shell_sort,
    "Heap Sort":            heap_sort,
    "Quick Sort":           quick_sort,
    "Merge Sort":           merge_sort,
}

sizes = [500, 1_000, 2_000, 3_000, 5_000, 8_000]

sys.setrecursionlimit(20_000)

times = {name: [] for name in algorithms}

random.seed(1)

for n in sizes:
    base = [random.random() for _ in range(n)]   # same array for all algos
    for name, func in algorithms.items():
        arr = base[:]
        try:
            t0 = time.perf_counter()
            result = func(arr)
            elapsed = time.perf_counter() - t0
            times[name].append(elapsed)
            # correctness check
            if result != sorted(base):
                print(f"WARNING: {name} gave a wrong result!")
        except (RecursionError, OverflowError, MemoryError):
            times[name].append(None)   # stack overflow — skip gracefully
            print(f"  [{name}] skipped at n={n} (stack overflow)")

    print(f"n = {n:6,d}  done")

# ---------- print table ----------
col_w = 10
print(f"\nExecution time (seconds):")
print(f"{'Algorithm':<26}", end="")
for n in sizes:
    print(f"{n:{col_w},d}", end="")
print()
print("-" * (26 + col_w * len(sizes)))
for name, t_list in times.items():
    print(f"{name:<26}", end="")
    for t in t_list:
        if t is None:
            print(f"{'OVERFLOW':>{col_w}}", end="")
        else:
            print(f"{t:{col_w}.4f}", end="")
    print()


# ############################################################
#  PLOT  (matplotlib)
# ############################################################

COLORS = [
    "#ff4f6d",  # Bubble
    "#ff9f43",  # Selection
    "#ffd32a",  # Insertion
    "#e84393",  # Cocktail Shaker
    "#fd79a8",  # Comb
    "#00cec9",  # Shell
    "#a29bfe",  # Heap
    "#2ecc71",  # Quick
    "#5b8cf5",  # Merge
]
MARKERS = ["o", "s", "^", "v", "<", ">", "D", "x", "P"]
LINES   = ["-", "--", "-.", ":", "-", "--", "-.", "-", "--"]

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#161b22")

for idx, (name, t_list) in enumerate(times.items()):
    valid = [(s, t) for s, t in zip(sizes, t_list) if t is not None]
    if not valid:
        continue
    xs, ys = zip(*valid)
    ax.plot(
        xs, ys,
        color     = COLORS[idx % len(COLORS)],
        marker    = MARKERS[idx % len(MARKERS)],
        linestyle = LINES[idx % len(LINES)],
        linewidth = 2,
        markersize= 6,
        label     = name,
    )

# --- styling ---
ax.set_xlabel("Array size  n",             color="#c9d1d9", fontsize=12, labelpad=8)
ax.set_ylabel("Execution time  (seconds)", color="#c9d1d9", fontsize=12, labelpad=8)
ax.set_title("Sorting Algorithms – Execution Time",
             color="#f0f6fc", fontsize=15, fontweight="bold", pad=14)

ax.tick_params(colors="#8b949e", labelsize=10)
for spine in ax.spines.values():
    spine.set_edgecolor("#30363d")

ax.grid(color="#30363d", linestyle="--", linewidth=0.7, alpha=0.8)
ax.xaxis.set_major_locator(ticker.FixedLocator(sizes))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

legend = ax.legend(
    framealpha=0.15,
    facecolor="#161b22",
    edgecolor="#30363d",
    labelcolor="#c9d1d9",
    fontsize=9.5,
    loc="upper left",
)

plt.tight_layout()
plt.savefig("benchmark_chart.png", dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
print("\nChart saved to  benchmark_chart.png")
