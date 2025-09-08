# This file makes 'data_extracion_nfe' a Python package.

# Define __all__ for 'from my_package import *'
__all__ = ["qrcode_reader", "test", "PACKAGE_VERSION"]

# Import submodules into the package's namespace
from .qrcode_reader import QRcodeReader
from .utils import utils

# You can also define package-level variables or functions here
PACKAGE_VERSION = "1.0.0"