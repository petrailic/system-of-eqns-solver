# System of Equations Solver
This project implements linear algebra principles along with a parser to solve systems of equations provided in string form.

### Example Performed on a 5 x 5 System

Input:
```
'''2*v + w + x + y + z =4
    v + w + y + 2x + z = 6
    v + 2w + 1x + y +z = 5
    v + w + x + 2y + z = 7
    v + 2z + x + y + w = 8'''
```

The input string is parsed and converted into an augmented matrix representing the system. The row_reduce function uses Gaussian elimination to get the matrix into Reduced Row-Echelon Form (RREF). Below are the steps of this matrix's reduction:

Step 1 - First pivotal 1:
<p align="center">
  
<img width="468" alt="rr1" src="https://github.com/user-attachments/assets/443bcdf5-4d5f-4c2b-be93-45ccdf007c5f">

</p>
Step 2 - Second pivotal 1:
<p align="center">

<img width="474" alt="rr2" src="https://github.com/user-attachments/assets/3e6a6aee-43d7-4ce0-bc07-0f02d60a7208">

</p>
Step 3 - Third pivotal 1:
<p align="center">
  
<img width="466" alt="rr3" src="https://github.com/user-attachments/assets/aa94c3fa-1f44-43a4-adce-3d2d799505b3">

</p>
Step 4 - Fourth pivotal 1:
<p align="center">
  
<img width="471" alt="rr4" src="https://github.com/user-attachments/assets/118eb640-6d44-4bf8-b942-f248ab905cbf">

</p>
Step 5 - Final pivotal 1:
<p align="center">
  
<img width="474" alt="rr5" src="https://github.com/user-attachments/assets/d6e9b198-46dc-4231-9dfd-a5ada80e6325">

</p>

Finally, a solution is extracted from the RREF matrix and returned as a dictionary of the variables and their corresponding values:

```{'v': -1.0, 'w': -0.0, 'x': 1.0, 'y': 2.0, 'z': 3.0}```



