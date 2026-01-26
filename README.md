# Test Repository - Python Import Patterns

This repository demonstrates various Python import patterns including:
- Absolute imports
- Relative imports
- Package imports
- Class imports
- Function imports
- Method imports
- Cross-package imports

## Structure

```
test-repo/
├── main.py                 # Main script demonstrating various imports
├── notebook1.ipynb          # Jupyter notebook with absolute imports
├── notebook2.ipynb          # Jupyter notebook with relative imports
├── utils/                   # Utility package
│   ├── __init__.py
│   ├── math_utils.py        # Math utility functions
│   ├── string_utils.py      # String utility functions
│   └── data_processor.py    # Data processing class
└── models/                  # Models package
    ├── __init__.py
    ├── base_model.py        # Base model class
    └── user_model.py        # User model class (inherits from base)
```

## Import Patterns Demonstrated

### Absolute Imports
- `from utils.math_utils import add`
- `from models.user_model import User`
- `import utils.string_utils`

### Relative Imports
- `from .math_utils import multiply`
- `from ..models.base_model import BaseModel`
- `from .string_utils import capitalize_words`

### Package Imports
- `import utils`
- `import models`

### Class Imports
- `from models.user_model import User`
- `from models.base_model import BaseModel`

### Function Imports
- `from utils.math_utils import add, subtract`
- `from utils.string_utils import capitalize_words`

### Method Imports
- Classes with methods that can be imported and used

## Usage

Run the main script:
```bash
python main.py
```

Or open the Jupyter notebooks:
```bash
jupyter notebook notebook1.ipynb
jupyter notebook notebook2.ipynb
```
