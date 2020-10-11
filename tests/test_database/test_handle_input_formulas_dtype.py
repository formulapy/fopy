import pandas as pd
from fopy.database._handle_input_formulas_dtype import * 


d_list = ['f = m*a', 'd = v*t']
d_tuple = tuple(d_list)
d_set = set(d_list)
d_dict_fos = {'Formula': d_list}
d_dict_fos_id = {**d_dict_fos, 'ID':[1,2]}
d_dict_numb = {1:d_list[0], 2:d_list[1]}
d_df = pd.DataFrame(data=d_dict_fos)

good_df = pd.DataFrame(data={'ID':[1, 2], 'Formula':d_list})

def Test_Handle_input_dtype():
    h_list = _Handle_input_dtype(data=d_list)
    assert h_list.data == good_df
    assert False