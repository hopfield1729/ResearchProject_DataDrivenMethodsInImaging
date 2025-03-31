import numpy as np 

def add_noise(img, noise_level, type):
    '''
    Inputs: Single-channel image, desired noise level, type ('Gaussin' or 'Uniform')
    '''
    shape = img.shape
    if type == 'Gaussian':
        noise = np.random.normal(loc = 0, scale = noise_level, size = shape)
    elif type == 'Uniform':
        noise = np.random.random(size = shape)
    return img + noise

def add_noise_multichannel(image, sd):
    '''
    Inputs: Coloured image, desired noise level
    Returns: b, g, r layers with Gaussian noise
    '''
    b = cv2.split(img)[2]
    g = cv2.split(img)[1]
    r = cv2.split(img)[0]
    
    r = r + np.random.normal(loc = 0, scale = sd, size = r.shape) #np.random.normal(loc = 0, scale = sd, size = r.shape)
    g = g + np.random.normal(loc = 0, scale = sd, size = r.shape) #np.random.normal(loc = 0, scale = sd, size = r.shape)
    b = b + np.random.normal(loc = 0, scale = sd, size = r.shape) #np.random.normal(loc = 0, scale = sd, size = r.shape)
    
    r = 255 * (r - np.min(r))/(np.max(r) - np.min(r))
    g = 255 * (g - np.min(g))/(np.max(g) - np.min(g))
    b = 255 * (b - np.min(b))/(np.max(b) - np.min(b))
    
    return b, g, r

def add_spnoise(image, sd, prob):
    '''
    Inputs: Single-channel image, desired noise level, probabilty of noise
    Returns: b, g, r layers with salt and pepper noise
    '''
    Nx = image.shape[1]
    Ny = image.shape[0]

    new_img = image

    for i in range(Ny):
        for j in range(Nx):
            if np.random.random() <= prob:
                new_img[i][j] += np.random.normal(loc = 0, scale = sd)
                    
    return new_img

def add_spnoise_multichannel(image, sd, prob):
    '''
    Inputs: Coloured image, desired noise level, probabilty of noise
    Returns: b, g, r layers with salt and pepper noise
    '''
    b = add_spnoise(cv2.split(image)[2], sd, prob)
    g = add_spnoise(cv2.split(image)[1], sd, prob)
    r = add_spnoise(cv2.split(image)[0], sd, prob)
    
    r = 255 * (r - np.min(r))/(np.max(r) - np.min(r))
    g = 255 * (g - np.min(g))/(np.max(g) - np.min(g))
    b = 255 * (b - np.min(b))/(np.max(b) - np.min(b))
    
    return b, g, r

def merger(x,y,z):
    '''
    Inputs: 3 channels (r, g, b)
    Returns: Coloured image from channels
    '''
    R = np.dstack((x, y, z)).astype(np.uint8)
    return R