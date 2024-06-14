# Peter-sort
Peter-sort is a Python package that provides implementations of three popular sorting algorithms: Bubble Sort, Quick Sort, and Insertion Sort. These algorithms can be used to sort lists of numbers efficiently.

## Table of Contents

- [Installation](##installation)
- [Usage](##usage)
- [Sorting Algorithms](##sorting-algorithms)
  - [Bubble Sort](###bubble-sort)
  - [Quick Sort](###quick-sort)
  - [Insertion Sort](###insertion-sort)
- [Contributing](##contributing)
- [License](##license)

## Installation

You can install the Peter-Sort package using pip:

```bash
pip install peter-sort
```

## Usage

Heres how you use the package

```bash
from sort.bubble_sort import bubble_sort
from sort.insertion_sort import insertion_sort
from sort.quick_sort import quick_sort

numbers = [64, 34, 25, 12, 22, 11, 90]
```
and call the command or simply use the test file provided

## Sorting Algorithms
### Bubble Sort
Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
### Quick Sort
Quick Sort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.
### Insertion Sort
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Explanation

1. **Installation**: Provides the command to install the package using pip.
2. **Usage**: Shows how to import and use the sorting functions provided by the package.
3. **Sorting Algorithms**: Describes each sorting algorithm, including a brief explanation and usage example.
4. **Contributing**: Encourages contributions and provides a link to the GitHub repository.
5. **License**: Mentions the license under which the package is distributed.

This `README.md` file should help users understand what the `peter-sort` package does and how to use it effectively.

