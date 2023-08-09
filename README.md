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

## Ranking Algorithm with Step-by-Step Revealed Preferences
**output_for_n3()** : This function will use all possible matrices from 3x3 size
-	function will ask for matrix index (above diagonal) from the available indices
-	in next step function will ask for value from Saaty scale
-	output will be printed rankings for all generated matrices with selected indices, weights of all objects (vectors)

**output_for_n4()** : This function will use all possible matrices from 4x4 size. Note that there are 17^6 possible matrices, then it can take while to calculate rankings.
-	function will ask for matrix index (above diagonal) from the available indices
-	in next step function will ask for value from Saaty scale
-	in each step function will ask if you want to run calculations or to go to the next index
-	output will be printed rankings for all generated matrices with selected indices, weights of all objects (vectors)

**output_for_n5**`(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a23=None,a24=None,a25=None,a34=None,a35=None,a45=None)`
-	filePath: path to the matrix file (default None for auto generated matrices)
-	Loops: number of generated matrices (default 1000000)
-	a12,a13,a14,a15,a23,a24,a25,a34,a35,a45 – values of selected indices (default None, if none then it will generate random indices from Saaty scale)
-	function will return rankings for all generated matrices with selected indice(s), permutations list and weights of all objects (vectors)

**output_for_n6**`(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a16=None,a23=None,a24=None,a25=None,a26=None,a34=None,a35=None,a36=None,a45=None,a46=None,a56=None)`
-	filePath: path to the matrix file (default None for auto generated matrices)
-	Loops: number of generated matrices (default 1000000)
-	a12,a13,a14,a15,a16,a23,a24,a25,a26,a34,a35,a36,a45,a46,a56 – values of selected indices (default None, if none then it will generate random indices from Saaty scale)
-	function will return rankings for all generated matrices with selected indice(s), permutations list and weights of all objects (vectors)

**output_for_n7**`(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a16=None,a17=None,a23=None,a24=None,a25=None,a26=None,a27=None,a34=None,a35=None,a36=None,a37=None,a45=None,a46=None,a47=None,a56=None,a57=None,a67=None)`
-	filePath: path to the matrix file (default None for auto generated matrices)
-	Loops: number of generated matrices (default 1000000)
-	a12,a13,a14,a15,a16,a17,a23,a24,a25,a26,a27,a34,a35,a36,a37,a45,a46,a47,a56,a57,a67 – values of selected indices (default None, if none then it will generate random indices from Saaty scale)
-	function will return rankings for all generated matrices with selected indice(s), permutations list and weights of all objects (vectors)

**output_for_n8**`(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a16=None,a17=None,a18=None,a23=None,a24=None,a25=None,a26=None,a27=None,a28=None,a34=None,a35=None,a36=None,a37=None,a38=None,a45=None,a46=None,a47=None,a48=None,a56=None,a57=None,a58=None,a67=None,a68=None,a78=None)`
-	filePath: path to the matrix file (default None for auto generated matrices)
-	Loops: number of generated matrices (default 1000000)
-	a12,a13,a14,a15,a16,a17,a18,a23,a24,a25,a26,a27,a28,a34,a35,a36,a37,a38,a45,a46,a47,a48,a56,a57,a58,a67,a68,a78– values of selected indices (default None, if none then it will generate random indices from Saaty scale)
-	function will return rankings for all generated matrices with selected indice(s), permutations list and weights of all objects (vectors)

**output_for_n9**`(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a16=None,a17=None,a18=None,a19=None,a23=None,a24=None,a25=None,a26=None,a27=None,a28=None,a29=None,a34=None,a35=None,a36=None,a37=None,a38=None,a39=None,a45=None,a46=None,a47=None,a48=None,a49=None,a56=None,a57=None,a58=None,a59=None,a67=None,a68=None,a69=None,a78=None,a79=None,a89=None)`
-	filePath: path to the matrix file (default None for auto generated matrices)
-	Loops: number of generated matrices (default 1000000)
-	a12,a13,a14,a15,a16,a17,a18,a19,a23,a24,a25,a26,a27,a28,a29,a34,a35,a36,a37,a38,a39,a45,a46,a47,a48,a49,a56,a57,a58,a59,a67,a68,a69,a78,a79,a89 – values of selected indices (default None, if none then it will generate random indices from Saaty scale)
-	function will return rankings for all generated matrices with selected indice(s), permutations list and weights of all objects (vectors)

**output_for_n10**`(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a16=None,a17=None,a18=None,a19=None,a1A=None,a23=None,a24=None,a25=None,a26=None,a27=None,a28=None,a29=None,a2A=None,a34=None,a35=None,a36=None,a37=None,a38=None,a39=None,a3A=None,a45=None,a46=None,a47=None,a48=None,a49=None,a4A=None,a56=None,a57=None,a58=None,a59=None,a5A=None,a67=None,a68=None,a69=None,a6A=None,a78=None,a79=None,a7A=None,a89=None,a8A=None,a9A=None)`
-	filePath: path to the matrix file (default None for auto generated matrices)
-	Loops: number of generated matrices (default 1000000)
-	a12,a13,a14,a15,a16,a17,a18,a19,a1A,a23,a24,a25,a26,a27,a28,a29,a2A,a34,a35,a36,a37,a38,a39,a3A,a45,a46,a47,a48,a49,a4A,a56,a57,a58,a59,a5A,a67,a68,a69,a6A,a78,a79,a7A,a89,a8A,a9A – values of selected indices (default None, if none then it will generate random indices from Saaty scale)
-	function will return rankings for all generated matrices with selected indice(s), permutations list and weights of all objects (vectors)

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
* Generator for 5x5 matrices with indices: loops=100, a14=1/2 , a15=2
```
import PerfMC

percentages, permutations_list, minv, maxv, avgv = PerfMC.output_for_n5(loops=1000,a14=1/2,a15=2)
for percentage, permutation in zip(percentages, permutations_list):
     if percentage>0:
       print(permutation, f'{percentage:.8f}%')

```
And the output should be list of probability rankings, list of permutations and list of weights (min, max, avg) of vectors:
```
('A', 'B', 'C', 'D', 'E') 20.69839482%
('A', 'B', 'D', 'C', 'E') 12.61616446%
('B', 'E', 'C', 'A', 'D') 37.84849338%
('C', 'A', 'B', 'E', 'D') 22.07828781%
('D', 'E', 'A', 'B', 'C') 6.75865953%

```
Note that it's possible that there are no matrices with given indices in current loop
```
    raise MatrixIndexError("No matrices with given indice(s)")
PerfMC.MatrixIndexError: No matrices with given indice(s)
```
*Example of matrices n5 in file.
```
1;1/2;1;1;6;2;1;1/9;1;1/3;1;9;1;1/8;1/3;1;1;8;1;1/5;1/6;3;3;5;1
1;1/3;1/9;1/9;1/3;3;1;9;1/2;2;9;1/9;1;4;1/4;9;2;1/4;1;6;3;1/2;4;1/6;1
1;2;1/6;1;3;1/2;1;1/4;1;5;6;4;1;1/5;1/3;1;1;5;1;1/5;1/3;1/5;3;5;1
```

## 🛡 License
This project is licensed under the terms of the `MIT` license
