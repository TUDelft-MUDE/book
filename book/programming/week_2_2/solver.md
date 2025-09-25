## Solving systems of equations

In numerical methods, problems are often cast in the form of a linear system of equations

$$
\mathbf{Ku} = \mathbf{f}
$$

Where $\mathbf{K}$ is a matrix, $\mathbf{u}$ is a vector with unknowns and $\mathbf{f}$ is a known right hand side vector. The system of equations then needs to be solved for $\mathbf{u}$. Mathematically, it is clear that the solution can be obtained as:

$$
\mathbf{u} = \mathbf{K}^{-1}\mathbf{f}
$$

However, computing the inverse of a large matrix is an expensive operation. Generally, the number of operations that need to be performed to compute the inverse of an $n\times n$-matrix is of the order $n^3$, which implies that it blows up quickly when the matrix is large. Faster algorithms are available that compute the solution $\mathbf{u}$ to the linear system of equations without computing the inverse of the matrix. Many different algorithms are available that do the job and which is to be preferred depends on the size and structure of the matrix. 

For matrices of medium size, `numpy.linalg.solve` is a better choice than `numpy.linalg.inv`. The algorithms in `numpy.linalg.solve` still scale with the order $n^3$ but they get to a result faster, typically 2-3 times faster. Besides, `inv` followed by matrix-vector multiplication can give rise to larger round-off errors than `solve`, which may be significant depending on the _condition number_ of the matrix.

For sparse matrices, better scaling with the size can be obtained with dedicated algorithms. The function `scipy.sparse.linalg.spsolve` gives much better performance. 

For very large systems, the direct solver of `scipy.sparse.linalg.solve` can be outperformed by iterative solvers that search for the $\mathbf{u}$ that satisfies $\mathbf{Ku}=\mathbf{f}$ iteratively. Examples are the Conjugate Gradient method `scipy.sparse.linalg.cg` for symmetric positive definite matrices and the Generalized Minimal Residual method `scipy.sparse.linalg.gmres` for general non-symmetric matrices. In order to get good performance out of iterative solvers, they need to be combined with a preconditioner, for instance incomplete LU (ILU) decomposition. 



