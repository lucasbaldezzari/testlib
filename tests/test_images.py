from testlib.logging_config import configure_logging
configure_logging(level="DEBUG") #"DEBUG"
import numpy as np

# from testlib.images import transform
# transform.conv2D()
# transform.modifyContrast()

# from testlib.images.transform import conv2D, modifyContrast
# conv2D()
# modifyContrast()

from testlib.images.transform import *
conv2D()
modifyContrast()

##visualización
from testlib.images import visualization
visualization.show()