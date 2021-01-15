import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly_express as px

'''
# Club and Nationality App

This very simple webapp allows you to select and visualize players from certain clubs and certain nationalities.
'''
df = st.cache(pd.read_csv)("football_data.csv")

clubs = st.sidebar.multiselect('Show Player for clubs?', df['Club'].unique())
nationalities = st.sidebar.multiselect('Show Player from Nationalities?', df['Nationality'].unique())

new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]
st.write(new_df)

# Create distplot with custom bin_size
fig = px.scatter(new_df, x ='Overall',y='Age',color='Name')

'''
### Here is a simple chart between player age and overall
'''

st.plotly_chart(fig)

html_temp = """<div class='tableauPlaceholder' id='viz1610691990344' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Vi&#47;VizoftheDay2020Analysis&#47;VODin2020&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='VizoftheDay2020Analysis&#47;VODin2020' /><param name='tabs' value='no' /><param name='toolbar' value='no' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Vi&#47;VizoftheDay2020Analysis&#47;VODin2020&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='filter' value='mobile=' /><param name='language' value='ko' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1610691990344');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1290px';vizElement.style.height='2810px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp)
