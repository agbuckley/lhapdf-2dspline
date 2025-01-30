import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from scipy.stats.mstats import mquantiles

plt.rcParams["text.usetex"] = True

# NEED TO WRITE THIS
if __name__ == '__main__':
    # Plot params
    title_size = 14
    cbar_size = 14
    axes_size = 14
    
    sizex = 51
    sizey = 51
    
    an_d1x,an_d1y,an_d2x, an_d2y = np.loadtxt("/mnt/c/Users/dillo/Desktop/work/Uni/Year_5/Project/Code/MSci_Project/C++/outputs/an_boundary_derivs.csv", dtype='float', delimiter=',', unpack=True, skiprows=1, usecols=[2,3,4,5])
    y,d2x_left, d2x_right = np.loadtxt("/mnt/c/Users/dillo/Desktop/work/Uni/Year_5/Project/Code/MSci_Project/C++/outputs/x_boundary_derivs.csv", dtype='float', delimiter=',', unpack=True, skiprows=1)
    x,d2y_top, d2y_bottom = np.loadtxt("/mnt/c/Users/dillo/Desktop/work/Uni/Year_5/Project/Code/MSci_Project/C++/outputs/y_boundary_derivs.csv", dtype='float', delimiter=',', unpack=True, skiprows=1)
    d4d2xd2y = np.loadtxt("/mnt/c/Users/dillo/Desktop/work/Uni/Year_5/Project/Code/MSci_Project/C++/outputs/corner_boundary_derivs.csv", dtype='float', delimiter=',', unpack=True, skiprows=1, usecols=[2])
    num_d1x, num_d1y, num_d2x, num_d2y = np.loadtxt("/mnt/c/Users/dillo/Desktop/work/Uni/Year_5/Project/Code/MSci_Project/C++/outputs/num_ds_pdf.csv", dtype='float', delimiter=',', unpack=True, skiprows=1, usecols=[2,3,4,5])
    
    an_d1x = an_d1x.reshape((sizey,sizex))
    an_d1y = an_d1y.reshape((sizey,sizex))
    num_d1x = num_d1x.reshape((sizey,sizex))
    num_d1y = num_d1y.reshape((sizey,sizex))
    
    an_d2x = an_d2x.reshape((sizey,sizex))
    an_d2y = an_d2y.reshape((sizey,sizex))
    num_d2x = num_d2x.reshape((sizey,sizex))
    num_d2y = num_d2y.reshape((sizey,sizex))
    
    # Boundaries
    fig = plt.figure(figsize=(10,10))
    axs = fig.subplots(2,2).flatten()

    plot = axs[0].plot(x, an_d2y[-1][:], marker="x", linestyle='None', label=r"analytic")
    axs[0].plot(x, d2y_top,  marker='.', linestyle='None', label=r"numerical extrapolation")
    axs[0].set_title(r"Top boundary",fontsize=title_size)
    axs[0].set_ylabel(r"$\partial^2_y z(x,y)$",fontsize=axes_size)
    axs[0].label_outer()
    
    plot = axs[2].plot(x, an_d2y[0][:], marker="x", linestyle='None', label=r"analytic")
    axs[2].plot(x, d2y_bottom,  marker='.', linestyle='None', label=r"numerical extrapolation")
    axs[2].set_title(r"Bottom boundary",fontsize=title_size)
    axs[2].set_ylabel(r"$\partial^2_y z(x,y)$",fontsize=axes_size)
    axs[2].set_xlabel(r"$\log_{10}x$",fontsize=axes_size)
    
    plot = axs[1].plot(y, an_d2x.T[-1][:], marker="x", linestyle='None', label=r"analytic")
    axs[1].plot(y, d2x_right,  marker='.', linestyle='None', label=r"numerical extrapolation")
    axs[1].set_title(r"Right boundary",fontsize=title_size)
    axs[1].set_ylabel(r"$\partial^2_x z(x,y)$",fontsize=axes_size)
    axs[1].tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=False)
    axs[1].legend()
    
    
    plot = axs[3].plot(y, an_d2x.T[0][:], marker="x", linestyle='None', label=r"analytic")
    axs[3].plot(y, d2x_left,  marker='.', linestyle='None', label=r"numerical extrapolation")
    axs[3].set_title(r"Left boundary",fontsize=title_size)
    axs[3].set_ylabel(r"$\partial^2_x z(x,y)$",fontsize=axes_size)
    axs[3].set_xlabel(r"$\log_{10}Q$",fontsize=axes_size)
    
    fig.savefig("../outputs/pdflike/boundary_extrapolation.pdf", format="pdf")
    