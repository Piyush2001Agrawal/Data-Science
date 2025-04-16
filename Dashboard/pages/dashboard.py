import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


st.title("This is the Dashboard Page")

df= sns.load_dataset("titanic")
st.dataframe(df)
 #gender filter
gender= st.sidebar.multiselect('Gender',
                               options= df['sex'].unique(),
                               default= df['sex'].unique())

# pclass filter
pclass= st.sidebar.multiselect('pasanger class',
                               options= df['pclass'].unique(),
                               default= df['pclass'].unique())

filtered_df =df[
    (df['sex'].isin(gender)) &
    (df['pclass'].isin(pclass)) #to check whether the pclass filter has the data of pclass column of df
    #& (df['survived'].isin(survived)) #to check whether the survived filter has the data of survived column of df
    #to check weathe r the gender filter has the data of sex column of df
]

fig = px.sunburst(filtered_df,path=['pclass','sex','survived'],values='age',
            title='Survival by class and gender', width=500, height=500,
        template='plotly_dark', color='age', color_continuous_scale='RdBu')
st.plotly_chart(fig)
st.markdown("This graph shows the survival rate")

fig2= px.histogram(df,x='age',nbins=30,color='survived',title='Age Distribution by Survival',
           template='plotly_dark',)
st.plotly_chart(fig2)

fig3= px.violin(df, x='survived', y='age', color='sex', 
                 box=True, points='all', 
                 title='Age Distribution by Survival and Gender', 
                 template='plotly_dark')
st.plotly_chart(fig3)

fig4= px.scatter_matrix(df, dimensions=['age', 'fare', 'pclass'], color='survived',
                          title='Pair Plot of Age, Fare, Class, and Survival', 
                          color_continuous_scale='viridis',)
st.plotly_chart(fig4)

embark_survival = df.groupby('embark_town')['survived'].mean().reset_index()
fig5= px.line_polar(embark_survival, r='survived', theta='embark_town',
                     line_close=True, title='Survival Rate by Embarkation Town',
                     template='plotly_dark')
st.plotly_chart(fig5)

fig6= px.scatter_3d(df, x='age', y='fare', z='pclass', color='survived',
                      title='3D Scatter Plot: Age, Fare, and Survival',color_continuous_scale='viridis'
                )
st.plotly_chart(fig6)

fig7= px.scatter(df, x='age', y='fare', size='sibsp', color='survived',
                  title='Bubble Chart: Age vs Fare with SibSp',
                  template='plotly_dark')
st.plotly_chart(fig7)

survived_counts= filtered_df['survived'].value_counts()
fig8= px.pie(names=survived_counts.index, values=survived_counts.values,
       title='Survival Rate', template='plotly_dark',
       width=500, height=500)
st.plotly_chart(fig8)