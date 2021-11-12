from typing import Text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('プログレスバーの標示')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'



# left_column, rigth_column = st.beta_columns(2) beta_は消す20211102
left_column, rigth_column = st.columns(2)
button = left_column.button('右カラムに文字を標示')
if button:
    rigth_column.write('ここは右カラムです。')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')



# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの好きな趣味は、' , text, 'です。'
# 'コンディション',condition


# if st.checkbox('Show Image'):
#     img = Image.open('0905東京事変ライブ.png')
#     st.image(img, caption='Tokyo', use_column_width=True)



# st.write('DateFrame')
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)


# st.table(df.style.highlight_max(axis=0))
# tableは静的な表、
# st.dataframe(df.style.highlight_max(axis=0))
# st.write(df, width=100, height=100)

# """
# # 章
# ## 節
# ### 項

# ```Python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """