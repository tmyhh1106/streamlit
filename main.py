import streamlit as st
import numpy as  np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}') # 文章を表示している
    bar.progress(i + 1) #プレグレスバーを動かしている
    time.sleep(0.1) # 0.1秒ずつ進む
    
'Done!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write("ここは右カラムです")

expander = st.expander('問い合わせ')
expander.write("問い合わせ内容を書く")


text = st.text_input('あなたの趣味を教えて下さい')
condition = st.slider('あなたの今の調子は？', 0, 100, 50) # min, max, start
'あなたの趣味：', text # type: ignore
'コンディション：', condition # type: ignore

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、' , option, 'です。' # type: ignore

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption="ケーキバイキング", use_container_width=True)

