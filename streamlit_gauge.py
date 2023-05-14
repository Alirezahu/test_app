#https://echarts.apache.org/v4/en/option.html#series-gauge.data.value

import random
from streamlit_echarts import st_echarts
import streamlit as st
import math as Math
import time
# temp = 40
temp = [random.randint(0, 100) for _ in range(1)]
st.set_page_config(layout="wide")
col1, col2, col3, col4, col5=st.columns([0.2, 1, 0.2, 1, 0.2])
with col1:
    st.empty()
with col2:
    option = {
  "series": [{
    "name": "Indicator",
    "type": "gauge",
    "detail": {
      "formatter": "{value}C"
    },
    "axisLine":{
                "lineStyle":{
                    "color":[[0.2, '#91c7ae'], [0.8, '#63869e'], [1, '#c23531']]
                },
            },
    "itemStyle": {
                "color": 'auto'},
    "data": [{
      "value": temp,
      "name": "Temperature"
    }]
  }]
}


    # option.series[0].data[0].value = 80;
    # myChart.setOption(option, true);

##thissss
# st_echarts(options=option, key="1")
# st_echarts(options=option, key="chart")




# time.sleep(3)
# temp = 80
# option['series'] = [dict(option['series'][0], type= 'guage')]
# st_echarts(options=option, key="1")

# st_echarts.setOption({
#     "series": [{
#         "data": [{
#       "value": temp,}]
#     }]
        
# })

if "iteration" not in st.session_state:
    st.session_state["iteration"] = 0
# while st.session_state["iteration"] < 10:
# while st.session_state["iteration"] < 100:
while True:
    st.markdown(f"Iteration number {st.session_state['iteration']}")

    with col2:
        st_echarts(option, height="500px", key="chart")
    time.sleep(1)
    st.session_state["iteration"] += 1

    if st.session_state["iteration"] < 100:
        st.experimental_rerun()
# for i in range(10):
#     time.sleep(3)
#     temp = i*10
#     st_echarts(options=option, key="chart")

