import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

def app():
    #pegando os data frames
    df = pd.read_excel('Atlantic_Slave_Trade_Brazil.xlsx')

    df2 = pd.read_excel('AfricanNamesDatabase.xlsx')


    #calculando a media das variaveis quantitativas
    tabela= df.groupby(["Year of arrival at port of disembarkation"])['Total embarked',"Total disembarked"].sum().reset_index()
    tabela2 = df.groupby(["Local de desembarque"])['Percent children','Total embarked',"Total disembarked"].sum().reset_index()
    y_c = df2['country'].value_counts().values
    x_c = df2['country'].value_counts().index
    y_bar = df2['sexage'].value_counts().values
    x_bar = df2['sexage'].value_counts().index



    #Gráfico de linhas

    st.write("Gráficos do datebase: Atlantic_Slave_Trade_Brazil")

    linha = px.line(tabela, x="Year of arrival at port of disembarkation", 
    y="Total disembarked", title= "Captive people arriving per year")


    st.plotly_chart(linha, use_container_width=True)

    #scatter de numero de raizes

    number = px.bar(tabela2, x="Local de desembarque", y="Total disembarked", 
    title= "Captive people arriving by Brazillian region")          

    st.plotly_chart(number)

    st.write("Gráficos do datebase: AfricanNamesDatabase")
    number = px.bar(x=x_c, y=y_c, color=x_c,
    title= "Native 'home country' of captive people")         

    st.plotly_chart(number)
   
    number = px.bar(x=x_bar, y=y_bar, color=x_bar,
    title= "Captive people by age group")          

    st.plotly_chart(number)


if __name__ == '__main__':
        app()
