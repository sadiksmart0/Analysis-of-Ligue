
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import numpy as np
import plotly.express as px





data = pd.read_csv("C:/Users/A.M. MUKTAR/DataVisualizationProject/epldat10seasons/Dataset/all_season_table.csv")
clubs_df = pd.read_csv("C:/Users/A.M. MUKTAR/DataVisualizationProject/epldat10seasons/Dataset/All_tables.csv")

club_df1 = clubs_df.groupby(by=['Club','Season'], as_index=False).sum()
club_df2 = clubs_df.groupby(by=['Club','Season'], as_index=False)['Points'].sum()
club_df3 = clubs_df.groupby(by=['Club','Season'], as_index=False)['GoalsScored','GoalsConceded'].sum()
club_df4 = club_df3.groupby(by='Club', as_index=False)['GoalsScored','GoalsConceded'].sum()


# Page Headers
st.subheader('An Insight Into Ten season of EPL Football')

# Page Tabs creation
tab1, tab2, tab3 = st.tabs(["Total Point per Team per Season", "Total Goals Scored per team per Season",  "Total Goals Conceded per Team per Season"])

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
    st.header(" Total goals Conceded Per Team / Per Season")

    
    option = st.selectbox(
        'Select Season?',
        ('2010/11','2011/12','2012/13','2013/14','2014/15','2015/16','2016/17','2017/18','2018/19','2019/20'), key='goals_con')

    goals_con = {'2010/11':'GoalsConceded10_11','2011/12':'GoalsConceded11_12','2012/13':'GoalsConceded12_13','2013/14':'GoalsConceded13_14','2014/15':'GoalsConceded14_15','2015/16':'GoalsConceded15_16','2016/17':'GoalsConceded16_17','2017/18':'GoalsConceded17_18','2018/19':'GoalsConceded18_19','2019/20':'GoalsConceded19_20'}
    if option in point.keys():
        fig3 = px.scatter(data, x='Club', y=goals_con.get(option), size_max=50,size=goals_con.get(option) ,hover_data=[goals.get(option)], color='Club',labels={'pop':'population of Canada'}, height=400)
        st.plotly_chart(fig3, use_container_width=True)



# Page Tabs creation
tab4, tab5, tab6 = st.tabs(["Position and games Lost Per Season  ", "Points  Distribution by Team Accross 10 Season", "Win Percentage Per Team Per Season"])

with tab4:
    st.write(" Position and Games Lost and Per Season")
    
    fig4 = px.sunburst(
    club_df1,
    path=['Season', 'Club'], values='Position', hover_data=['Losses','Position'],
    color='Club'
    )
    st.plotly_chart(fig4, use_container_width=True)

    

with tab5:
    st.header("Total point accross All seasons")

    fig5 = px.line(club_df2, x="Season", y="Points", color='Club', hover_data=['Points'])
    st.plotly_chart(fig5, use_container_width=True)



with tab6:
    st.header("Win Percentage Per Team Per Season")
    fig6 = px.treemap(clubs_df, path=[ 'Season','Club'], values='Win_percentage', color='Club',hover_data=['Draw_Percentage','Loss_Percentage'])
    st.plotly_chart(fig6, use_container_width=True)


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

    #fig10 = px.pie(club_df4, x="Club", y="GoalsScored", color='Club')
    fig10 = px.funnel(club_df4, x='GoalsScored', y='Club', color='Club', hover_data=['GoalsConceded'], height=1000)
    st.plotly_chart(fig10, use_container_width=True)




with tab9:
    st.header("Total Goals & Percentage Across 10 Seasons")
    # fig11 = px.treemap(club_df3, path=[ 'Season','Club'], values='GoalsScored', color='Club',hover_data=['GoalsScored','GoalsConceded'])
    # st.plotly_chart(fig11, use_container_width=True)

    fig11 = px.pie(club_df4, values='GoalsScored', names='Club', title='Total Goals & Percentage  Scored By teams Across Ten Seasons')
    st.plotly_chart(fig11, use_container_width=True)

