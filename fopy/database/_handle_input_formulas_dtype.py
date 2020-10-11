""" Handle input formulas database types, and convert them to pandas DataFrame
"""
import pandas as pd

class _Handle_input_dtype:

    def __init__(self, data, formula_col='Formula', id_col='ID',
                save_all_derived_formulas=True):
        """Convert data into pandas.DataFrame and generate a graph for formulas.

        """

        #* formula_col, id_col, and graph should be privet attributes "_a"
        self.formula_col = formula_col
        self.id_col = id_col
        if not isinstance(data, pd.DataFrame):
            if isinstance(data, list):
                self._list_to_DataFrame(data)
            elif isinstance(data, set) or isinstance(data, tuple):
                self._list_to_DataFrame(list(data))
            elif isinstance(data, dict):
                self._dict_to_DataFrame(data)
            else:
                raise TypeError('The input data type: "{}" is not supported!\
                                Instead use Pandas.DatFrame, list, dict, tuple\
                                or set'.format(type(data)))
        else:  # pd.DataFrame
            self.data = data
        self._check_id()


    def _list_to_DataFrame(self, data_list):
        self._dict_to_DataFrame({self.formula_col:data_list})

    def _dict_to_DataFrame(self, data_dict):
        if self.formula_col not in data_dict:
            if str(list(data_dict.keys())[0]).isdigit():
                # if the user input: {1:'f=m*a', 2:'v=a*t',}
                self.data = {self.id_col: list(data_dict.keys())}
                self.data[self.formula_col] = list(data_dict.values())
                self.data = pd.DataFrame(self.data)
            else:
                raise Exception('The formula column name must be "{}"'\
                                .format(self.formula_col))
        else:
            self.data = pd.DataFrame(data=data_dict)
        
    def _check_id(self,):
        column = list(self.data)
        if self.id_col not in column:
            self.data[self.id_col] = list(range(1, self.data.shape[0]+1))
            #Sort column oreder for convienant
            self.data = self.data[[self.id_col, *column]]

