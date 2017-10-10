import os
import sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
grandparent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
vendor_dir = os.path.join(grandparent_dir, 'vendor')

sys.path.append(vendor_dir)

from server import cert

