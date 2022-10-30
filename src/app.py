
from turtle import color
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import numpy as np
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt


# Loading Data and DataFrame

data = pd.read_csv("C:/Users/A.M. MUKTAR/DataVisualizationProject/Dataset/all_12_seasons.csv")
clubs_df = pd.read_csv("C:/Users/A.M. MUKTAR/DataVisualizationProject/Dataset/All_Ligue1.csv")
extra_df = pd.read_csv("C:/Users/A.M. MUKTAR/DataVisualizationProject/Dataset/all_match_stats.csv")


club_df1 = clubs_df.groupby(by=['Club','Season'], as_index=False).sum()
club_df2 = clubs_df.groupby(by=['Club','Season'], as_index=False)['Points'].sum()
club_df3 = clubs_df.groupby(by=['Club','Season'], as_index=False)['GoalsScored','GoalsConceded'].sum()
club_df4 = club_df3.groupby(by='Club', as_index=False)['GoalsScored','GoalsConceded'].sum()


#Fair play Dataset
fairplay_df = extra_df.groupby(by=["HomeTeam"], as_index=False)["HomeYellowCards","AwayYellowCards","HomeRedCards","AwayRedCards","HomeFouls","AwayFouls"].sum()
fairplay_df["Total_YellowCards"] = fairplay_df["HomeYellowCards"] + fairplay_df["AwayYellowCards"]
fairplay_df["Total_RedCards"] = fairplay_df["HomeRedCards"] + fairplay_df["AwayRedCards"]
fairplay_df["Total_fouls"] = fairplay_df["HomeFouls"] + fairplay_df["AwayFouls"]





#Site Image/logo

image = Image.open('C:/Users/A.M. MUKTAR/DataVisualizationProject/Images/ligue_1.png')

st.image(image, caption='The French Ligue 1')


# Page Headers
st.subheader('An Insight Into 12 seasons of Ligue 1 Football 2010 - 2022')


with st.expander("Insight 1"):
    # Page Tabs creation
    tab1, tab2, tab3 = st.tabs(["Total Point per Team per Season", "Total Goals Scored per team per Season",  "Total Goals Conceded per Team per Season"])

    with tab1:
        option = st.selectbox(
            'Select Season?',
            ('2010/11','2011/12','2012/13','2013/14','2014/15','2015/16','2016/17','2017/18','2018/19','2019/20','2020/21','2021/22'), key='points')

        point = {'2010/11':'Points_10/11','2011/12':'Points_11/12','2012/13':'Points_12/13','2013/14':'Points_13/14','2014/15':'Points_14/15','2015/16':'Points_15/16','2016/17':'Points_16/17','2017/18':'Points_17/18','2018/19':'Points_18/19','2019/20':'Points_19/20','2020/21':'Points_20/21','2021/22':'Points_21/22'}
        st.header("Total Points Per Team for Season ", option)
        if option in point.keys():
            fig1 = px.bar(data, x='Club', y=point.get(option),hover_data=[point.get(option)], color='Club', height=400,text_auto='.2s')
            fig1.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
            st.plotly_chart(fig1, use_container_width=True)
            
    with tab2:
        st.write("Goals Per team / Per season")

        
        option = st.selectbox(
            'Select Season?',
            ('2010/11','2011/12','2012/13','2013/14','2014/15','2015/16','2016/17','2017/18','2018/19','2019/20','2020/2021','2021/22'), key='goalsScored')

        goals = {'2010/11':'GoalsScored_10/11','2011/12':'GoalsScored_11/12','2012/13':'GoalsScored_12/13','2013/14':'GoalsScored_13/14','2014/15':'GoalsScored_14/15','2015/16':'GoalsScored_15/16','2016/17':'GoalsScored_16/17','2017/18':'GoalsScored_17/18','2018/19':'GoalsScored_18/19','2019/20':'GoalsScored_19/20','2020/21':'GoalsScored_20/21','2021/22':'GoalsScored_21/22'}
        st.header("Total goals scored by Each Team in Season :", option)
        if option in point.keys():
            fig2 = px.scatter(data, x='Club', y=goals.get(option), size_max=70,size=goals.get(option) ,hover_data=[goals.get(option)], color='Club',labels={'pop':'population of Canada'}, height=400)
            st.plotly_chart(fig2, use_container_width=True)


    with tab3:
        st.header(" Total goals Conceded Per Team / Per Season")

        
        option = st.selectbox(
            'Select Season?',
            ('2010/11','2011/12','2012/13','2013/14','2014/15','2015/16','2016/17','2017/18','2018/19','2019/20','2020/2021','2021/22'), key='goals_con')

        goals_con = {'2010/11':'GoalsConceded_10/11','2011/12':'GoalsConceded_11/12','2012/13':'GoalsConceded_12/13','2013/14':'GoalsConceded_13/14','2014/15':'GoalsConceded_14/15','2015/16':'GoalsConceded_15/16','2016/17':'GoalsConceded_16/17','2017/18':'GoalsConceded_17/18','2018/19':'GoalsConceded_18/19','2019/20':'GoalsConceded_19/20','2020/21':'GoalsConceded_20/21','2021/22':'GoalsConceded_21/22'}
        if option in point.keys():
            fig3 = px.scatter(data, x='Club', y=goals_con.get(option), size_max=30,size=goals_con.get(option) ,hover_data=[goals.get(option)], color='Club', height=400, symbol="Club")
            st.plotly_chart(fig3, use_container_width=True)


with st.expander("Insight 2"):
    # Page Tabs creation
    tab4, tab5, tab6 = st.tabs(["Position and games Lost Per Season  ", "Points Distribution by Team Across 12 Season", "Win Percentage Per Team Per Season"])

    with tab4:
        st.header(" Position and Games Lost and Per Season")
        
        fig4 = px.sunburst(
        club_df1,
        path=['Season', 'Club'], values='Position', hover_data=['Losses','Position'],
        color='Club'
        )
        st.plotly_chart(fig4, use_container_width=True)   

    with tab5:
        st.header("Total point across All seasons")
        option = st.selectbox(
            'Select Season?',
            club_df3.Club.unique(), key='clubs_point')

        if option in club_df3.Club.unique():
            fig5 = px.line(club_df2[club_df2["Club"]==option], x="Season", y="Points", color='Club', hover_data=['Points'])
            st.plotly_chart(fig5, use_container_width=True)


    with tab6:
        st.header("Win Percentage Per Team Per Season")
        fig6 = px.treemap(clubs_df, path=['Season','Club'], values='Win_Percentage', color='Club',hover_data=['Draw_Percentage','Loss_Percentage'])
        st.plotly_chart(fig6, use_container_width=True)

with st.expander("Insight 3"):
    # Page Tabs creation
    tab7, tab8, tab9 = st.tabs(["Goals scored Per team for Each Season", "Goals Scored & Distribution by Team", "Goals Percentage Across all Season"])
    with tab7:
        st.header("Goals scored Per team for Each Season")
        option = st.selectbox(
            'Select Season?',
            club_df3.Club.unique(), key='clubs')

        if option in club_df3.Club.unique():
            fig9 = px.histogram(club_df3[club_df3['Club'] == option], x='Club', y="GoalsScored",
                    color='Season', barmode='group',
                    height=400)
            st.plotly_chart(fig9, use_container_width=True)    

        else:
            st.write("Team Not Selected")    

            
    with tab8:
        st.header("Total Goals Scored and Conceded Per team")

        fig10 = px.funnel(club_df4, x='GoalsScored', y='Club', color='Club', hover_data=['GoalsConceded'], height=1000)
        st.plotly_chart(fig10, use_container_width=True)

with tab9:
    st.header("Total Goals & Percentage Across 10 Seasons")
    fig11 = px.pie(club_df4, values='GoalsScored', names='Club')
    st.plotly_chart(fig11, use_container_width=True)


with st.expander("Insight 4"):
    st.header("Fair Play Stats")
    # Page Tabs creation
    tab10, tab11, tab12 = st.tabs(["Total Yellow Cards per club", "Total Red Cards per club", "Total fouls committed"])
 
with tab10:
    st.header("Total Yellows In accross all 12 seasons")
    st.area_chart(data=fairplay_df, x="Total_YellowCards", y="HomeTeam", width=0, height=0, use_container_width=True)


with tab11:
    st.header("title='Total Red Cards per club")
    fig13 = px.pie(fairplay_df, values='Total_RedCards', names='HomeTeam', hole=.4, height=1000)
    st.plotly_chart(fig13, use_container_width=True)
with tab12:
    st.header('Total fouls committed per team Teams accross 12 Season')
    fig14, ax = plt.subplots(figsize= (15,20))
    ax.barh( y=fairplay_df["HomeTeam"], width=fairplay_df["Total_fouls"])
    for index, value in enumerate(fairplay_df["Total_fouls"]):
        ax.text(value, index,
                str(value))
    st.pyplot(fig14, clear_figure=True)
    