# -*- coding: utf-8 -*-
"""
v1.0
@authors: Bartosz Kowal, Krzysztof Smalara: RZESZOW UNIVERSITY OF TECHNOLOGY, Poland
Jiří Mazurek: Silesian University in Opava, Czech Republic  
"""
#####
#to floats
from fractions import Fraction 

#### for permutations generator
from itertools import permutations

#for geometric vectors
from scipy.stats.mstats import gmean
import numpy as np

import csv
# for random generator
import random  
#####

def generator_matrices_n3(a12=None, a13=None, a23=None):
    if a12 is None:
        a12_values = [1,2,3,4,5,6,7,8,9,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9]
    else:
        a12_values = [a12]

    if a13 is None:
        a13_values = [1,2,3,4,5,6,7,8,9,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9]
    else:
        a13_values = [a13]

    if a23 is None:
        a23_values = [1,2,3,4,5,6,7,8,9,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9]
    else:
        a23_values = [a23]

    perm_index_table=[0]*6

    for a12_val in a12_values:
        for a13_val in a13_values:
            for a23_val in a23_values:
                A = [1, a12_val, a13_val]
                B = [1/a12_val, 1, a23_val]
                C = [1/a13_val, 1/a23_val, 1]

                row=A+B+C

                KI=Koczkodaj_index_list(row)

                vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))

                perms_calculated_table = permutations_for(vectors,KI)
                perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
    

    total = sum(perm_index_table)


    percentages = [(num / total) * 100 for num in perm_index_table]
    
    permutations_list = list(permutations(['A','B','C']))
        
    for percentage, permutation in zip(percentages, permutations_list):
        print(permutation, f'{percentage:.8f}%')
                
                
def generator_matrices_n4(a12=None, a13=None, a14=None, a23=None , a24=None, a34=None):
    if a12 is None:
        a12_values = [1,2,3,4,5,6,7,8,9,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9]
    else:
        a12_values = [a12]

    if a13 is None:
        a13_values = [1,2,3,4,5,6,7,8,9,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9]
    else:
        a13_values = [a13]
        
    if a14 is None:
        a14_values = [1,2,3,4,5,6,7,8,9,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9]
    else:
        a14_values = [a14]    

    if a23 is None:
        a23_values = [1,2,3,4,5,6,7,8,9,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9]
    else:
        a23_values = [a23]
        
    if a24 is None:
        a24_values = [1,2,3,4,5,6,7,8,9,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9]
    else:
        a24_values = [a24]

    if a34 is None:
        a34_values = [1,2,3,4,5,6,7,8,9,1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9]
    else:
        a34_values = [a34]
    


    perm_index_table=[0]*24


    for a12_val in a12_values:
        for a13_val in a13_values:
            for a14_val in a14_values:
                for a23_val in a23_values:
                    for a24_val in a24_values:
                        for a34_val in a34_values:
                            A = [1,a12_val,a13_val,a14_val]
                            B = [1/a12_val,1,a23_val,a24_val]
                            C = [1/a13_val,1/a23_val,1,a34_val]
                            D = [1/a14_val,1/a24_val,1/a34_val,1]

                            row=A+B+C+D

                            KI=Koczkodaj_index_list(row)

                            vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))

                            
                            perms_calculated_table = permutations_for(vectors,KI)
                            perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]

                            
        

    total = sum(perm_index_table)

    percentages = [(num / total) * 100 for num in perm_index_table]

    permutations_list = list(permutations(['A','B','C','D']))
        
    
    for percentage, permutation in zip(percentages, permutations_list):
        print(permutation, f'{percentage:.8f}%')



                
def generator_random_matrices_n5():


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9]

    a12_val= random.choice(numbers)
    a13_val= random.choice(numbers)
    a14_val= random.choice(numbers)
    a15_val= random.choice(numbers)

    a23_val= random.choice(numbers)
    a24_val= random.choice(numbers)
    a25_val= random.choice(numbers)

    a34_val= random.choice(numbers)
    a35_val= random.choice(numbers)

    a45_val= random.choice(numbers)

    A=[1,a12_val,a13_val,a14_val,a15_val] 
    B=[1/a12_val,1,a23_val,a24_val,a25_val]
    C=[1/a13_val,1/a23_val,1,a34_val,a35_val]
    D=[1/a14_val,1/a24_val,1/a34_val,1,a45_val]
    E=[1/a15_val,1/a25_val,1/a35_val,1/a45_val,1]

    row=A+B+C+D+E   
    
    return row


def generator_random_matrices_n6():


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9]

    a12_val= random.choice(numbers)
    a13_val= random.choice(numbers)
    a14_val= random.choice(numbers)
    a15_val= random.choice(numbers)
    a16_val= random.choice(numbers)

    a23_val= random.choice(numbers)
    a24_val= random.choice(numbers)
    a25_val= random.choice(numbers)
    a26_val= random.choice(numbers)

    a34_val= random.choice(numbers)
    a35_val= random.choice(numbers)
    a36_val= random.choice(numbers)

    a45_val= random.choice(numbers)
    a46_val= random.choice(numbers)
    
    a56_val= random.choice(numbers)    

    A=[1        ,a12_val   ,a13_val   ,a14_val   ,a15_val   ,a16_val]
    
    B=[1/a12_val,1         ,a23_val   ,a24_val   ,a25_val   ,a26_val]
    
    C=[1/a13_val,1/a23_val ,1         ,a34_val   ,a35_val   ,a36_val]
    
    D=[1/a14_val,1/a24_val ,1/a34_val ,1         ,a45_val   ,a46_val]
    
    E=[1/a15_val,1/a25_val ,1/a35_val ,1/a45_val,1          ,a56_val]
    
    F=[1/a16_val,1/a26_val ,1/a36_val ,1/a46_val,1/a56_val  ,1]

    row=A+B+C+D+E+F   
    
    return row


def generator_random_matrices_n7():


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9]

    a12_val= random.choice(numbers)
    a13_val= random.choice(numbers)
    a14_val= random.choice(numbers)
    a15_val= random.choice(numbers)
    a16_val= random.choice(numbers)
    a17_val= random.choice(numbers)

    a23_val= random.choice(numbers)
    a24_val= random.choice(numbers)
    a25_val= random.choice(numbers)
    a26_val= random.choice(numbers)
    a27_val= random.choice(numbers)

    a34_val= random.choice(numbers)
    a35_val= random.choice(numbers)
    a36_val= random.choice(numbers)
    a37_val= random.choice(numbers)

    a45_val= random.choice(numbers)
    a46_val= random.choice(numbers)
    a47_val= random.choice(numbers)
    
    a56_val= random.choice(numbers) 
    a57_val= random.choice(numbers) 
    
    a67_val= random.choice(numbers) 

    A=[1        ,a12_val   ,a13_val   ,a14_val   ,a15_val   ,a16_val,    a17_val]
    
    B=[1/a12_val,1         ,a23_val   ,a24_val   ,a25_val   ,a26_val,    a27_val]
    
    C=[1/a13_val,1/a23_val ,1         ,a34_val   ,a35_val   ,a36_val,    a37_val]
    
    D=[1/a14_val,1/a24_val ,1/a34_val ,1         ,a45_val   ,a46_val,    a47_val]
    
    E=[1/a15_val,1/a25_val ,1/a35_val ,1/a45_val,1          ,a56_val,    a57_val]
    
    F=[1/a16_val,1/a26_val ,1/a36_val ,1/a46_val,1/a56_val  ,1      ,    a67_val]
    
    G=[1/a17_val,1/a27_val ,1/a37_val ,1/a47_val,1/a57_val  ,1/a67_val,  1]

    row=A+B+C+D+E+F+G
    
    return row
     
def generator_random_matrices_n8():


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9]

    a12_val= random.choice(numbers)
    a13_val= random.choice(numbers)
    a14_val= random.choice(numbers)
    a15_val= random.choice(numbers)
    a16_val= random.choice(numbers)
    a17_val= random.choice(numbers)
    a18_val= random.choice(numbers)

    a23_val= random.choice(numbers)
    a24_val= random.choice(numbers)
    a25_val= random.choice(numbers)
    a26_val= random.choice(numbers)
    a27_val= random.choice(numbers)
    a28_val= random.choice(numbers)

    a34_val= random.choice(numbers)
    a35_val= random.choice(numbers)
    a36_val= random.choice(numbers)
    a37_val= random.choice(numbers)
    a38_val= random.choice(numbers)

    a45_val= random.choice(numbers)
    a46_val= random.choice(numbers)
    a47_val= random.choice(numbers)
    a48_val= random.choice(numbers)
    
    a56_val= random.choice(numbers) 
    a57_val= random.choice(numbers) 
    a58_val= random.choice(numbers)
    
    a67_val= random.choice(numbers) 
    a68_val= random.choice(numbers)
    
    a78_val= random.choice(numbers)

    A=[1        ,a12_val   ,a13_val   ,a14_val   ,a15_val   ,a16_val,    a17_val,    a18_val]
    
    B=[1/a12_val,1         ,a23_val   ,a24_val   ,a25_val   ,a26_val,    a27_val,    a28_val]
    
    C=[1/a13_val,1/a23_val ,1         ,a34_val   ,a35_val   ,a36_val,    a37_val,    a38_val]
    
    D=[1/a14_val,1/a24_val ,1/a34_val ,1         ,a45_val   ,a46_val,    a47_val,    a48_val]
    
    E=[1/a15_val,1/a25_val ,1/a35_val ,1/a45_val,1          ,a56_val,    a57_val,    a58_val]
    
    F=[1/a16_val,1/a26_val ,1/a36_val ,1/a46_val,1/a56_val  ,1      ,    a67_val,    a68_val]
    
    G=[1/a17_val,1/a27_val ,1/a37_val ,1/a47_val,1/a57_val  ,1/a67_val,  1,          a78_val]
    
    H=[1/a18_val,1/a28_val ,1/a38_val ,1/a48_val,1/a58_val  ,1/a68_val,  1/a78_val, 1]

    row=A+B+C+D+E+F+G+H
    
    return row


def generator_random_matrices_n9():


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9]

    a12_val= random.choice(numbers)
    a13_val= random.choice(numbers)
    a14_val= random.choice(numbers)
    a15_val= random.choice(numbers)
    a16_val= random.choice(numbers)
    a17_val= random.choice(numbers)
    a18_val= random.choice(numbers)
    a19_val= random.choice(numbers)

    a23_val= random.choice(numbers)
    a24_val= random.choice(numbers)
    a25_val= random.choice(numbers)
    a26_val= random.choice(numbers)
    a27_val= random.choice(numbers)
    a28_val= random.choice(numbers)
    a29_val= random.choice(numbers)

    a34_val= random.choice(numbers)
    a35_val= random.choice(numbers)
    a36_val= random.choice(numbers)
    a37_val= random.choice(numbers)
    a38_val= random.choice(numbers)
    a39_val= random.choice(numbers)

    a45_val= random.choice(numbers)
    a46_val= random.choice(numbers)
    a47_val= random.choice(numbers)
    a48_val= random.choice(numbers)
    a49_val= random.choice(numbers)
    
    a56_val= random.choice(numbers) 
    a57_val= random.choice(numbers) 
    a58_val= random.choice(numbers)
    a59_val= random.choice(numbers)
    
    a67_val= random.choice(numbers) 
    a68_val= random.choice(numbers)
    a69_val= random.choice(numbers)
    
    a78_val= random.choice(numbers)
    a79_val= random.choice(numbers)
    
    a89_val= random.choice(numbers)

    A=[1        ,a12_val   ,a13_val   ,a14_val   ,a15_val   ,a16_val,    a17_val,    a18_val,   a19_val]
    
    B=[1/a12_val,1         ,a23_val   ,a24_val   ,a25_val   ,a26_val,    a27_val,    a28_val,   a29_val]
    
    C=[1/a13_val,1/a23_val ,1         ,a34_val   ,a35_val   ,a36_val,    a37_val,    a38_val,   a39_val]
    
    D=[1/a14_val,1/a24_val ,1/a34_val ,1         ,a45_val   ,a46_val,    a47_val,    a48_val,   a49_val]
    
    E=[1/a15_val,1/a25_val ,1/a35_val ,1/a45_val,1          ,a56_val,    a57_val,    a58_val,   a59_val]
    
    F=[1/a16_val,1/a26_val ,1/a36_val ,1/a46_val,1/a56_val  ,1      ,    a67_val,    a68_val,   a69_val]
    
    G=[1/a17_val,1/a27_val ,1/a37_val ,1/a47_val,1/a57_val  ,1/a67_val,  1,          a78_val,   a79_val]
    
    H=[1/a18_val,1/a28_val ,1/a38_val ,1/a48_val,1/a58_val  ,1/a68_val,  1/a78_val, 1       ,   a89_val]
    
    I=[1/a19_val,1/a29_val ,1/a39_val ,1/a49_val,1/a59_val  ,1/a69_val,  1/a79_val, 1 /a89_val,   1]

    row=A+B+C+D+E+F+G+H+I
    
    return row


def generator_random_matrices_n10():


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9]

    a12_val= random.choice(numbers)
    a13_val= random.choice(numbers)
    a14_val= random.choice(numbers)
    a15_val= random.choice(numbers)
    a16_val= random.choice(numbers)
    a17_val= random.choice(numbers)
    a18_val= random.choice(numbers)
    a19_val= random.choice(numbers)
    a1A_val= random.choice(numbers)

    a23_val= random.choice(numbers)
    a24_val= random.choice(numbers)
    a25_val= random.choice(numbers)
    a26_val= random.choice(numbers)
    a27_val= random.choice(numbers)
    a28_val= random.choice(numbers)
    a29_val= random.choice(numbers)
    a2A_val= random.choice(numbers)

    a34_val= random.choice(numbers)
    a35_val= random.choice(numbers)
    a36_val= random.choice(numbers)
    a37_val= random.choice(numbers)
    a38_val= random.choice(numbers)
    a39_val= random.choice(numbers)
    a3A_val= random.choice(numbers)

    a45_val= random.choice(numbers)
    a46_val= random.choice(numbers)
    a47_val= random.choice(numbers)
    a48_val= random.choice(numbers)
    a49_val= random.choice(numbers)
    a4A_val= random.choice(numbers)
    
    a56_val= random.choice(numbers) 
    a57_val= random.choice(numbers) 
    a58_val= random.choice(numbers)
    a59_val= random.choice(numbers)
    a5A_val= random.choice(numbers)
    
    a67_val= random.choice(numbers) 
    a68_val= random.choice(numbers)
    a69_val= random.choice(numbers)
    a6A_val= random.choice(numbers)
    
    a78_val= random.choice(numbers)
    a79_val= random.choice(numbers)
    a7A_val= random.choice(numbers)
    
    a89_val= random.choice(numbers)
    a8A_val= random.choice(numbers)
    
    a9A_val= random.choice(numbers)
    

    A=[1        ,a12_val   ,a13_val   ,a14_val   ,a15_val   ,a16_val,    a17_val,    a18_val,   a19_val,   a1A_val]
    
    B=[1/a12_val,1         ,a23_val   ,a24_val   ,a25_val   ,a26_val,    a27_val,    a28_val,   a29_val,   a2A_val]
    
    C=[1/a13_val,1/a23_val ,1         ,a34_val   ,a35_val   ,a36_val,    a37_val,    a38_val,   a39_val,   a3A_val]
    
    D=[1/a14_val,1/a24_val ,1/a34_val ,1         ,a45_val   ,a46_val,    a47_val,    a48_val,   a49_val,   a4A_val]
    
    E=[1/a15_val,1/a25_val ,1/a35_val ,1/a45_val,1          ,a56_val,    a57_val,    a58_val,   a59_val,   a5A_val]
    
    F=[1/a16_val,1/a26_val ,1/a36_val ,1/a46_val,1/a56_val  ,1      ,    a67_val,    a68_val,   a69_val,   a6A_val]
    
    G=[1/a17_val,1/a27_val ,1/a37_val ,1/a47_val,1/a57_val  ,1/a67_val,  1,          a78_val,   a79_val,   a7A_val]
    
    H=[1/a18_val,1/a28_val ,1/a38_val ,1/a48_val,1/a58_val  ,1/a68_val,  1/a78_val, 1       ,   a89_val,   a8A_val]
    
    I=[1/a19_val,1/a29_val ,1/a39_val ,1/a49_val,1/a59_val  ,1/a69_val,  1/a79_val, 1 /a89_val,   1    ,   a9A_val]
    
    J=[1/a1A_val,1/a2A_val ,1/a3A_val ,1/a4A_val,1/a5A_val  ,1/a6A_val,  1/a7A_val, 1 /a8A_val, 1/a9A_val , 1]

    row=A+B+C+D+E+F+G+H+I+J
    
    return row

def permutations_for(indices, KI):
    permutations_list = list(permutations(indices))
    perm_index_table = [0] * len(permutations_list)
    perm_index = 0

    if len(indices) == 3:
        tie_counter=0
        ranking= float(1-KI)
        for permutation in permutations_list:
            
          if permutation[0] == permutation[1]:
              if permutation[1] == permutation[2]:
                 perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                 tie_counter=tie_counter+1 
            
              elif permutation[1] > permutation[2]:
                 perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                 tie_counter=tie_counter+1 
              
          elif permutation[0] > permutation[1]:
               if permutation[1] == permutation[2]:
                 perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                 tie_counter=tie_counter+1 
              
               elif permutation[1] > permutation[2]:
                 perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                 tie_counter=tie_counter+1 
                    
                
            

          perm_index = perm_index + 1
        for i in range(len(perm_index_table)):
            if perm_index_table[i] != 0:
                if tie_counter != 0:
                    perm_index_table[i] /= tie_counter   
        return perm_index_table
    
    ###for n=4
    if len(indices) == 4:
        tie_counter=0
        for permutation in permutations_list:
            ranking= float(1-KI)
            if permutation[0] == permutation[1]:
                if permutation[1] == permutation[2]:
                    if permutation[2] == permutation[3]:
                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking

                        tie_counter=tie_counter+1
                        
                    elif permutation[2] > permutation[3]:
                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                        
                        
                        tie_counter=tie_counter+1
                elif permutation[1] > permutation[2]:
                    if permutation[2] == permutation[3]:
                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                        
                        
                        tie_counter=tie_counter+1
                    elif permutation[2] > permutation[3]:
                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                        
                        
                        tie_counter=tie_counter+1
            elif permutation[0] > permutation[1]:
                if permutation[1] == permutation[2]:
                    if permutation[2] == permutation[3]:
                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                        
                        
                        tie_counter=tie_counter+1
                    elif permutation[2] > permutation[3]:
                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                        
                        
                        tie_counter=tie_counter+1
                elif permutation[1] > permutation[2]:
                    if permutation[2] == permutation[3]:
                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                        
                        tie_counter=tie_counter+1
                        
                    elif permutation[2] > permutation[3]:
                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                        
                        
                        tie_counter=tie_counter+1             


            perm_index = perm_index + 1
        
        for i in range(len(perm_index_table)):
            if perm_index_table[i] != 0:
                if tie_counter != 0:
                    perm_index_table[i] /= tie_counter        
        return perm_index_table

    if len(indices) == 5:
        tie_counter=0
        ranking= float(1-KI)
        for permutation in permutations_list:
            
          #tier 1 [0] = [1]
          if permutation[0] == permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                         
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                         
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1                 
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                    
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:                
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 


          #tier 1 [0] > [1]    
          elif permutation[0] > permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1 
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
                         perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                         tie_counter=tie_counter+1                     
                    


          perm_index = perm_index + 1
        for i in range(len(perm_index_table)):
            if perm_index_table[i] != 0:
                if tie_counter != 0:
                    perm_index_table[i] /= tie_counter   
        return perm_index_table
    
    if len(indices) == 6:
        tie_counter=0
        ranking= float(1-KI)
        for permutation in permutations_list:
            
          #tier 1 [0] = [1]
          if permutation[0] == permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
							 
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
                         
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
                         
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	            
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
                    
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:                
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	


          #tier 1 [0] > [1]    
          elif permutation[0] > permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                            tie_counter=tie_counter+1	                
                    


          perm_index = perm_index + 1
        for i in range(len(perm_index_table)):
            if perm_index_table[i] != 0:
                if tie_counter != 0:
                    perm_index_table[i] /= tie_counter   
        return perm_index_table


    if len(indices) == 7:
        tie_counter=0
        ranking= float(1-KI)
        for permutation in permutations_list:
            
          #tier 1 [0] = [1]
          if permutation[0] == permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
							 
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
                         
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
                         
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1	            
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
                    
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:                
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1


          #tier 1 [0] > [1]    
          elif permutation[0] > permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
                                perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                tie_counter=tie_counter+1             
                    


          perm_index = perm_index + 1
        for i in range(len(perm_index_table)):
            if perm_index_table[i] != 0:
                if tie_counter != 0:
                    perm_index_table[i] /= tie_counter   
        return perm_index_table
    

    if len(indices) == 8:
        tie_counter=0
        ranking= float(1-KI)
        for permutation in permutations_list:
            
          #tier 1 [0] = [1]
          if permutation[0] == permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
							 
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
                         
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
                         
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1            
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
                    
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:                
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1


          #tier 1 [0] > [1]    
          elif permutation[0] > permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
                                    perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                    tie_counter=tie_counter+1            
                    

          perm_index = perm_index + 1
        for i in range(len(perm_index_table)):
            if perm_index_table[i] != 0:
                if tie_counter != 0:
                    perm_index_table[i] /= tie_counter   
        return perm_index_table


    if len(indices) == 9:
        tie_counter=0
        ranking= float(1-KI)
        for permutation in permutations_list:
            
          #tier 1 [0] = [1]
          if permutation[0] == permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
							 
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                         
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                         
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1           
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:                
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1


          #tier 1 [0] > [1]    
          elif permutation[0] > permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1         
                    


          perm_index = perm_index + 1
        for i in range(len(perm_index_table)):
            if perm_index_table[i] != 0:
                if tie_counter != 0:
                    perm_index_table[i] /= tie_counter   
        return perm_index_table

    if len(indices) == 9:
        tie_counter=0
        ranking= float(1-KI)
        for permutation in permutations_list:
            
          #tier 1 [0] = [1]
          if permutation[0] == permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
							 
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                         
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                         
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1           
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:                
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1


          #tier 1 [0] > [1]    
          elif permutation[0] > permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                                        perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                        tie_counter=tie_counter+1         
                    


          perm_index = perm_index + 1
        for i in range(len(perm_index_table)):
            if perm_index_table[i] != 0:
                if tie_counter != 0:
                    perm_index_table[i] /= tie_counter   
        return perm_index_table


    if len(indices) == 10:
        tie_counter=0
        ranking= float(1-KI)
        for permutation in permutations_list:
            
          #tier 1 [0] = [1]
          if permutation[0] == permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
							 
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                         
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                         
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1         
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                    
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:                
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1


          #tier 1 [0] > [1]    
          elif permutation[0] > permutation[1]:
             #tier 2 [1] = [2]
             if permutation[1] == permutation[2]:
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
             
             #tier 2 [1] > [2]
             elif permutation[1] > permutation[2]:
             
                #tier3 [2] = [3]
                if permutation[2] == permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                
                #tier3 [2] = [3]
                elif permutation[2] > permutation[3]:
                    #tier4 [3] = [4]
                    if permutation[3] == permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                    
                    #tier4 [3] > [4]
                    elif permutation[3] > permutation[4]:
						#tier5 [4] = [5]
                        if permutation[4] == permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
						#tier5 [4] > [5]
                        elif permutation[4] > permutation[5]:
    						#tier6 [5] = [6]
                            if permutation[5] == permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
    						#tier6 [5] > [6]
                            elif permutation[5] > permutation[6]:
        						#tier7 [6] = [7]
                                if permutation[6] == permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
        						#tier7 [6] > [7]
                                elif permutation[6] > permutation[7]:
            						#tier8 [7] = [8]
                                    if permutation[7] == permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
            						#tier8 [7] > [8]
                                    elif permutation[7] > permutation[8]:
                						#tier9 [8] = [9]
                                        if permutation[8] == permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1
                						#tier9 [8] > [9]
                                        elif permutation[8] > permutation[9]:
                                            perm_index_table[perm_index]= float(perm_index_table[perm_index]) + ranking
                                            tie_counter=tie_counter+1       
                    


          perm_index = perm_index + 1
        for i in range(len(perm_index_table)):
            if perm_index_table[i] != 0:
                if tie_counter != 0:
                    perm_index_table[i] /= tie_counter   
        return perm_index_table

def Koczkodaj_index_list(matrix):

    min_list = []
    size = int(len(matrix) ** 0.5)  
    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                index_ij = i * size + j
                index_ik = i * size + k
                index_kj = k * size + j
                
                min_a = abs(1 - matrix[index_ij] / (matrix[index_ik] * matrix[index_kj]))
                min_b = abs(1 - (matrix[index_ik] * matrix[index_kj]) / matrix[index_ij])
                minimum = min(min_a, min_b)
                min_list.append(minimum)
    return max(min_list)
                    


def priority_vector(matrix):
    # calculate the geometric mean of each row
    row_means = [gmean(row) for row in matrix]
    # calculate the product of the row means
    product = np.prod(row_means)
    # divide each row mean by the product
    priority_vector = [mean / product for mean in row_means]
    # normalize the priority vector so that its sum is 1
    priority_vector /= np.sum(priority_vector)
    return priority_vector


def output_for_n3(filePath=None):
    options = ['A12', 'A13', 'A23']
    indice = []
    values = []
    while options:
        print("Available indices:", options)
        choice = str(input("Choose one value: "))
        if choice in options:
            print("Selected:", choice)
            if choice=='A12':
                choice2=0
            elif choice=='A13':
                choice2=1
            elif choice=='A23':
                choice2=2
            indice.append(choice2)
            value = input("Write one value from the SAATy scale: ")
            fraction = Fraction(value)
            value=float(fraction)
            values.append(value)
            options.remove(choice)
            
            if len(indice) == len(values):
                params = {
                    'a12': None,
                    'a13': None,
                    'a23': None
                }

                for i in range(len(indice)):
                    index = indice[i]
                    value = values[i]

                    if index == 0:
                        params['a12'] = value
                    elif index == 1:
                        params['a13'] = value
                    elif index == 2:
                        params['a23'] = value

                generator_matrices_n3(**params)
            else:
                print("Incorrect matching of list sizes")

    return 0
    

def output_for_n4(filePath=None):
        options = ['A12', 'A13', 'A14', 'A23', 'A24', 'A34']
        indice = []
        values = []
        while options:
            print("Available indices:", options)
            choice = str(input("Choose one value: "))
            if choice in options:
                print("Selected:", choice)
                if choice=='A12':
                    choice2=0
                elif choice=='A13':
                    choice2=1
                elif choice=='A14':
                    choice2=2
                elif choice=='A23':
                    choice2=3
                elif choice=='A24':
                    choice2=4
                elif choice=='A34':
                    choice2=5
                indice.append(choice2)
                value = input("Write one value from the SAATy scale: ")
                fraction = Fraction(value)
                value=float(fraction)
                values.append(value)
                options.remove(choice)
                
                if len(indice) == len(values):
                    params = {
                        'a12': None,
                        'a13': None,
                        'a14': None,
                        'a23': None,
                        'a24': None,
                        'a34': None
                    }

                    for i in range(len(indice)):
                        index = indice[i]
                        value = values[i]

                        if index == 0:
                            params['a12'] = value
                        elif index == 1:
                            params['a13'] = value
                        elif index == 2:
                            params['a14'] = value
                        elif index == 3:
                            params['a23'] = value
                        elif index == 4:
                            params['a24'] = value
                        elif index == 5:
                            params['a34'] = value                            

                    if len(indice)==1:
                        choice = str(input("This may take 40min to calculate, are you sure? (Write YES, if you want to show results: "))
                        if choice in ["YES" , "yes", "y", "Y"]:
                            generator_matrices_n4(**params)
                    if len(indice)==2:
                        choice = str(input("This may take 20min to calculate, are you sure? (Write YES, if you want to show results: "))
                        if choice in ["YES" , "yes", "y", "Y"]:
                            generator_matrices_n4(**params)
                    if len(indice)==3:
                        choice = str(input("This may take 5min to calculate, are you sure? (Write YES, if you want to show results: "))
                        if choice in ["YES" , "yes", "y", "Y"]:
                            generator_matrices_n4(**params)
                    if len(indice)==4:
                        choice = str(input("This may take 2min to calculate, are you sure? (Write YES, if you want to show results: "))
                        if choice in ["YES" , "yes", "y", "Y"]:
                            generator_matrices_n4(**params)   
                    if len(indice)==5:
                        choice = str(input("This may take 1min to calculate, are you sure? (Write YES, if you want to show results: "))
                        if choice in ["YES" , "yes", "y", "Y"]:
                            generator_matrices_n4(**params)   
                    if len(indice)>5:
                        generator_matrices_n4(**params)
                else:
                    print("Incorrect matching of list sizes")       


def output_for_n5(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a23=None,a24=None,a25=None,a34=None,a35=None,a45=None):
    perm_index_table=[0]*120
    counter_for_indices=0
    if filePath is None:
        for i in range(0,loops):
            row=generator_random_matrices_n5()
                
            variables = [None, a12, a13, a14, a15, None, None, a23, a24, a25, None, None, None, a34, a35, None, None, None, None, a45]
    
            found_variables = True
            
            for i, var in enumerate(variables):
                if var is not None and row[i] != var:
                    found_variables = False
                    break
             
            if found_variables:
                #print(row)
                KI=Koczkodaj_index_list(row)

                vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))

                
                perms_calculated_table = permutations_for(vectors,KI)
                perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                
                counter_for_indices=counter_for_indices+1
            
                            
                            
        if counter_for_indices > 0:    
            
            total = sum(perm_index_table)
        
            
            percentages = [(num / total) * 100 for num in perm_index_table]
            
            
            permutations_list = list(permutations(['A','B','C','D','E']))
            
            for percentage, permutation in zip(percentages, permutations_list):
                if percentage>0:
                    print(permutation, f'{percentage:.8f}%')
                    
        else:
            print("No matrices with given indice(s)")    
        
        return 0
    else:
            with open(filePath, newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    row_float = [float(Fraction(data)) for data in row]
                    row=row_float
                    
                    variables = [None, a12, a13, a14, a15, None, None, a23, a24, a25, None, None, None, a34, a35, None, None, None, None, a45]
        
                    found_variables = True
                    
                    for i, var in enumerate(variables):
                        if var is not None and row[i] != var:
                            found_variables = False
                            break
                     
                    if found_variables:
                        #print(row)
                        KI=Koczkodaj_index_list(row)

                        vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))

                        
                        perms_calculated_table = permutations_for(vectors,KI)
                        perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                        
                        counter_for_indices=counter_for_indices+1
          
                                    
                if counter_for_indices > 0:    

                    total = sum(perm_index_table)
                

                    percentages = [(num / total) * 100 for num in perm_index_table]
                    
                    
                    permutations_list = list(permutations(['A','B','C','D','E']))

                    for percentage, permutation in zip(percentages, permutations_list):
                        if percentage>0:
                            print(permutation, f'{percentage:.8f}%')
                            
                else:
                    print("No matrices with given indice(s)")    
                
                return 0


def output_for_n6(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a16=None,a23=None,a24=None,a25=None,a26=None,a34=None,a35=None,a36=None,a45=None,a46=None,a56=None):

    perm_index_table=[0]*720

    counter_for_indices=0
    if filePath is None:
        for i in range(0,loops):
            row=generator_random_matrices_n6()
    
                
            variables = [None, a12, a13, a14, a15, a16, 
                         None, None, a23, a24, a25, a26, 
                         None, None, None, a34, a35, a36,
                         None, None, None, None, a45, a46,
                         None, None, None, None, None, a56]
    
            found_variables = True
            
            for i, var in enumerate(variables):
                if var is not None and row[i] != var:
                    found_variables = False
                    break
             
            if found_variables:
                #print(row)
                KI=Koczkodaj_index_list(row)

                vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))

                
                perms_calculated_table = permutations_for(vectors,KI)
                perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                
                counter_for_indices=counter_for_indices+1

                            
                            
        if counter_for_indices > 0:    

            total = sum(perm_index_table)

            percentages = [(num / total) * 100 for num in perm_index_table]
            
            
            permutations_list = list(permutations(['A','B','C','D','E','F']))

            for percentage, permutation in zip(percentages, permutations_list):
                if percentage>0:
                    print(permutation, f'{percentage:.8f}%')
                    
        else:
            print("No matrices with given indice(s)")    
        return 0
    
    else:
            with open(filePath, newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    row_float = [float(Fraction(data)) for data in row]
                    row=row_float
 
                    variables = [None, a12, a13, a14, a15, a16, 
                                 None, None, a23, a24, a25, a26, 
                                 None, None, None, a34, a35, a36,
                                 None, None, None, None, a45, a46,
                                 None, None, None, None, None, a56]
            
                    found_variables = True
                    
                    for i, var in enumerate(variables):
                        if var is not None and row[i] != var:
                            found_variables = False
                            break
                     
                    if found_variables:
                        #print(row)
                        KI=Koczkodaj_index_list(row)

                        vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))

                        
                        perms_calculated_table = permutations_for(vectors,KI)
                        perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                        
                        counter_for_indices=counter_for_indices+1
                    
                                    
                if counter_for_indices > 0:    

                    total = sum(perm_index_table)
                
                    percentages = [(num / total) * 100 for num in perm_index_table]
                    
                    
                    permutations_list = list(permutations(['A','B','C','D','E','F']))

                    for percentage, permutation in zip(percentages, permutations_list):
                        if percentage>0:
                            print(permutation, f'{percentage:.8f}%')
                            
                else:
                    print("No matrices with given indice(s)")    
                return 0                   


def output_for_n7(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a16=None,a17=None,a23=None,a24=None,a25=None,a26=None,a27=None,a34=None,a35=None,a36=None,a37=None,a45=None,a46=None,a47=None,a56=None,a57=None,a67=None):
    perm_index_table=[0]*5040

    counter_for_indices=0
    if filePath is None:
        for i in range(0,loops):
            row=generator_random_matrices_n7()
                
            variables = [None, a12, a13, a14, a15, a16, a17, 
                         None, None, a23, a24, a25, a26, a27,
                         None, None, None, a34, a35, a36, a37,
                         None, None, None, None, a45, a46, a47,
                         None, None, None, None, None, a56, a57,
                         None, None, None, None, None, None,a67]
    
            found_variables = True
            
            for i, var in enumerate(variables):
                if var is not None and row[i] != var:
                    found_variables = False
                    break
             
            if found_variables:
                #print(row)
                KI=Koczkodaj_index_list(row)

                vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))
                
                perms_calculated_table = permutations_for(vectors,KI)
                perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                
                counter_for_indices=counter_for_indices+1
                                       
                            
        if counter_for_indices > 0:    

            total = sum(perm_index_table)
        
            percentages = [(num / total) * 100 for num in perm_index_table]
            
            
            permutations_list = list(permutations(['A','B','C','D','E','F','G']))

            for percentage, permutation in zip(percentages, permutations_list):
                if percentage>0:
                    print(permutation, f'{percentage:.8f}%')
                    
        else:
            print("No matrices with given indice(s)")    
        return 0
    
    else:
            with open(filePath, newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    row_float = [float(Fraction(data)) for data in row]
                    row=row_float
                    
                    variables = [None, a12, a13, a14, a15, a16, a17, 
                                 None, None, a23, a24, a25, a26, a27,
                                 None, None, None, a34, a35, a36, a37,
                                 None, None, None, None, a45, a46, a47,
                                 None, None, None, None, None, a56, a57,
                                 None, None, None, None, None, None,a67]
            
                    found_variables = True
                    
                    for i, var in enumerate(variables):
                        if var is not None and row[i] != var:
                            found_variables = False
                            break
                     
                    if found_variables:
                        #print(row)
                        KI=Koczkodaj_index_list(row)

                        vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))
                        #print(vectors)
                        
                        perms_calculated_table = permutations_for(vectors,KI)
                        perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                        
                        counter_for_indices=counter_for_indices+1
                                    
                                    
                if counter_for_indices > 0:    
                    total = sum(perm_index_table)
                
                    percentages = [(num / total) * 100 for num in perm_index_table]
                    
                    
                    permutations_list = list(permutations(['A','B','C','D','E','F','G']))
                    for percentage, permutation in zip(percentages, permutations_list):
                        if percentage>0:
                            print(permutation, f'{percentage:.8f}%')
                            
                else:
                    print("No matrices with given indice(s)")    
                return 0
        

def output_for_n8(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a16=None,a17=None,a18=None,a23=None,a24=None,a25=None,a26=None,a27=None,a28=None,a34=None,a35=None,a36=None,a37=None,a38=None,a45=None,a46=None,a47=None,a48=None,a56=None,a57=None,a58=None,a67=None,a68=None,a78=None):
    perm_index_table=[0]*40320
	
    counter_for_indices=0
    if filePath is None:
        for i in range(0,loops):
            row=generator_random_matrices_n8()
                
            variables = [None, a12, a13, a14, a15, a16, a17, a18,
                         None, None, a23, a24, a25, a26, a27, a28,
                         None, None, None, a34, a35, a36, a37, a38,
                         None, None, None, None, a45, a46, a47, a48,
                         None, None, None, None, None, a56, a57, a58,
                         None, None, None, None, None, None,a67, a68,
                         None, None, None, None, None, None,None,a78]
    
            found_variables = True
            
            for i, var in enumerate(variables):
                if var is not None and row[i] != var:
                    found_variables = False
                    break
             
            if found_variables:
                #print(row)
                KI=Koczkodaj_index_list(row)

                vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))

                
                perms_calculated_table = permutations_for(vectors,KI)
                perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                
                counter_for_indices=counter_for_indices+1

                            
                            
        if counter_for_indices > 0:    

            total = sum(perm_index_table)

            percentages = [(num / total) * 100 for num in perm_index_table]
            
            permutations_list = list(permutations(['A','B','C','D','E','F','G','H']))

            for percentage, permutation in zip(percentages, permutations_list):
                if percentage>0:
                    print(permutation, f'{percentage:.8f}%')
                    
        else:
            print("No matrices with given indice(s)")
        
        return 0
    
    else:
            with open(filePath, newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    row_float = [float(Fraction(data)) for data in row]
                    row=row_float
                    
                    variables = [None, a12, a13, a14, a15, a16, a17, a18,
                                 None, None, a23, a24, a25, a26, a27, a28,
                                 None, None, None, a34, a35, a36, a37, a38,
                                 None, None, None, None, a45, a46, a47, a48,
                                 None, None, None, None, None, a56, a57, a58,
                                 None, None, None, None, None, None,a67, a68,
                                 None, None, None, None, None, None,None,a78]
            
                    found_variables = True
                    
                    for i, var in enumerate(variables):
                        if var is not None and row[i] != var:
                            found_variables = False
                            break
                     
                    if found_variables:
                        #print(row)
                        KI=Koczkodaj_index_list(row)

                        vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))

                        
                        perms_calculated_table = permutations_for(vectors,KI)
                        perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                        
                        counter_for_indices=counter_for_indices+1
                    
                                    
                                    
                if counter_for_indices > 0:    
                    total = sum(perm_index_table)
                
                    percentages = [(num / total) * 100 for num in perm_index_table]
                    
                    permutations_list = list(permutations(['A','B','C','D','E','F','G','H']))

                    for percentage, permutation in zip(percentages, permutations_list):
                        if percentage>0:
                            print(permutation, f'{percentage:.8f}%')
                            
                else:
                    print("No matrices with given indice(s)")
                
                return 0


def output_for_n9(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a16=None,a17=None,a18=None,a19=None,a23=None,a24=None,a25=None,a26=None,a27=None,a28=None,a29=None,a34=None,a35=None,a36=None,a37=None,a38=None,a39=None,a45=None,a46=None,a47=None,a48=None,a49=None,a56=None,a57=None,a58=None,a59=None,a67=None,a68=None,a69=None,a78=None,a79=None,a89=None):
    perm_index_table=[0]*362880

    counter_for_indices=0
    if filePath is None:
        for i in range(0,loops):
            row=generator_random_matrices_n9()
    
                
            variables = [None, a12, a13, a14, a15, a16, a17, a18, a19,
                         None, None, a23, a24, a25, a26, a27, a28, a29,
                         None, None, None, a34, a35, a36, a37, a38, a39,
                         None, None, None, None, a45, a46, a47, a48, a49,
                         None, None, None, None, None, a56, a57, a58, a59,
                         None, None, None, None, None, None,a67, a68, a69,
                         None, None, None, None, None, None,None,a78, a79,
                         None, None, None, None, None, None,None,None, a89]
    
            found_variables = True
            
            for i, var in enumerate(variables):
                if var is not None and row[i] != var:
                    found_variables = False
                    break
             
            if found_variables:
                #print(row)
                KI=Koczkodaj_index_list(row)

                vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))
                
                perms_calculated_table = permutations_for(vectors,KI)
                perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                
                counter_for_indices=counter_for_indices+1
                                      
                            
        if counter_for_indices > 0:    
            total = sum(perm_index_table)
        
            percentages = [(num / total) * 100 for num in perm_index_table]
                   
            permutations_list = list(permutations(['A','B','C','D','E','F','G','H','I']))
            for percentage, permutation in zip(percentages, permutations_list):
                if percentage>0:
                    print(permutation, f'{percentage:.8f}%')
                    
        else:
            print("No matrices with given indice(s)") 
            return 0
        
    else:
            with open(filePath, newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    row_float = [float(Fraction(data)) for data in row]
                    row=row_float        
                    variables = [None, a12, a13, a14, a15, a16, a17, a18, a19,
                                 None, None, a23, a24, a25, a26, a27, a28, a29,
                                 None, None, None, a34, a35, a36, a37, a38, a39,
                                 None, None, None, None, a45, a46, a47, a48, a49,
                                 None, None, None, None, None, a56, a57, a58, a59,
                                 None, None, None, None, None, None,a67, a68, a69,
                                 None, None, None, None, None, None,None,a78, a79,
                                 None, None, None, None, None, None,None,None, a89]
            
                    found_variables = True
                    
                    for i, var in enumerate(variables):
                        if var is not None and row[i] != var:
                            found_variables = False
                            break
                     
                    if found_variables:
                        #print(row)
                        KI=Koczkodaj_index_list(row)

                        vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))
                        
                        perms_calculated_table = permutations_for(vectors,KI)
                        perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                        
                        counter_for_indices=counter_for_indices+1
                                                      
                                    
                if counter_for_indices > 0:    
                    total = sum(perm_index_table)
                
                    percentages = [(num / total) * 100 for num in perm_index_table]
                                    
                    permutations_list = list(permutations(['A','B','C','D','E','F','G','H','I']))
                    for percentage, permutation in zip(percentages, permutations_list):
                        if percentage>0:
                            print(permutation, f'{percentage:.8f}%')
                            
                else:
                    print("No matrices with given indice(s)") 
                    return 0      
    
        
def output_for_n10(filePath=None, loops=1000000, a12=None,a13=None,a14=None,a15=None,a16=None,a17=None,a18=None,a19=None,a1A=None,a23=None,a24=None,a25=None,a26=None,a27=None,a28=None,a29=None,a2A=None,a34=None,a35=None,a36=None,a37=None,a38=None,a39=None,a3A=None,a45=None,a46=None,a47=None,a48=None,a49=None,a4A=None,a56=None,a57=None,a58=None,a59=None,a5A=None,a67=None,a68=None,a69=None,a6A=None,a78=None,a79=None,a7A=None,a89=None,a8A=None,a9A=None):

    perm_index_table=[0]*3628800

    counter_for_indices=0
    if filePath is None:    
        for i in range(0,loops):
            row=generator_random_matrices_n10()
    
                
            variables = [None, a12, a13, a14, a15, a16, a17, a18, a19, a1A,
                         None, None, a23, a24, a25, a26, a27, a28, a29, a2A, 
                         None, None, None, a34, a35, a36, a37, a38, a39, a3A, 
                         None, None, None, None, a45, a46, a47, a48, a49, a4A, 
                         None, None, None, None, None, a56, a57, a58, a59, a5A, 
                         None, None, None, None, None, None,a67, a68, a69, a6A,
                         None, None, None, None, None, None,None,a78, a79, a7A, 
                         None, None, None, None, None, None,None,None, a89, a8A,
                         None, None, None, None, None, None,None,None, None, a9A]
    
            found_variables = True
            
            for i, var in enumerate(variables):
                if var is not None and row[i] != var:
                    found_variables = False
                    break
             
            if found_variables:
                #print(row)
                KI=Koczkodaj_index_list(row)

                vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))
                
                perms_calculated_table = permutations_for(vectors,KI)
                perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                
                counter_for_indices=counter_for_indices+1
                 
                            
        if counter_for_indices > 0:    

            total = sum(perm_index_table)
        
            percentages = [(num / total) * 100 for num in perm_index_table]
            
            permutations_list = list(permutations(['A','B','C','D','E','F','G','H','I','J']))

            for percentage, permutation in zip(percentages, permutations_list):
                if percentage>0:
                    print(permutation, f'{percentage:.8f}%')
        else:
            print("No matrices with given indice(s)") 
        return 0
    
    else:
            with open(filePath, newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    row_float = [float(Fraction(data)) for data in row]
                    row=row_float         
                    variables = [None, a12, a13, a14, a15, a16, a17, a18, a19, a1A,
                                 None, None, a23, a24, a25, a26, a27, a28, a29, a2A, 
                                 None, None, None, a34, a35, a36, a37, a38, a39, a3A, 
                                 None, None, None, None, a45, a46, a47, a48, a49, a4A, 
                                 None, None, None, None, None, a56, a57, a58, a59, a5A, 
                                 None, None, None, None, None, None,a67, a68, a69, a6A,
                                 None, None, None, None, None, None,None,a78, a79, a7A, 
                                 None, None, None, None, None, None,None,None, a89, a8A,
                                 None, None, None, None, None, None,None,None, None, a9A]
            
                    found_variables = True
                    
                    for i, var in enumerate(variables):
                        if var is not None and row[i] != var:
                            found_variables = False
                            break
                     
                    if found_variables:
                        #print(row)
                        KI=Koczkodaj_index_list(row)

                        vectors=priority_vector(np.array(row).reshape((int(len(row) ** 0.5)), (int(len(row) ** 0.5))))
                   
                        perms_calculated_table = permutations_for(vectors,KI)
                        perm_index_table = [perm_index_table[i] + perms_calculated_table[i] for i in range(len(perm_index_table))]
                        
                        counter_for_indices=counter_for_indices+1
                              
                                    
                if counter_for_indices > 0:    
                    total = sum(perm_index_table)
                
                    percentages = [(num / total) * 100 for num in perm_index_table]
                                 
                    permutations_list = list(permutations(['A','B','C','D','E','F','G','H','I','J']))
					
                    for percentage, permutation in zip(percentages, permutations_list):
                        if percentage>0:
                            print(permutation, f'{percentage:.8f}%')

                else:
                    print("No matrices with given indice(s)") 
                return 0


