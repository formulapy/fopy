import pandas as pd
from pandas._testing import assert_frame_equal
#from fopy.database._handle_input_formulas_dtype import _Handle_input_dtype
from fopy import Formulas

df = pd.DataFrame(data={'ID':[1,2,3], 'Formula':['Force = mass * Acc', 'Acc = Velocity/time',\
                                    'Electric_field = Force/charge'], 'Field':['CM', 'CM', 'EM']})

df_match_Acc = pd.DataFrame(data={'ID':[1,2], 'Formula':['Force = mass * Acc', 'Acc = Velocity/time'],\
                                  'Field':['CM', 'CM']})

df_match_field_CM = df_match_Acc


def test_search():
    fo = Formulas(data=df)
    fo_Acc = Formulas(data=df_match_Acc)
    fo_field_CM = Formulas(data=df_match_field_CM)

    assert_frame_equal(fo.search('Acc').data, fo_Acc.data)
    assert_frame_equal(fo.search('CM', col='Field').data, fo_field_CM.data)



