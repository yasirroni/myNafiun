import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np
import copy
def quadratic_to_piecewise(a,a0,a00,xmin,xmax,piece_number=2,steps_ize=0.1,mode_hanging=False,hanging_sigma=0.01,show_result=False):
    '''
    Convert quadratic into piecewise (linear function) of:
        y = m*x_delta + y_ref, where:
            x_delta=x-x_ref
            x_ref,y_ref is point of piecewise
            ...

    ## Example:
    xmin=0
    xmax=100
    a=0.1
    a0=1
    a00=10
    w=quadratic_to_piecewise(a,a0,a00,xmin,xmax)   
    print(w)
    '''

    def func_2piecewise(x, m_0, x_1, y_1, m_1):
        y = np.piecewise(x, [x <= x_1, x > x_1],
                        [lambda x:m_0*(x-x_1) + y_1, lambda x:m_1*(x-x_1) + y_1])
        return y

    def func_3piecewise(x, m_0, x_1, y_1, x_2, y_2, m_2):
        y = np.piecewise(x, [x <= x_1, (x > x_1) & (x <= x_2), x > x_2],
                        [lambda x:m_0*(x-x_1) + y_1, lambda x:y_1+(y_2-y_1)*(x-x_1)/(x_2-x_1), lambda x:m_2*(x-x_2) + y_2])
        return y

    def func_quadratic(x,a,a0,a00):
        y=a*x*x+a0*x+a00
        return y    

    def func_gradients(x_list,y_list):
        if isinstance(x_list, list): 
            m_list=[]
            for idx in range(len(x_list)-1):
                m_list.append((y_list[idx+1]-y_list[idx])/(x_list[idx+1]-x_list[idx]))
            return m_list 
        else:
            m_list=y_list/x_list
            return m_list

    def func_linear(x_delta,y_ref,m):
        y=y_ref+m*x_delta
        return y

    def func_piecewise(x_list,result):
        idx=0
        x_piece=[]
        y_piece=[]
        m_piece=[]
        while idx < piece_number*3:
            x_piece.append(result[idx])
            y_piece.append(result[idx+1])
            m_piece.append(result[idx+2])
            idx=idx+3
        piece=0
        y_list=[]
        for x in x_list:
            for piece in range(piece_number):
                if piece == piece_number-1:
                    y_list.append(func_linear(x-x_piece[piece],y_piece[piece],m_piece[piece]))
                elif x <= x_piece[piece+1]:
                    y_list.append(func_linear(x-x_piece[piece],y_piece[piece],m_piece[piece]))
                    break
        return y_list

    def func_show_result(a,a0,a00,xmin,xmax,w,marker_number=20):
        # Get points
        x_sample_show=np.linspace(xmin,xmax,marker_number)
        y_real_show = func_quadratic (x_sample_show,a,a0,a00)
        y_model_show = func_piecewise (x_sample_show,result)

        # Plot
        plt.plot(x_sample_show,y_real_show,c='#1f77b4',marker='+',label="Data")
        plt.plot(x_sample_show,y_model_show,c='#ff7f0e',marker='*',label="Fit")
        plt.title("Piecewise to Real Comparison")
        plt.legend(loc="upper left")
        plt.show()
        pass

    ## Get sample
    numberOfStep=int(1+(xmax-xmin)/steps_ize)
    x_sample=np.linspace(xmin,xmax,numberOfStep)
    y_sample=[a*x*x+a0*x+a00 for x in x_sample]

    ## Sigma (wighting)
    sigma=np.ones(numberOfStep)
    if mode_hanging==True:
        sigma[[0,-1]]=hanging_sigma

    ## Solve
    if piece_number==2:
        lower_bounds=[-np.inf,xmin,-np.inf,-np.inf]
        upper_bounds=[np.inf,xmax,np.inf,np.inf]

        w, _ = opt.curve_fit(func_2piecewise, x_sample, y_sample,bounds=(lower_bounds,upper_bounds),sigma=sigma)
        x_0=copy.deepcopy(xmin)
        y_0=func_2piecewise(x_0, *w).tolist()
        [m_0, x_1, y_1, m_1]=w
        result=[x_0,y_0,m_0,x_1,y_1,m_1]

    elif piece_number==3:
        lower_bounds=[-np.inf,xmin,-np.inf,xmin,-np.inf,-np.inf]
        upper_bounds=[np.inf,xmax,np.inf,xmax,np.inf,np.inf]
        w, _ = opt.curve_fit(func_3piecewise, x_sample, y_sample,bounds=(lower_bounds,upper_bounds),sigma=sigma)
        x_0=copy.deepcopy(xmin)
        y_0=func_3piecewise(x_0, *w).tolist()
        [m_0, x_1, y_1, x_2, y_2, m_2]=w
        m_1=func_gradients(x_2-x_1,y_2-y_1)
        result=[x_0,y_0,m_0,x_1,y_1,m_1, x_2, y_2, m_2]
    else:
        print('Number of piece is unsupported')
        return []
    
    ## Show result
    if show_result==True:
        func_show_result(a,a0,a00,xmin,xmax,w)
    
    return result

## Uncomment for example
xmin=0
xmax=100
a=0.1
a0=1
a00=10
result=quadratic_to_piecewise(a,a0,a00,xmin,xmax,piece_number=3,steps_ize=0.01,mode_hanging=True,show_result=True)
# result=quadratic_to_piecewise(a,a0,a00,xmin,xmax,piece_number=2,steps_ize=0.01,mode_hanging=True,show_result=True)
# result=quadratic_to_piecewise(a,a0,a00,xmin,xmax,piece_number=2,steps_ize=0.01,show_result=True)   
# print(result)