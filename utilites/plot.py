import matplotlib.pyplot as plt

def show_segment(coords):
    max_y = max(coords[:,0,0])
    max_x = max(coords[:,1,1])
    img = np.zeros([max_y+1, max_x+1])
    for border_index in range(coords.shape[0]):
        row = coords[border_index][0][0]
        cols = coords[border_index][:,1]
        cols = cols if cols[1]-cols[0] < 2 else list(range(cols[0], cols[1]+1, 1))
        for col in cols:
            img[row][col] = 1
    plt.imshow(img)
    plt.axis("off")
    plt.show()
    return img

def show_pic(pic, size=15):
    ax = plt.figure(figsize = (size,size))
    plt.imshow(pic[::-1])
    ax = plt.gca()
    ax.invert_yaxis()
    
def crop_image(image, x=None, y=None, w=None, h=None):
    x = 0 if x == None else x
    y = 0 if y == None else y
    h = image.shape[0] if h == None else h
    w = image.shape[1] if w == None else w
    return image[y:y+h, x:x+w]