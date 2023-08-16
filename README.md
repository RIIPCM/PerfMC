# PerfMC.py
**`PerfMC.py`** is a python module for our algorithm for the ranking pairwise comparisons matrices in Saaty Scale.

## How to use it?
-	It supports pairwise comparison matrices from 3x3 to 10x10 in **Saaty scale**
-	run one of functions for n size matrix, the output will be rankings for generated matrices

## Important note
-	Numbers in Saaty scale are (1,2,3,4,5,6,7,8,9, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9)
-	to avoid problems with comparing values, numbers are not rounded but write as **Fraction**
-	If you want to load matrices from file set parameter filePath.
-	Algorithm support csv files separated by semicolons, and values must be write as **Fraction** e.g. 0.2 as 1/5

## Ranking Algorithm with Step-by-Step Revealed Preferences for 3x3 and 4x4 size
**output_for_n3()** : This function will use all possible matrices from 3x3 size
-	function will ask for matrix element a[ i,j ] (above diagonal) from the available matrix elements
-	in next step function will ask for value from Saaty scale
-	output will be printed rankings for all generated matrices with selected elements, weights of all objects (vectors)

**output_for_n4()** : This function will use all possible matrices from 4x4 size. Note that there are 17^6 possible matrices, then it can take while to calculate rankings.
-	function will ask for matrix index (above diagonal) from the available matrix elements
-	in next step function will ask for value from Saaty scale
-	in each step function will ask if you want to run calculations or to go to the next element
-	output will be printed rankings for all generated matrices with selected elements, weights of all objects (vectors)

## Ranking Algorithm with Step-by-Step Revealed Preferences for 5x5 to 10x10 size
**Function:**
- `output_for_n5(filePath=None, loops=1000000, a12=None,...)`
- `output_for_n6(filePath=None, loops=1000000, a12=None,...)`
- `output_for_n7(filePath=None, loops=1000000, a12=None,...)`
- `output_for_n8(filePath=None, loops=1000000, a12=None,...)`
- `output_for_n9(filePath=None, loops=1000000, a12=None,...)`
- `output_for_n10(filePath=None, loops=1000000, a12=None,...)`

**Parameters:**
- `filePath`: Path to the matrix file in csv, separatted by semicolon. If None, auto-generated matrices are used.
- `loops`: Number of matrices to generate. Default is 1,000,000.
- `a12, a13, ...`: Values of selected elements a[ i,j ] above the diagonal. If set to None, it auto-generates random indices from the Saaty scale.
  - for 10x10, indices with 10 are written as 'A'

**Example of matrice indices for 5x5**
| a11  | a12 | a13 | a14 | a15 |
| --- | --- | --- | --- | --- |
|      | a22 | a23 | a24 | a25 |
|      |     | a33 | a34 | a35 |
|      |     |     | a44 | a45 |
|      |     |     |     | a55 |

**Example of matrice indices for 10x10**
| a11  | a12 | a13 | a14 | a15 | a16 | a17 | a18 | a19 | a1A |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   | a22 | a23 | a24 | a25 | a26 | a27 | a28 | a29 | a2A |
|   |  | a33 | a34 | a35 | a36 | a37 | a38 | a39 | a3A |
|   |  |  | a44 | a45 | a46 | a47 | a48 | a49 | a4A |
|   |  |  |  | a55 | a56 | a57 | a58 | a59 | a5A |
|   |  |  |  |  | a66 | a67 | a68 | a69 | a6A |
|   |  |  |  |  |  | a77 | a78 | a79 | a7A |
|   |  |  |  |  |  |  | a88 | a89 | a8A |
|   |  |  |  |  |  |  |  | a99 | a9A |
|   |  |  |  |  | |  |  |  | aA |
 
**Return:**
- Rankings for generated matrices based on selected elements:
  - `percentages` as Type list eg. `[0.0, 0.111, ...]`
- Permutations list:
  - `permutations_list` as Type list of tuples eg. `[('A', 'B', 'C', 'D', 'E'), ('A', 'B', 'C', 'E', 'D') , ... ]`
- Weights of all objects (vectors) with n size of matrix eg:
  - `min_values` as Array of float64 eg. `[8.2424160719140, 5.62966884715, 4.3813015415, 1.126765779, 6.2814413042]`
  - `max_values` as Array of float64 eg. `[2.8348217440118, 4.73348015472, 3.0547544898, 4.549693518, 4.0544601034]`
  - `avg_values` as Array of float64 eg. `[1.8353850753244, 2.22047015985, 1.7047819104, 2.466579267, 1.7727835873]`
  
## Example
* Generator for all 3x3 matrices
```
import PerfMC
PerfMC.output_for_n3()
```
And the output should be
```
Choose one value: A12
Selected: A12
Write one value from the SAATy scale: 5
('A', 'B', 'C') 32.34015440%
('A', 'C', 'B') 35.05807541%
('B', 'A', 'C') 0.09388521%
('B', 'C', 'A') 0.07384538%
('C', 'A', 'B') 32.34015440%
('C', 'B', 'A') 0.09388521%
Vector A:
  Max: 0.7694828147267339
  Min: 0.15139524835670604
  Avg: 0.484582112773771

Vector B:
  Max: 0.4014674224791505
  Min: 0.051776446626222425
  Avg: 0.18205143505965954

Vector C:
  Max: 0.7968283050170716
  Min: 0.0461829440043201
  Avg: 0.33336645216656924

Available indices: ['A13', 'A23']
Choose one value: 
```
* Generator for 5x5 matrices with elements: loops=100, a14=1/2 , a15=2
```
import PerfMC

percentages, permutations_list, minv, maxv, avgv = PerfMC.output_for_n5(loops=1000,a14=1/2,a15=2)
for percentage, permutation in zip(percentages, permutations_list):
     if percentage>0:
       print(permutation, f'{percentage:.8f}%')

letters = ['A', 'B', 'C', 'D','E']

for i, (max_val, min_val, avg_val) in enumerate(zip(maxv, minv, avgv)):
    print(f"Vector {letters[i]}:")
    print(f"  Max: {max_val}")
    print(f"  Min: {min_val}")
    print(f"  Avg: {avg_val}\n")

```
And the output should be list of probability rankings, list of permutations and list of weights (min, max, avg) of vectors:
```
('A', 'D', 'E', 'C', 'B') 41.15629593%
('B', 'C', 'D', 'E', 'A') 2.74375306%
('B', 'D', 'C', 'A', 'E') 9.14584354%
('D', 'A', 'E', 'C', 'B') 41.15629593%
('E', 'B', 'A', 'D', 'C') 5.14453699%
('E', 'D', 'A', 'C', 'B') 0.65327454%
Vector A:
  Max: 0.3226619844796927
  Min: 0.07944837806631484
  Avg: 0.16632899626630648

Vector B:
  Max: 0.6006346171435221
  Min: 0.0611330144073739
  Avg: 0.2954819767344667

Vector C:
  Max: 0.2740980011998804
  Min: 0.041495317945437704
  Avg: 0.1340660269444714

Vector D:
  Max: 0.3226619844796927
  Min: 0.12539470692548724
  Avg: 0.19619181927823104

Vector E:
  Max: 0.3494146108029695
  Min: 0.06021061140874737
  Avg: 0.20793118077652437

```
Note that it's possible that there are no matrices with given elements in generated loop or in file
```
PerfMC.MatrixIndexError: No matrices with given indice(s)
```
* Example of matrices n5 in csv file.
```
1;1/2;1;1;6;2;1;1/9;1;1/3;1;9;1;1/8;1/3;1;1;8;1;1/5;1/6;3;3;5;1
1;1/3;1/9;1/9;1/3;3;1;9;1/2;2;9;1/9;1;4;1/4;9;2;1/4;1;6;3;1/2;4;1/6;1
1;2;1/6;1;3;1/2;1;1/4;1;5;6;4;1;1/5;1/3;1;1;5;1;1/5;1/3;1/5;3;5;1
```


## 🛡 License
This project is licensed under the terms of the `MIT` license
