# ⚡ Sorting Algorithms & Complexity Benchmark

A comprehensive collection and benchmarking suite of classic and advanced sorting algorithms implemented in **Python** and **Scilab**, accompanied by an interactive **HTML/JS complexity dashboard** and visual benchmark charts.

---

## 🚀 Features

- **Implementations**:
  - **Iterative Sorts**: Bubble Sort, Selection Sort, Insertion Sort, Shell Sort, Cocktail Shaker Sort, Comb Sort, Gnome Sort.
  - **Divide & Conquer / Advanced**: Merge Sort, Quick Sort, Heap Sort, Counting Sort, Radix Sort, Bucket Sort, Random Sort (Bogo).
  - **Scilab Script**: Equivalent algorithmic implementations (`sorting_algorithms.sce`).
- **Performance Benchmarks**:
  - Empirical runtime measurement across input sizes ($N \in [100, 5000]$).
  - Generated comparison chart (`benchmark_chart.png`).
- **Interactive Visualizer & Complexity Reference**:
  - `sorting_complexity.html`: Modern, responsive dashboard comparing time complexities ($O(n \log n)$, $O(n^2)$, etc.), space complexity, stability, and algorithmic properties.

---

## 📁 Project Structure

```text
├── sorting_algorithms.py      # Main Python implementations and benchmarking script
├── sorting_algorithms.sce     # Scilab script for algorithmic analysis
├── sorting_complexity.html    # Interactive complexity comparison web dashboard
├── benchmark_chart.png        # Benchmark runtime visual analysis
├── new.py                     # Utility / test script
├── Tp1.txt                    # Project notes / specifications
└── sync-github.bat            # One-click script to push latest updates to GitHub
```

---

## 🛠️ Usage

### Run Python Benchmarks:
```bash
python sorting_algorithms.py
```

### View Interactive Visualizer:
Simply open `sorting_complexity.html` in your web browser.

---

## 🔄 Automatic GitHub Sync
To sync any new changes or progress to GitHub at any time, run:
```bash
./sync-github.bat
```
or execute:
```bash
git add .
git commit -m "Update progress"
git push origin main
```
