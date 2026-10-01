# Vectors and matrices

## Matrix
A matrix is a rectangular array of different numbers.  If $A$ is a matrix, it can be written, in a generic form as: 

$$ 
A= \left[ \begin{array}{cccc} a_{11} & a_{12} & \ldots & a_{1n} \\ a_{21} & a_{22} & \ldots & a_{2n} \\ \vdots & \vdots &        & \vdots \\ a_{m1} & a_{m2} & \ldots & a_{mn} \\ \end{array} \right], 
$$ 

where $a_{ij}=(A)_{ij}$ denotes the $ (i,j) $th element of $A$.  The size of a matrix is defined as its number of rows times the number of columns. In the above example,  the size of the matrix  $A$ is $ m \times n $.   

## Vector
An $m \times 1$ matrix 

$$ 
x = \left[ \begin{array}{c} x_{1} \\ x_{2} \\ \vdots \\ x_{m} \\ \end{array} \right] $$ 

is called an $m$-dimensional column vector. A $ 1 \times n $ matrix is called an $ n$-dimensional row vector. When we speak of vectors, we usually refer to column vectors, unless otherwise stated.

(pm_matrix)=
## Matrix operations 
*Summation*: The sum of two matrices $A$ and $B$ is defined if they have the same size. Then $A+B=(a_{ij}+b_{ij})$. The product of a scalar $\alpha$ and a matrix $A$ is $ \alpha A = A \alpha = (\alpha a_{ij}) $.

*Multiplication*: The product $AB$ of two matrices $A$ and $B$ is defined only if the number of columns of matrix $A$ equals the number of rows of matrix $B$. Thus if $A$ is of size $m \times n$ and $B$ is of size $n \times o$, then $C=AB$ is of size $m \times o$, which has its $(ij)$th entry $c_{ij}$ given by $ c_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj} $. Note that in general $AB \neq BA$.

## Special matrices
*Square matrices*: Matrices with the same number of columns and rows are called square matrices. Let $A$ be an $m \times n$ matrix. If $m=n$, then $A$ is a square matrix.  

*Symmetric matrices*: A square matrix $A$ is called symmetric when $A^{T}=A$. For example, the following matrix is a symmetric matrix: 

$$ 
A= \left[ \begin{array}{cccc} 4 & 3& 2& 1 \\ 3 & 4& 3& 2 \\ 2 & 3& 4& 3 \\ 1 & 2& 3& 4 \\ \end{array} \right].  
$$ 

In other words, in symmetric matrices,  $a_{ij}=a_{ji}$.

*Diagonal matrices*: The diagonal entries of an $m \times m$ matrix $A$, with entries $(A)_{ij}=a_{ij}$, are $a_{11}, a_{22}, \ldots, a_{mm}$. Matrix $A$ is called a diagonal matrix if all other entries are equal to zero. Such a matrix will be denoted as $A= \text{diag}(a_{11}, a_{22}, \ldots, a_{mm})$. For example, the following matrix is a diagonal matrix: 

$$ 
A= \left[ \begin{array}{cccc} 1 & 0& 0& 0 \\ 0 & 2& 0& 0 \\ 0 & 0& 5& 0 \\ 0 & 0& 0& 3 \\ \end{array} \right].  
$$

*Identity matrices*: A diagonal matrix is called an  identity matrix if all of its diagonal entries equal $1$. An identity matrix of size $m \times m$ will be written as $A=I_{m}$ or sometimes simply as $A=I$. Examples of identity metrices are: 

$$
I_{1}=1, ~ ~ ~ ~ I_{2}= \left[ \begin{array}{cc}  1&0\\0&1 \end{array} \right], ~ ~ ~ ~ I_{3}=\left[ \begin{array}{ccc}  1&0&0\\0&1&0\\0&0&1 \end{array} \right], ~ ~ ~ ~   I_{4}=\left[ \begin{array}{cccc}  1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1 \end{array} \right].  
$$

*Zero matrix*: A matrix of which all its entries equal zero is called the zero-matrix and is written as $A=0$. 

## Matrix Transpose 
The transpose of a matrix $A$ is the matrix $A^{T}$ obtained by interchanging the rows and columns of $A$. Therefore,  the $(i,j)$th entry of $A^{T}$ is $a_{ji}$. If the size of $A$ is  $ m{\times}n$, then its transpose  $A^{T}$ is a matrix of size  $ n{\times}m$.  Let $\alpha$ and $\beta$ be scalars and $A$ and $B$ be matrices of appropriate size. Then the following properties are hold:

$$ 
\begin{array}{llll} (a) & (\alpha A)^{T}=\alpha A^{T} & (c) & (\alpha A+\beta B)^{T}= \alpha A^{T} + \beta B^{T}\\ (b) & (A^{T})^{T}=A & (d) & (AB)^{T}=B^{T}A^{T} \\ \end{array}. 
$$

Check yourself that for a symmetric matrix $W$ we have $W=W^T$.
Consequently, also $\left(\mathrm{A}^T W\mathrm{A} \right) $ and $\left(\mathrm{A}^T W\mathrm{A} \right)^{-1} $ are symmetric.

## Trace of a matrix
The trace is a function that is only defined on square matrices. The  trace of an square matrix $A$ of size $m \times m$ , denoted as ${\rm trace}(A)$, is defined to be the sum of all its diagonal entries, ${\rm trace}(A)= \sum_{i=1}^{m} a_{ii}.$   For example: 

$$ 
\text{trace}\Big( \left[ \begin{array}{ccc} 4 & 2 & 1 \\ 2 & 3 & 1 \\ 1 & 1 & 2 \\ \end{array} \right] \Big)= 4+3+2=9. 
$$ 

## Linear Combination
Assume $x_{1}, ~ x_{2}, \dots, x_{n}$ are $n$ vectors with the size of $m \times 1$ each, and $\alpha_{1}, ~ \alpha_{2}, \dots \alpha_{n}$, are $n$ scalars, then $ \sum_{i=1}^{n} \alpha_{i} x_{i} $ is called a linear combination of $ x_{1}, \ldots, x_{n} $.  In other words, if we multiply vectors by scalars, and add or subtract them from each other, the result is called the linear combination of the vectors. 

## Linear Dependency
Vectors $ x_{i} $, $ i=1, \ldots, n $, are said to be linear dependent if there exist scalars $ \alpha_{i} $, not all equal to zero, such that $ \alpha_{1}x_{1}+\alpha_{2}x_{2}+\ldots + \alpha_{n}x_{n} = 0 $. An alternative but equivalent definition is:  a set of vectors are linear dependent if at least one of the vectors can be written as linear combination of the others. If not, we say that the vectors $ x_{i} $ are linear independent.  The vectors $ x_{1}, \ldots, x_{n} $ are linear independent if and only if: 

$$ 
\alpha_{1}x_{1}+\alpha_{2}x_{2}+\ldots + \alpha_{n}x_{n} = 0 \Rightarrow \alpha_{1}= \ldots = \alpha_{n}=0 
$$

## Rank of a matrix
The maximum number of linearly independent column vectors of a matrix $A$ is called the rank of $A$, and it is denoted as $\text{rank}(A)$.  The maximum number of linearly independent column vectors of a matrix always equals its maximum number of linearly independent row vectors. A matrix $A$ of size $m \times n$ is said to have full row rank if $\text{rank}(A)=m$ and full column rank if $\text{rank}(A)=n$ . The matrix is said to have a rank deficiency if $ \text{rank}(A) < \text{min}(m,n) $.  

## Singular matrices 
Square matrices with a rank deficiency are called singular. Alternatively, if a square matrix of size $m \times m$ has a rank equal to $m$, the matrix is called nonsingular. 

## Inverse of a matrix
Let $A$ be a square $m \times m$ and nonsingular matrix. Then there exists a unique matrix $A^{-1}$, called the inverse of $A$, such that 

$$
AA^{-1}=A^{-1}A=I_{m}.
$$ 

It can be shown that $ (A^{-1})^{-1}=A$. If $\alpha$ is a nonzero scalar, then $ (\alpha A)^{-1}=\frac{1}{\alpha}A^{-1} $. Note that, singular matrices (or matrices with rank deficiency) are not invertible. 


