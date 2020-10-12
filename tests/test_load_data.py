import pandas as pd
from pandas._testing import assert_frame_equal
#from fopy.database._handle_input_formulas_dtype import _Handle_input_dtype
from fopy import Formulas

d_list = ['d = v*t', 'f = m*a']
d_tuple = tuple(d_list)
d_set = set(d_list)
d_dict_fos = {'Formula': d_list}
d_dict_fos_id = {'ID':[1,2], **d_dict_fos}
d_dict_num = {1:d_list[0], 2:d_list[1]}
d_df = pd.DataFrame(data=d_dict_fos)

good_df = pd.DataFrame(data={'ID':[1, 2], 'Formula':d_list})

def test_load_data():
    h_list = Formulas(data=d_list)
    assert_frame_equal(h_list.data, good_df)
    
    h_tuple = Formulas(data=d_tuple)
    assert_frame_equal(h_tuple.data, good_df)

    #h_set = _Handle_input_dtype(data=d_set)
    #assert_frame_equal(h_set.data, good_df)

    h_dict_fos = Formulas(data=d_dict_fos)
    assert_frame_equal(h_dict_fos.data, good_df)

    h_dict_fos_id = Formulas(data=d_dict_fos_id)
    assert_frame_equal(h_dict_fos_id.data, good_df)

    h_dict_num = Formulas(data=d_dict_num)
    assert_frame_equal(h_dict_num.data, good_df)

    h_df = Formulas(data=d_df)
    assert_frame_equal(h_df.data, good_df)


