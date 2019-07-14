    import numpy as np
    from matplotlib import pyplot as plt

    data = np.load('sdss_galaxy_colors.npy')
    # Get a colour map
    cmap = plt.get_cmap('YlOrRd')

    # Define our colour indexes u-g and r-i
    u_g = data['u']-data['g']
    r_i= data['r']-data['i']
    
    # Make a redshift array
    redshift = data['redshift']
    
    # Create the plot with plt.scatter and plt.colorbar    
    plt.scatter(u_g, r_i, lw=0, s=2, c=redshift, cmap=cmap)
    cbr = plt.colorbar()
    cbr.set_label('Redshift')
    # Define your axis labels and plot title
    plt.xlabel('Colour index u-g')
    plt.ylabel('Colour index r-i')
    # Set any axis limits
    plt.axis([-0.5,2.5,-0.5,1])
    plt.show()
