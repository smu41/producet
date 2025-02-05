from unicodedata import category

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from millify import millify

# read data
total = pd.read_csv('total.csv')
accessories = total[total.category == 'accessories']
bags = total[total.category == 'bags']
beauty = total[total.category == 'beauty']
house = total[total.category == 'house']
jewelry = total[total.category == 'jewelry']
kids = total[total.category == 'kids']
men = total[total.category == 'men']
shoes = total[total.category == 'shoes']
women = total[total.category == 'women']


def Top_10(data):
    data = data.groupby('subcategory')[['likes_count', 'total_prices']].sum().sort_values(by='likes_count', ascending=False).reset_index()
    data.subcategory[10:] = 'Other'
    data_top = data[:10]
    data_total = data.groupby('subcategory')['total_prices'].sum().reset_index()

    return data_top, data_total

def Avg_price(data):
    current_avg_price = data.groupby('subcategory')['current_price'].mean()
    data_index = data.groupby('subcategory')['likes_count'].sum().sort_values(ascending=False).head().index

    return current_avg_price, data_index

# Top 10 the quantity of the sales
accessories_top, accessories_total = Top_10(accessories)
bags_top, bags_total = Top_10(bags)
beauty_top, beauty_total = Top_10(beauty)
house_top, house_total = Top_10(house)
jewelry_top, jewelry_total = Top_10(jewelry)
kids_top, kids_total = Top_10(kids)
men_top, men_total = Top_10(men)
shoes_top, shoes_total = Top_10(shoes)
women_top, women_total = Top_10(women)

# average prices
accessories_avg_prices, accessories_index = Avg_price(accessories)
bags_avg_prices, bags_index = Avg_price(bags)
beauty_avg_prices, beauty_index = Avg_price(beauty)
house_avg_prices, house_index = Avg_price(house)
jewelry_avg_prices, jewelry_index = Avg_price(jewelry)
kids_avg_prices, kids_index = Avg_price(kids)
men_avg_prices, men_index = Avg_price(men)
shoes_avg_prices, shoes_index = Avg_price(shoes)
women_avg_prices, women_index = Avg_price(women)

total_top = total.groupby('category')[['likes_count', 'total_prices']].sum().reset_index()
cate_name = total.category.unique()

st.set_page_config(layout='wide')

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, col8, col9 = st.columns(3)
col10, col11, col12  = st.columns(3)

col1.metric(label='The total account for accessories', value=millify(total_top.total_prices[0]))
col2.metric(label='The total account for bags', value=millify(total_top.total_prices[1]))
col3.metric(label='The total account for beauty', value=millify(total_top.total_prices[2]))
col4.metric(label='The total account for house', value=millify(total_top.total_prices[3]))
col5.metric(label='The total account for jewerly', value=millify(total_top.total_prices[4]))
col6.metric(label='The total account for kids', value=millify(total_top.total_prices[5]))
col7.metric(label='The total account for men', value=millify(total_top.total_prices[6]))
col8.metric(label='The total account for shoes', value=millify(total_top.total_prices[7]))
col9.metric(label='The total account for women', value=millify(total_top.total_prices[8]))
col10.metric(label='The total account', value=millify(sum(total.total_prices)))

name = st.selectbox('select category', cate_name, index=None)

if name == 'accessories':
    fig = px.bar(accessories_top, x='subcategory', y='likes_count', labels={'likes_count': 'Quantity'})
    st.plotly_chart(fig)

    fig_account = px.bar(accessories_top, x='subcategory', y='total_prices', labels={'total_prices': 'Account'})
    st.plotly_chart(fig_account)

    fig_pie= px.pie(accessories_total, values='total_prices', names='subcategory')
    fig_pie.update_traces(textposition='inside', textinfo='label+percent')
    st.plotly_chart(fig_pie)

    fig_avg = go.Figure()
    fig_avg.add_trace(go.Box(y=accessories_avg_prices, name='Average Prices'))
    fig_avg.add_trace(go.Box(y=accessories_avg_prices.loc[accessories_index], name='Top 10 Average Prices'))
    st.plotly_chart(fig_avg)

elif name == 'bags':
    fig = px.bar(bags_top, x='subcategory', y='likes_count', labels={'likes_count': 'Quantity'})
    st.plotly_chart(fig)

    fig_account = px.bar(bags_top, x='subcategory', y='total_prices', labels={'total_prices': 'Account'})
    st.plotly_chart(fig_account)

    fig_pie= px.pie(bags_total, values='total_prices', names='subcategory')
    fig_pie.update_traces(textposition='inside', textinfo='label+percent')
    st.plotly_chart(fig_pie)

    fig_avg = go.Figure()
    fig_avg.add_trace(go.Box(y=bags_avg_prices, name='Average Prices'))
    fig_avg.add_trace(go.Box(y=bags_avg_prices.loc[bags_index], name='Top 10 Average Prices'))
    st.plotly_chart(fig_avg)

elif name == 'beauty':
    fig = px.bar(beauty_top, x='subcategory', y='likes_count', labels={'likes_count': 'Quantity'})
    st.plotly_chart(fig)

    fig_account = px.bar(beauty_top, x='subcategory', y='total_prices', labels={'total_prices': 'Account'})
    st.plotly_chart(fig_account)

    fig_pie = px.pie(beauty_total, values='total_prices', names='subcategory')
    fig_pie.update_traces(textposition='inside', textinfo='label+percent')
    st.plotly_chart(fig_pie)

    fig_avg = go.Figure()
    fig_avg.add_trace(go.Box(y=beauty_avg_prices, name='Average Prices'))
    fig_avg.add_trace(go.Box(y=beauty_avg_prices.loc[beauty_index], name='Top 10 Average Prices'))
    st.plotly_chart(fig_avg)

elif name == 'house':
    fig = px.bar(house_top, x='subcategory', y='likes_count', labels={'likes_count': 'Quantity'})
    st.plotly_chart(fig)

    fig_account = px.bar(house_top, x='subcategory', y='total_prices', labels={'total_prices': 'Account'})
    st.plotly_chart(fig_account)

    fig_pie = px.pie(house_total, values='total_prices', names='subcategory')
    fig_pie.update_traces(textposition='inside', textinfo='label+percent')
    st.plotly_chart(fig_pie)

    fig_avg = go.Figure()
    fig_avg.add_trace(go.Box(y=house_avg_prices, name='Average Prices'))
    fig_avg.add_trace(go.Box(y=house_avg_prices.loc[house_index], name='Top 10 Average Prices'))
    st.plotly_chart(fig_avg)

elif name == 'jewelry':
    fig = px.bar(jewelry_top, x='subcategory', y='likes_count', labels={'likes_count': 'Quantity'})
    st.plotly_chart(fig)

    fig_account = px.bar(jewelry_top, x='subcategory', y='total_prices', labels={'total_prices': 'Account'})
    st.plotly_chart(fig_account)

    fig_pie = px.pie(jewelry_total, values='total_prices', names='subcategory')
    fig_pie.update_traces(textposition='inside', textinfo='label+percent')
    st.plotly_chart(fig_pie)

    fig_avg = go.Figure()
    fig_avg.add_trace(go.Box(y=jewelry_avg_prices, name='Average Prices'))
    fig_avg.add_trace(go.Box(y=jewelry_avg_prices.loc[jewelry_index], name='Top 10 Average Prices'))
    st.plotly_chart(fig_avg)

elif name == 'kids':
    fig = px.bar(kids_top, x='subcategory', y='likes_count', labels={'likes_count': 'Quantity'})
    st.plotly_chart(fig)

    fig_account = px.bar(kids_top, x='subcategory', y='total_prices', labels={'total_prices': 'Account'})
    st.plotly_chart(fig_account)

    fig_pie = px.pie(kids_total, values='total_prices', names='subcategory')
    fig_pie.update_traces(textposition='inside', textinfo='label+percent')
    st.plotly_chart(fig_pie)

    fig_avg = go.Figure()
    fig_avg.add_trace(go.Box(y=kids_avg_prices, name='Average Prices'))
    fig_avg.add_trace(go.Box(y=kids_avg_prices.loc[kids_index], name='Top 10 Average Prices'))
    st.plotly_chart(fig_avg)

elif name == 'men':
    fig = px.bar(men_top, x='subcategory', y='likes_count', labels={'likes_count': 'Quantity'})
    st.plotly_chart(fig)

    fig_account = px.bar(men_top, x='subcategory', y='total_prices', labels={'total_prices': 'Account'})
    st.plotly_chart(fig_account)

    fig_pie = px.pie(men_total, values='total_prices', names='subcategory')
    fig_pie.update_traces(textposition='inside', textinfo='label+percent')
    st.plotly_chart(fig_pie)

    fig_avg = go.Figure()
    fig_avg.add_trace(go.Box(y=men_avg_prices, name='Average Prices'))
    fig_avg.add_trace(go.Box(y=men_avg_prices.loc[men_index], name='Top 10 Average Prices'))
    st.plotly_chart(fig_avg)

elif name == 'shoes':
    fig = px.bar(shoes_top, x='subcategory', y='likes_count', labels={'likes_count': 'Quantity'})
    st.plotly_chart(fig)

    fig_account = px.bar(shoes_top, x='subcategory', y='total_prices', labels={'total_prices': 'Account'})
    st.plotly_chart(fig_account)

    fig_pie = px.pie(shoes_total, values='total_prices', names='subcategory')
    fig_pie.update_traces(textposition='inside', textinfo='label+percent')
    st.plotly_chart(fig_pie)

    fig_avg = go.Figure()
    fig_avg.add_trace(go.Box(y=shoes_avg_prices, name='Average Prices'))
    fig_avg.add_trace(go.Box(y=shoes_avg_prices.loc[shoes_index], name='Top 10 Average Prices'))
    st.plotly_chart(fig_avg)

elif name == 'women':
    fig = px.bar(women_top, x='subcategory', y='likes_count', labels={'likes_count': 'Quantity'})
    st.plotly_chart(fig)

    fig_account = px.bar(women_top, x='subcategory', y='total_prices', labels={'total_prices': 'Account'})
    st.plotly_chart(fig_account)

    fig_pie = px.pie(women_total, values='total_prices', names='subcategory')
    fig_pie.update_traces(textposition='inside', textinfo='label+percent')
    st.plotly_chart(fig_pie)

    fig_avg = go.Figure()
    fig_avg.add_trace(go.Box(y=women_avg_prices, name='Average Prices'))
    fig_avg.add_trace(go.Box(y=women_avg_prices.loc[women_index], name='Top 10 Average Prices'))
    st.plotly_chart(fig_avg)

else:
    fig = px.bar(total_top, x='category', y='likes_count', labels={'likes_count': 'Quantity'})
    st.plotly_chart(fig)

    fig_prices = px.bar(total_top, x='category', y='total_prices', labels={'total_prices': 'Account'})
    st.plotly_chart(fig_prices)