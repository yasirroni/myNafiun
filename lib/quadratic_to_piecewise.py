import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np
def quadratic_to_piecewise(a,a0,a00,xmin,xmax,piece_number=2,steps_ize=0.1,show_result=False):
    '''
    Convert quadratic into piecewise (linear function) of:
    
    y = m*x + c, where:
        c1=y0-m1*x0
        c2=y0-m2*x0
        ...

    Example:
    xmin=0
    xmax=100
    a=0.1
    a0=1
    a00=10
    w=quadratic_to_piecewise(a,a0,a00,xmin,xmax,piece_number=2,steps_ize=0.01,show_result=True)   
    print(w)
    '''

    def func_2piecewise(x, x0, y0, m1, m2):
        y = np.piecewise(x, [x < x0, x >= x0],
                        [lambda x:m1*(x-x0) + y0, lambda x:m2*(x-x0) + y0])
        return y

    # def func_3piecewise(x, x0, y0, m1, m2):
    #     y = np.piecewise(x, [x < x0, x >= x0],
    #                     [lambda x:m1*(x-x0) + y0, lambda x:m2*(x-x0) + y0])
    #     return y

    def func_quadratic(x,a,a0,a00):
        y=a*x*x+a0*x+a00
        return y    

    def func_show_result(a,a0,a00,xmin,xmax,w,marker_number=20):
        # Get points
        x_sample_show=np.linspace(xmin,xmax,marker_number)
        y_real_show = func_quadratic (x_sample_show,a,a0,a00)
        y_model_show = func_2piecewise(x_sample_show,*w)

        # Plot
        plt.plot(x_sample_show,y_real_show,c='#1f77b4',marker='+',label="Data")
        plt.plot(x_sample_show,y_model_show,c='#ff7f0e',marker='*',label="Fit")
        plt.title("Piecewise to Real Comparison")
        plt.legend(loc="upper left")
        plt.show()
        pass

    ## main()
    numberOfStep=1+(xmax-xmin)/steps_ize

    x_sample=np.linspace(xmin,xmax,numberOfStep)
    y_sample=[a*x*x+a0*x+a00 for x in x_sample]

    if piece_number==2:
        w, _ = opt.curve_fit(func_2piecewise, x_sample, y_sample,bounds=([xmin,-np.inf,-np.inf,-np.inf],[xmax,np.inf,np.inf,np.inf]))
    elif piece_number==3:
        # w, _ = opt.curve_fit(func_3piecewise, x_sample, y_sample,bounds=([xmin,-np.inf,-np.inf,-np.inf],[xmax,np.inf,np.inf,np.inf]))
        print('Number of piece is unsupported')
    else:
        print('Number of piece is unsupported')

    if show_result==True:
        func_show_result(a,a0,a00,xmin,xmax,w)
    
    return w

xmin=0
xmax=100
a=0.1
a0=1
a00=10
w=quadratic_to_piecewise(a,a0,a00,xmin,xmax,piece_number=2,steps_ize=0.01,show_result=True)   
print(w)