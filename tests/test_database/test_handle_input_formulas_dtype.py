import pandas as pd
from pandas._testing import assert_frame_equal
from fopy.database._handle_input_formulas_dtype import _Handle_input_dtype


d_list = ['d = v*t', 'f = m*a']
d_tuple = tuple(d_list)
d_set = set(d_list)
d_dict_fos = {'Formula': d_list}
d_dict_fos_id = {'ID':[1,2], **d_dict_fos}
d_dict_num = {1:d_list[0], 2:d_list[1]}
d_df = pd.DataFrame(data=d_dict_fos)

good_df = pd.DataFrame(data={'ID':[1, 2], 'Formula':d_list})

def test_Handle_input_dtype():
    h_list = _Handle_input_dtype(data=d_list)
    assert_frame_equal(h_list.data, good_df)
    
    h_tuple = _Handle_input_dtype(data=d_tuple)
    assert_frame_equal(h_tuple.data, good_df)

    #h_set = _Handle_input_dtype(data=d_set)
    #assert_frame_equal(h_set.data, good_df)

    h_dict_fos = _Handle_input_dtype(data=d_dict_fos)
    assert_frame_equal(h_dict_fos.data, good_df)

    h_dict_fos_id = _Handle_input_dtype(data=d_dict_fos_id)
    assert_frame_equal(h_dict_fos_id.data, good_df)

    h_dict_num = _Handle_input_dtype(data=d_dict_num)
    assert_frame_equal(h_dict_num.data, good_df)

    h_df = _Handle_input_dtype(data=d_df)
    assert_frame_equal(h_df.data, good_df)


