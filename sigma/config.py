# Global Configuration

# Input service
INPUT_SERVICE = "Terminal"

# Output service
OUTPUT_SERVICE = "Terminal"

# Service class names
SERVICES = ["Terminal", "GUI", "Matplotlib", "Rhino", "Blender", "Database", "Filesystem"]

# Modifier class names
MODIFIERS = ["SigmaModifier"]

# Filter class names
FILTERS = ["SigmaFilter"]

# Creator class names
CREATORS = ["CrystalCreator", "BranchingCreator", "CrystalBranchingCreator", "WormCreator"]

# Raw data filename
DATA_FILENAME = __import__("pkg_resources").resource_filename("sigma", "data/data.dat")

# Local Configuration

# Terminal Service

# Matplotlib Service

# Rhino Service

# Blender Service

# Database Service

# Filestystem Service
