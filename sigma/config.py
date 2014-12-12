# Input/Output Services

# Input service
INPUT_SERVICE = "Terminal"

# Output service
OUTPUT_SERVICE = "Terminal"


# Data Files

# Raw data filename
DATA_FILENAME = __import__("pkg_resources").resource_filename("sigma", "data/data.dat")


# User Interface

# Service class names
SERVICES = ["Terminal", "GUI", "Matplotlib", "Rhino", "Blender", "Database", "Filesystem"]

# Modifier class names
MODIFIERS = ["Sigma"]

# Filter class names
FILTERS = ["Filter"]

# Creator class names
CREATORS = ["Crystal", "Branching", "CrystalBranching", "Worm"]
