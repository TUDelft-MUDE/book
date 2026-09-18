# Vector spaces

## Vector space and subspace 
A set $ \mathcal{W} $  is called a vector space if its elements are vectors and the sum of two elements of $ \mathcal{W} $ is again an element of $ \mathcal{W} $, and the product of an element of $ \mathcal{W} $ with a scalar is an element of $ \mathcal{W} $.  
A subset of a vector space which itself is a vector space is called a subspace. 

## Span 
Let $ a_{i} \in \mathcal{W} $,  $ i=1, \ldots, n $, where $ \mathcal{W}$ is a vector space. The set of all linear combinations of $ a_{1}, \ldots, a_{n} $, denoted as $ \{ a_{1}, \ldots, a_{n} \} $, is a subspace of $ \mathcal{W}$: $ \{ a_{1}, \ldots, a_{n} \} \subset \mathcal{W} $. 

If every vector of a vector space $ \mathcal{V} $ can be written as a linear combination of $ a_{1}, \ldots, a_{n} $, then $ a_{1}, \ldots, a_{n} $ is said to span $ \mathcal{V}$: $\mathcal{V} = \{ a_{1}, \ldots, a_{n} \} $.

## Basis and dimension of a vector space
A basis of a vector space $ \mathcal{W} $ is a set of linear independent vectors which span $ \mathcal{W} $.

Every vector space contains a basis and every vector can be written as a unique linear combination of the vectors of a basis.

The dimension of a vector space $ \mathcal{W} $, denoted as $ \dim \mathcal{W} $, is the number of vectors of a basis of $ \mathcal{W} $. In an $ n $-dimensional vector space $ \mathcal{W} $, every linear independent set of $n$ vectors is a basis of $ \mathcal{W} $. 

As an example, the three-dimensional space $\mathbb{R}^3$ is a vector space, and one possible basis for $\mathbb{R}^3$  is a set of the following unit vectors:

$$ 
\begin{bmatrix}1\\0\\0 \end{bmatrix}, ~~~ \begin{bmatrix}0\\1\\0 \end{bmatrix}, ~~~ \begin{bmatrix}0\\0\\1 \end{bmatrix}. 
$$

That is all the vectors in  $\mathbb{R}^3$ can be written as linear combination of these three unit vectors. For example, the arbitrary three dimentional  vector $ \begin{bmatrix} 4\\3\\5 \end{bmatrix} $ can be written as the linear combination:

$$
\begin{bmatrix} 4\\3\\5 \end{bmatrix}=4\begin{bmatrix}1\\0\\0 \end{bmatrix}+3\begin{bmatrix}0\\1\\0 \end{bmatrix}+5\begin{bmatrix}0\\0\\1 \end{bmatrix}. 
$$ 

We can say the three vectors  $ \begin{bmatrix}1\\0\\0 \end{bmatrix}, \begin{bmatrix}0\\1\\0 \end{bmatrix}$, and $\begin{bmatrix}0\\0\\1 \end{bmatrix} $span the vector space $\mathbb{R}^3$ . 

## Column Space (or Range Space) of a Matrix
The column space (or range space) of a matrix $A$ of size  $m\times n$, is the subspace of $\mathbb{R}^{m}$ which is spanned by the column vectors of $A$. The range space of $A$ is denoted as $\mathcal{R}(A)$.  The dimension of $\mathcal{R}(A)$, equals the maximum number of linear independent column vectors of $A$.

For example, let $A=\begin{bmatrix} 1&1\\1&2\\1&3 \end{bmatrix}$. Then the $\mathcal{R}(A)$ is a subspace in $\mathbb{R}^{3}$, and its elements can be written as linear combination of the two column vectors of $A$:

$$
\begin{bmatrix} 1\\1\\1 \end{bmatrix}, ~ \text{and} ~ \begin{bmatrix} 1\\2\\3 \end{bmatrix}. 
$$ 

In this example, the dimension of $\mathcal{R}(A)$ is 2 becouse $A$ has two independent columns. 

## Inner product of two vectors 
Inner product of two vectors $x$ and $ y$ denoted by $(x,y)$, is defined as: 

$$ 
(x,y)=x^Ty. 
$$ 

For example the inner product of the two vectors $ x= \begin{bmatrix} 3 \\ 2 \\ 1 \\ 1 \end{bmatrix} $ and $ y= \begin{bmatrix} 1 \\ 2 \\ 3 \\ 4 \end{bmatrix} $ is calculated as: 

$$   
(x,y)=x^Ty= \left[ \begin{array}{cccc} 3&2&1&1\\ \end{array} \right] \left[ \begin{array}{c} 1 \\ 2 \\ 3 \\ 4 \end{array} \right] =(3\times 1)+(2\times 2)+(1\times 3) +(1\times 4)=14.  
$$

## Norm or length of a vector
The length or norm of a vector $x$, denoted as $\|x\|$, is defined as:

$$ 
\| x \| = \sqrt{(x, x)}= \sqrt{x^Tx}. 
$$ 

For example, the length of the vector $ x= \begin{bmatrix} 3 \\ 2 \\ 1 \\ 1 \end{bmatrix} $ is computed as: 

$$ 
\| x \|=\sqrt{ (3\times 3)+ (2\times 2)+ (1\times 1)+(1\times 1)}=\sqrt{15} 
$$ 

## Distance between two vectors
The distance between two vectors $x$ and $y$ is defined as the norm of $u-v$, and is given as $ \|u-v\|$.

## Angle between two vectors and orthogonality
The angle between two vectors $x$ and $y$

is defined to be the number $\theta \in [0, \pi] $  such that:

$$
\cos (\theta) = \frac{ (x,y)}{ \|x\| \|y\|}.
$$ 

Two vectors are said to be orthogonal (or normal to each other) if the angle between them is $\pi/2$, or in other words when their inner product equals zero: $ (x,y)=x^Ty=0 $ .

