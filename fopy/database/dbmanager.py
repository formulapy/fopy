"""Manage Formulas database
- Loading
- Saving
- Update
- Test
-
"""

import pandas as pd
from ._handle_input_formulas_dtype import _Handle_input_dtype


class Dbmanager(_Handle_input_dtype, ):

    def __init__(self):
        pass

    def _load_data(self, data):
        self._handle_input_dtype(data)
        if self._save:
            self._save_db()
        