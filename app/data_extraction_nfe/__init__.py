# This file makes 'data_extracion_nfe' a Python package.

# Define __all__ for 'from my_package import *'
__all__ = ["QRcodeReader", "TextParser", "PACKAGE_VERSION"]

# Import submodules into the package's namespace
from .qrcode_reader import QRcodeReader
from .text_parser import TextParser
from .utils import *

# You can also define package-level variables or functions here
PACKAGE_VERSION = "1.0.0"