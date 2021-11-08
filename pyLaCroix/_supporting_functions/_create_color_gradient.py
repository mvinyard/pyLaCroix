# _create_color_gradient.py

__module_name__ = "_create_color_gradient.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# package imports #
# --------------- #
from colour import Color

def _create_color_gradient(n_points, color_theme, color_theme_name):
    
    """
    Create a color gradient between a given list of anchor colors. 
    
    color_theme
        list of colors to provide anchors between the gradient points. 
        type: list(str)
    
    n_points
        number of points between each `color_theme` anchor.
        
    Returns:
    --------
    
    Parameters:
    -----------
    
    Notes:
    ------
    
    """
    
    
    
    if n_points == 1:
        colormap = color_theme
        
    else:
        colormap=[]
        for i in range(0, len(color_theme)-1):
            colors_mapped = list(Color(color_theme[i]).range_to(Color(color_theme[i+1]),n_points))
            for color_i in colors_mapped:
                colormap.append(color_i.get_hex())    
    return colormap