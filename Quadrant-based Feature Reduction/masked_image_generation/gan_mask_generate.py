import numpy as np

def mask_generate(k,grey_area, size):
    """
    assign quadents of the image to black (masking certain region of the image to black) for masks for gan
    input:
      I: image
      k: quadents index
      grey area: quadents indexs that to be black out
    output:
      I_copy: is the blacked out masked image
    """
    I = np.zeros(size,dtype=np.uint8)
    shape1=I.shape[0]//(2**k)
    shape2=I.shape[1]//(2**k)
    for i in range(len(grey_area)):
        row=grey_area[i]//(2**k)
        col=grey_area[i]-row*(2**k)
        if col==0:
            col=2**k
        col-=1
        startr=row*shape1;endr=(row+1)*shape1
        startc=col*shape2;endc=(col+1)*shape2
        I[startr:endr,startc:endc,:]=255
    return I