// ============================================================
//  Sorting algorithms in Scilab
//  3 iterative (loops) + 3 recursive
//  Run with: exec("sorting_algorithms.sce", -1)
// ============================================================


// ############################################################
//  PART 1 : ITERATIVE VERSIONS (loops)
// ############################################################

// ---------- 1) Bubble sort (iterative) ----------
function T = bubble_sort(T)
    n = length(T);
    for i = 1:n-1
        swapped = %f;
        for j = 1:n-i
            if T(j) > T(j+1) then
                tmp = T(j); T(j) = T(j+1); T(j+1) = tmp;
                swapped = %t;
            end
        end
        if ~swapped then break; end   // already sorted
    end
endfunction


// ---------- 2) Selection sort (iterative) ----------
function T = selection_sort(T)
    n = length(T);
    for i = 1:n-1
        m = i;                         // index of the minimum
        for j = i+1:n
            if T(j) < T(m) then m = j; end
        end
        if m <> i then
            tmp = T(i); T(i) = T(m); T(m) = tmp;
        end
    end
endfunction


// ---------- 3) Insertion sort (iterative) ----------
function T = insertion_sort(T)
    n = length(T);
    for i = 2:n
        key = T(i);
        j = i - 1;
        while j >= 1
            if T(j) <= key then break; end
            T(j+1) = T(j);
            j = j - 1;
        end
        T(j+1) = key;
    end
endfunction


// ############################################################
//  PART 2 : RECURSIVE VERSIONS
// ############################################################

// ---------- 4) Quick sort (recursive) ----------
function R = quick_sort(T)
    n = length(T);
    if n <= 1 then
        R = T;
        return;
    end
    p    = T(1);                       // pivot
    rest = T(2:n);
    left  = rest(rest <  p);
    right = rest(rest >= p);
    R = [quick_sort(left), p, quick_sort(right)];
endfunction


// ---------- helper for merge sort ----------
function R = merge_arrays(A, B)
    na = length(A); nb = length(B);
    R = zeros(1, na + nb);
    i = 1; j = 1; k = 1;
    while i <= na & j <= nb
        if A(i) <= B(j) then
            R(k) = A(i); i = i + 1;
        else
            R(k) = B(j); j = j + 1;
        end
        k = k + 1;
    end
    while i <= na
        R(k) = A(i); i = i + 1; k = k + 1;
    end
    while j <= nb
        R(k) = B(j); j = j + 1; k = k + 1;
    end
endfunction

// ---------- 5) Merge sort (recursive) ----------
function R = merge_sort(T)
    n = length(T);
    if n <= 1 then
        R = T;
        return;
    end
    m = floor(n / 2);
    A = merge_sort(T(1:m));
    B = merge_sort(T(m+1:n));
    R = merge_arrays(A, B);
endfunction


// ---------- 6) Bubble sort (recursive) ----------
// One pass pushes the biggest element to the end,
// then we call the function again on the first n-1 elements.
function T = bubble_sort_rec(T, n)
    if argn(2) < 2 then n = length(T); end
    if n <= 1 then return; end
    for j = 1:n-1
        if T(j) > T(j+1) then
            tmp = T(j); T(j) = T(j+1); T(j+1) = tmp;
        end
    end
    T = bubble_sort_rec(T, n-1);
endfunction


// ############################################################
//  PART 3 : ADDITIONAL ALGORITHMS
// ############################################################

// ---------- 7) Random sort / Bogo sort ----------
function T = random_sort(T, max_attempts)
    if argn(2) < 2 then max_attempts = 100000; end
    n = length(T);
    attempts = 0;
    while %t
        // check if sorted
        is_sorted = %t;
        for i = 1:n-1
            if T(i) > T(i+1) then
                is_sorted = %f;
                break;
            end
        end
        if is_sorted then break; end
        // random shuffle via permutation
        p = grand(1, "prm", 1:n);
        T = T(p);
        attempts = attempts + 1;
        if attempts >= max_attempts then
            mprintf("Random sort reached max attempts (%d)\n", max_attempts);
            break;
        end
    end
endfunction


// ---------- 8) Heap sort (iterative / heapify) ----------
function T = heapify(T, n, i)
    largest = i;
    left  = 2 * i;
    right = 2 * i + 1;
    if left <= n & T(left) > T(largest) then
        largest = left;
    end
    if right <= n & T(right) > T(largest) then
        largest = right;
    end
    if largest <> i then
        tmp = T(i); T(i) = T(largest); T(largest) = tmp;
        T = heapify(T, n, largest);
    end
endfunction

function T = heap_sort(T)
    n = length(T);
    for i = floor(n / 2):-1:1
        T = heapify(T, n, i);
    end
    for i = n:-1:2
        tmp = T(1); T(1) = T(i); T(i) = tmp;
        T = heapify(T, i - 1, 1);
    end
endfunction


// ---------- 9) Shell sort (diminishing gap) ----------
function T = shell_sort(T)
    n = length(T);
    gap = floor(n / 2);
    while gap > 0
        for i = gap+1:n
            temp = T(i);
            j = i;
            while j > gap & T(j - gap) > temp
                T(j) = T(j - gap);
                j = j - gap;
            end
            T(j) = temp;
        end
        gap = floor(gap / 2);
    end
endfunction


// ---------- 10) Cocktail shaker sort ----------
function T = cocktail_shaker_sort(T)
    n = length(T);
    start_idx = 1;
    end_idx = n;
    swapped = %t;
    while swapped
        swapped = %f;
        for i = start_idx:end_idx-1
            if T(i) > T(i+1) then
                tmp = T(i); T(i) = T(i+1); T(i+1) = tmp;
                swapped = %t;
            end
        end
        if ~swapped then break; end

        swapped = %f;
        end_idx = end_idx - 1;
        for i = end_idx-1:-1:start_idx
            if T(i) > T(i+1) then
                tmp = T(i); T(i) = T(i+1); T(i+1) = tmp;
                swapped = %t;
            end
        end
        start_idx = start_idx + 1;
    end
endfunction


// ---------- 11) Comb sort ----------
function T = comb_sort(T)
    n = length(T);
    gap = n;
    shrink = 1.3;
    sorted_flag = %f;
    while ~sorted_flag
        gap = floor(gap / shrink);
        if gap <= 1 then
            gap = 1;
            sorted_flag = %t;
        end
        for i = 1:n-gap
            if T(i) > T(i+gap) then
                tmp = T(i); T(i) = T(i+gap); T(i+gap) = tmp;
                sorted_flag = %f;
            end
        end
    end
endfunction


// ############################################################
//  BENCHMARK : measure execution time
// ############################################################

// Demo of Random sort on small array (excluded from large benchmark due to O((n+1)!))
small_test = grand(1, 6, "uin", 1, 99);
mprintf("=== Random sort (Bogo sort) on small vector (n=6) ===\n");
mprintf("Before: "); disp(small_test);
res_bogo = random_sort(small_test);
mprintf("After:  "); disp(res_bogo);
mprintf("\n");

names = ["bubble_sort", "selection_sort", "insertion_sort", ..
         "cocktail_shaker_sort", "comb_sort", "shell_sort", ..
         "heap_sort", "quick_sort", "merge_sort"];
sizes    = [500, 1000, 2000, 3000, 5000, 8000];
nb_algo  = length(names);

times = zeros(nb_algo, length(sizes));
rand("seed", 1);

for k = 1:length(sizes)
    A = rand(1, sizes(k));
    for a = 1:nb_algo
        tic();
        R = evstr(names(a) + "(A)");
        times(a, k) = toc();
        // correctness check
        if or(R <> gsort(A, "g", "i")) then
            mprintf("WARNING: %s gave a wrong result!\n", names(a));
        end
    end
    mprintf("n = %4d done\n", sizes(k));
end

// ---------- print results table ----------
mprintf("\nExecution time (seconds):\n");
mprintf("%-24s", "Algorithm \\ n");
for k = 1:length(sizes)
    mprintf("%10d", sizes(k));
end
mprintf("\n");
for a = 1:nb_algo
    mprintf("%-24s", names(a));
    for k = 1:length(sizes)
        mprintf("%10.4f", times(a, k));
    end
    mprintf("\n");
end


// ############################################################
//  PLOT  (Scilab-native syntax)
// ############################################################

// Scilab built-in color indices
algo_colors = [5, 2, 3, 4, 6, 7, 1, 9, 13];

scf(1); clf();

for a = 1:nb_algo
    plot2d(sizes', times(a,:)', style = algo_colors(modulo(a-1, length(algo_colors)) + 1));
end

// axis labels & title
xlabel("Array size  n",              "fontsize", 3);
ylabel("Execution time  (seconds)",  "fontsize", 3);
title("Sorting Algorithms – Execution Time", "fontsize", 4);

// grid
xgrid(color("grey70"));

// legend: one label per algorithm, upper-left corner (pos = 2)
leg_names = strsubst(names, "_", " ");
legend(leg_names, 2);

// resize the figure window
gcf().figure_size = [950, 650];
