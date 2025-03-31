import numpy as np
from scipy.linalg import svdvals, svd
import scipy

def im_dual(x):
    Nx = x.shape[0]
    Ny = x.shape[1]

    tv = [0 * x, 0 * x]
    for i in range(Nx):
        for j in range(Ny):
            if i < Nx - 1:
                tv[1][i][j] = x[i + 1][j] - x[i][j]
            elif i == Nx - 1:
                tv[1][i][j] = 0
            if j < Ny - 1:
                tv[0][i][j] = x[i][j + 1] - x[i][j]
            elif j == Ny - 1:
                tv[0][i][j] = 0    
    return np.array(tv)

def TV(x):
    tv = im_dual(x)
    Nx = x.shape[0]
    Ny = x.shape[1]
    total = 0
    for i in range(Nx):
        for j in range(Ny):
            vec = np.array([tv[0][i][j], tv[1][i][j]])
            total += np.linalg.norm(vec)
    return total

def div(d):
    shadow_img = d[0]
    empty_img = 0 * shadow_img
    for i in range(shadow_img.shape[0]):
        for j in range(shadow_img.shape[1]):
            if i== 0:
                vi = d[1][i, j]
            elif i == shadow_img.shape[0] - 1:
                vi = -d[1][i - 1, j]
            else:
                vi = d[1][i,j] - d[1][i-1,j]
            
            if j == 0:
                vj = d[0][i, j]
            elif j == shadow_img.shape[1] -1:
                vj = -d[0][i, j-1]
            else:
                vj = d[0][i,j] - d[0][i,j-1]
                
            empty_img[i,j] = vi + vj
    return empty_img 


#def proj_plus(matrix):
#    sing_vd = scipy.linalg.svd(matrix)
#    U = sing_vd[0]
#    V = sing_vd[2]
#    sigmas = sing_vd[1]
#    for j, sigma in enumerate(sigmas):
#    pos_sigmas = 0 * sigmas
#        pos_sigmas[j] = max(0, sigma)
#    pos_sigmas = np.diag(pos_sigmas) 
#    return U @ pos_sigmas@ V


def proj_pos(A):

    d, O = np.linalg.eigh(A)

    return O@np.diag(np.maximum(d, 0))@O.T