# _update_parameter.py

__module_name__ = "_update_parameter.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


def _update_parameter(class_object, parameter, value):

    class_object.__setattr__(parameter, value)