This is the code used in my MA4K9 Research Project. The project 'Data Drivne Methods in Inverse Problems in Imaging' is focused specifically on the ROF model. Given a noisy image $\xi$, one specifies a level of denoising $\lambda > 0$ and then solves the problem

$$\min_u \frac12||u - \xi||_2 + \lambda \text{TV}(u)$$

![image](https://github.com/user-attachments/assets/426e7a98-671c-4c72-a562-94b8a80ea300)
