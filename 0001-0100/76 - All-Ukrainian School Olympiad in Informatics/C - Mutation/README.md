# C. Mutation

**Submission:** https://codeforces.com/contest/76/problem/C

**Limits:** 1 second / 256 megabytes

## Problem Statement

Scientists of planet Olympia are conducting an experiment in mutation of primitive organisms. Genome of organism from this planet can be represented as a string of the first K capital English letters. For each pair of types of genes they assigned a i ,ΓÇë j ΓÇö a risk of disease occurence in the organism provided that genes of these types are adjacent in the genome, where i ΓÇö the 1-based index of the first gene and j ΓÇö the index of the second gene. The gene 'A' has index 1, 'B' has index 2 and so on. For example, a 3,ΓÇë2 stands for the risk of 'CB' fragment. Risk of disease occurence in the organism is equal to the sum of risks for each pair of adjacent genes in the genome.

Scientists have already obtained a base organism. Some new organisms can be obtained by mutation of this organism. Mutation involves removal of all genes of some particular types. Such removal increases the total risk of disease occurence additionally. For each type of genes scientists determined t i ΓÇö the increasement of the total risk of disease occurence provided by removal of all genes having type with index i . For example, t 4 stands for the value of additional total risk increasement in case of removing all the 'D' genes.

Scientists want to find a number of different organisms that can be obtained from the given one which have the total risk of disease occurence not greater than T . They can use only the process of mutation described above. Two organisms are considered different if strings representing their genomes are different. Genome should contain at least one gene.

## Input

The first line of the input contains three integer numbers N ( 1ΓÇëΓëñΓÇë N ΓÇëΓëñΓÇë200ΓÇë000 ) ΓÇö length of the genome of base organism, K ( 1ΓÇëΓëñΓÇë K ΓÇëΓëñΓÇë22 ) ΓÇö the maximal index of gene type in the genome and T ( 1ΓÇëΓëñΓÇë T ΓÇëΓëñΓÇë2┬╖10 9 ) ΓÇö maximal allowable risk of disease occurence. The second line contains the genome of the given organism. It is a string of the first K capital English letters having length N .

The third line contains K numbers t 1 ,ΓÇë t 2 ,ΓÇë...,ΓÇë t K , where t i is additional risk value of disease occurence provided by removing of all genes of the i -th type.

The following K lines contain the elements of the given matrix a i ,ΓÇë j . The i -th line contains K numbers. The j -th number of the i -th line stands for a risk of disease occurence for the pair of genes, first of which corresponds to the i -th letter and second of which corresponds to the j -th letter. The given matrix is not necessarily symmetrical.

All the numbers in the input are integer, non-negative and all of them except T are not greater than 10 9 . It is guaranteed that the maximal possible risk of organism that can be obtained from the given organism is strictly smaller than 2 31 .

## Output

Output the number of organisms that can be obtained from the base one and which have the total risk of disease occurence not greater than T .

## Examples

Example 1:
```
5 3 13
BACAC
4 1 2
1 2 3
2 3 4
3 4 10
```
```
5
```

## Note

Explanation: one can obtain the following organisms (risks are stated in brackets): BACAC (11), ACAC (10), BAA (5), B (6), AA (4).
