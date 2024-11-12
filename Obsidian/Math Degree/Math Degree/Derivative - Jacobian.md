## Multivariate
In single variable calc, we generally define derivatives on the [[Interior Point|Interior]] of the domain of $f$ (or a subset)

Suppose $\overrightarrow f:U\to \mathbb{R}^m$ where $U\subset \mathbb{R}^n$. We say that $f$ is [[Differentiablility|Differentiable]] at $\overrightarrow x_0\in U$ if there is a $m\times n$ matrix A so that the following limit is 0:
$$\lim_{\overrightarrow x\to\overrightarrow x_0}\frac{||\overrightarrow f(\overrightarrow x) - \overrightarrow f(\overrightarrow x_0) - A(\overrightarrow x - \overrightarrow x_0)||}{||\overrightarrow x-\overrightarrow x_0||}=0$$
When this is true, $A$ must be unique. We call this matrix the derivative of $\overrightarrow f$ at $\overrightarrow x_0$ and we write it as $D\overrightarrow f(\overrightarrow x_0)=A$. 
1. If $\overrightarrow f$ is differentiable at $\overrightarrow x_0$, then all partials for $f=\begin{bmatrix} f_1\ldots f_m \end{bmatrix}$ exist and 
$$D\overrightarrow f(\overrightarrow x_0) = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \ldots & \frac{\partial f_1}{\partial x_n}\\ \vdots & \ddots &\vdots \\ \frac{\partial f_m}{\partial x_1}&\ldots & \frac{\partial f_m}{\partial x_n}\end{bmatrix}$$
2. If $\overrightarrow f$ is diff. at $\overrightarrow x_0$, then all [[Directional Derivative]]s exist, and 
$$D_\overrightarrow v\overrightarrow f(\overrightarrow x_0) =D\overrightarrow f(\overrightarrow x_0)\overrightarrow v $$
The converses of 1, 2 need not hold.
The above matrix is often called the Jacobian matrix
For a scalar function $f$, the vector $Df(\overrightarrow x_0)^T$ is called the gradient of $f$ at $\overrightarrow x_0$, written as $\nabla f(\overrightarrow x_0)$.
If all partials are continuous, then $\overrightarrow f$ is differentiable and therefore 1 and 2 hold in the above theorem.
## Tangent plane
The tangent plane for a point above is given by: 
$$\overrightarrow L(\overrightarrow x)=\overrightarrow f(\overrightarrow x_0)+D\overrightarrow f(\overrightarrow x_0)(\overrightarrow x-\overrightarrow x_0)$$
As well, the [[Normal Vector]] for this plane is given by:
$$\overrightarrow n = \pm\begin{bmatrix} f_x\\ f_y\\ -1 \end{bmatrix}$$