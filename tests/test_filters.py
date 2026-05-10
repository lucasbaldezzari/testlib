from testlib.logging_config import configure_logging
configure_logging(level="DEBUG") #"ERROR"
import numpy as np

## probando filter
from testlib.signals import Filter

f = Filter()
signal = np.array([1,2,3,4])
_ = f.pasabajos(signal)