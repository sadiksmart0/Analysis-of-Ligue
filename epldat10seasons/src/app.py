
import streamlit as st
import pandas as pd
#import plotly.figure_factory as ff
import numpy as np
import plotly.express as px





data = pd.read_csv("C:/Users/A.M. MUKTAR/Documents/epldat10seasons/Dataset/all_season_table.csv")
clubs_df = pd.read_csv("C:/Users/A.M. MUKTAR/Documents/epldat10seasons/Dataset/All_tables.csv")

club_df1 = clubs_df.groupby(by=['Club','Season'], as_index=False).sum()
club_df2 = clubs_df.groupby(by=['Club','Season'], as_index=False)['Points'].sum()
club_df3 = clubs_df.groupby(by=['Club','Season'], as_index=False)['GoalsScored','GoalsConceded'].sum()


# Page Headers
st.subheader('An Insight Into Ten season of EPL Football')

# Page Tabs creation
tab1, tab2, tab3 = st.tabs(["Total Point per season", "Total goals team per Season","Total winning per season"])

with tab1:
    option = st.selectbox(
        'Select Season?',
        ('2010/11','2011/12','2012/13','2013/14','2014/15','2015/16','2016/17','2017/18','2018/19','2019/20'), key='points')

    point = {'2010/11':'Points10_11','2011/12':'Points11_12','2012/13':'Points12_13','2013/14':'Points13_14','2014/15':'Points14_15','2015/16':'Points15_16','2016/17':'Points16_17','2017/18':'Points17_18','2018/19':'Points18_19','2019/20':'Points19_20'}
    st.header("Total Points Per Team for Season ", option)
    if option in point.keys():
        fig1 = px.bar(data, x='Club', y=point.get(option),hover_data=[point.get(option)], color='Club',labels={'pop':'population of Canada'}, height=400)
        st.plotly_chart(fig1, use_container_width=True)
with tab2:
    st.write("Goals Per team / Per season")

    
    option = st.selectbox(
        'Select Season?',
        ('2010/11','2011/12','2012/13','2013/14','2014/15','2015/16','2016/17','2017/18','2018/19','2019/20'), key='goalsScored')

    goals = {'2010/11':'GoalsScored10_11','2011/12':'GoalsScored11_12','2012/13':'GoalsScored12_13','2013/14':'GoalsScored13_14','2014/15':'GoalsScored14_15','2015/16':'GoalsScored15_16','2016/17':'GoalsScored16_17','2017/18':'GoalsScored17_18','2018/19':'GoalsScored18_19','2019/20':'GoalsScored19_20'}
    st.header("Total goals scored by Each Team in Season :", option)
    if option in point.keys():
        fig2 = px.scatter(data, x='Club', y=goals.get(option), size_max=50,size=goals.get(option) ,hover_data=[goals.get(option)], color='Club',labels={'pop':'population of Canada'}, height=400)
        st.plotly_chart(fig2, use_container_width=True)


with tab3:
    st.header(" Total goals Conceded Per Team Per Season")

    
    option = st.selectbox(
        'Select Season?',
        ('2010/11','2011/12','2012/13','2013/14','2014/15','2015/16','2016/17','2017/18','2018/19','2019/20'), key='goals_con')

    goals_con = {'2010/11':'GoalsConceded10_11','2011/12':'GoalsConceded11_12','2012/13':'GoalsConceded12_13','2013/14':'GoalsConceded13_14','2014/15':'GoalsConceded14_15','2015/16':'GoalsConceded15_16','2016/17':'GoalsConceded16_17','2017/18':'GoalsConceded17_18','2018/19':'GoalsConceded18_19','2019/20':'GoalsConceded19_20'}
    if option in point.keys():
        fig3 = px.scatter(data, x='Club', y=goals_con.get(option), size_max=50,size=goals_con.get(option) ,hover_data=[goals.get(option)], color='Club',labels={'pop':'population of Canada'}, height=400)
        st.plotly_chart(fig3, use_container_width=True)



# Page Tabs creation
tab4, tab5, tab6 = st.tabs(["Clubs Stats     ", "Point Distribution by Team Accross Season", "      View Past Predictions"])

with tab4:
    st.write("Club Statistics over ten Seasons")
    
    fig4 = px.sunburst(
    club_df1,
    path=['Season', 'Club'], values='Points',
    color='Club'
    )
    st.plotly_chart(fig4, use_container_width=True)

    

with tab5:
    st.header("Total point accross All seasons")

    fig5 = px.line(club_df2, x="Season", y="Points", color='Club')
    st.plotly_chart(fig5, use_container_width=True)



with tab6:
    st.header("This is tab 6")
    fig6 = px.treemap(club_df2, path=[ 'Season','Club'], values='Points', color='Club')
    st.plotly_chart(fig6, use_container_width=True)


# Page Tabs creation
tab7, tab8, tab9 = st.tabs(["Goals scored ", "Goals Scored Distribution by Team", "View Past Predictions"])
with tab7:
    st.write("Club Statistics over ten Seasons")
    


    

with tab8:
    st.header("Total point accross All seasons")

    fig10 = px.line(club_df3, x="Club", y="GoalsScored", color='Club')
    st.plotly_chart(fig10, use_container_width=True)



with tab9:
    st.header("This is tab 9")
    fig11 = px.treemap(club_df3, path=[ 'Club','GoalsScored'], values='GoalsScored', color='Club')
    st.plotly_chart(fig11, use_container_width=True)

