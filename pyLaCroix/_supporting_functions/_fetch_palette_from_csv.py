# _fetch_palette_from_csv.py

__module_name__ = "_fetch_palette_from_csv.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


def _fetch_palette_from_csv(filepath):
    
    """"""
    
    LaCroixPaletteDict = {}
    
    file = open(filepath + "/../../docs/data/palette.v0.csv")
    for line in file:

        line = line.strip('\n')

        if line.startswith(','):
            continue
        else:
            l= line.split(',')
            l2 = []
            for i in l[1:]:
                if i != '':
                    l2.append(i)
            
        LaCroixPaletteDict[l[0]] = l2
        
    return LaCroixPaletteDict