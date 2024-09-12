import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

#print(car_data.head(5))
#print()
#print(car_data.info())

st.title('Venta de Autos en U.S.A.')

st.write('Mostramos los datos recopilados de ventas de autos en Estados Unidos')

st.dataframe(car_data)

st.write()

hist_boton= st.checkbox('Generar  Histograma')


if hist_boton: 
    st.write('Creación de un histograma para el conjunto de datos de kilometraje')
            
            
    fig = px.histogram(car_data, x="odometer")
        
            
    st.plotly_chart(fig, use_container_width=True)

disp_boton= st.button('Generar  Grafica de dispercion')

if disp_boton:
    st.write('Creacion de Grafica de dispercion para el conjunto de datos del kilometraje Kilometraje')
    
    fig_b = px.scatter(car_data, x="odometer")
    
    st.scatter_chart(fig_b, use_container_width=True)
    
st.write('Si la informacion ha sido util haznoslo saber .')
feedback = st.feedback('stars')
if feedback is None:
    st.write("Trabajamos para mejorar")
elif feedback is not None:
    st.write("Gracias por su consulta")

