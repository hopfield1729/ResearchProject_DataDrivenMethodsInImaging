This is the code used in my MA4K9 Research Project. The project 'Data Drivne Methods in Inverse Problems in Imaging' is focused specifically on the ROF model. Given a noisy image $\xi$, one specifies a level of denoising $\lambda > 0$ and then solves the problem

$$\min_u \frac12|u - \xi|_2 + \lambda \text{TV}(u)$$

This clearly requires apriori knowledge of $\lambda$ before we solve. In my research, we focus on methods outlined in [source], developing on a suggested algorithm as well as proposing new ones. 

The first model studied is the static weight - we find the **best** $\lambda >0$ for all images (of the same dimension) and solve a monolevel proxy problem that allows for solving for the best hyperparameter. Below are some results of this model:

Static Weight on MNISt:
![image](https://github.com/user-attachments/assets/426e7a98-671c-4c72-a562-94b8a80ea300)

The next model is the model proposed in the original paper, the quadratic model. This is essentially a higher-dimensional version of the above model where we learna positive semi-definite matrix $A$ and our regularisation strangth for the ith noisy image $\xi_i$ is $\lambda = \xi^* A \xi$

[image]

We then investiage a spatially aware model (SAw). This is a model of the form 
$$\lambda(\xi) = \sum_{i,j = 1}^n \Lambda_{ij}|\nabla \xi (i,j)|_2$$

[image]

Then finally we study using a more advanced model, DSAwPCA/DSAwSPCA. These both compute dimensionality reduction of the training set of images (either via vanilla PCA or Sparse PCA) to get an image of dimension $p^2$, with each entry corresponing to a principal component. Let $L$ be the dimensionality reduction map, with $L^{(i,j)}$ the projection map onto the $i,k$th component. Then our regularisation strength takes the form
$$\lambda = \sum_{i = 1}$$

DSAwPCA on MNIST (test set):
![image](https://github.com/user-attachments/assets/043aba25-6e53-489d-bebf-233d827e48f5)

[**LEFT: True, MIDDLE: Noisy, RIGHT: Denoised via DSAwPCA**]

DSAwSCPA on MNST (test set):
![image](https://github.com/user-attachments/assets/f4244c71-486a-4a4d-b9fb-2cfd0bca06fd)

[**LEFT: True, MIDDLE: Noisy, RIGHT: Denoised via DSAwSPCA**]
