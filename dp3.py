# librerías
import streamlit as st
import base64  

# definiendo secciones

# layout
st.title("Portal de Drivers Servicios Falabella")

# funciones de secciones
def download_section():
    """
    Sección para descargar archivos
    """
    # Obtiene el archivo que se desea descargar
    filename = st.selectbox("Seleccione el archivo que desea descargar", ["archivo1.csv", "archivo2.txt"])

    # Mostrar el nombre del archivo
    st.write(f"Descargar {filename}")

    # Botón de descarga
    download_button = st.button("Descargar")
    if download_button:
        # Descarga el archivo
        with open(filename, "rb") as file:
            file_content = file.read()
            base64_file = base64.b64encode(file_content).decode('utf-8')
            href = f'<a href="data:file/{filename.split(".")[-1]};base64,{base64_file}" download="{filename}">Haz clic aquí para descargar</a>'
            st.markdown(href, unsafe_allow_html=True)

def upload_section():
    """
    Sección para subir archivos
    """
    # Obtiene el archivo que se desea subir
    file = st.file_uploader("Seleccione el archivo que desea subir", type=["csv", "txt"])

    # Sube el archivo
    if file is not None:
        # Guarda el archivo en la memoria
        data = file.read()

        # Visualiza el contenido del archivo
        st.write(data)

def results_section():
    """
    Sección para visualizar resultados
    """
    # Visualiza los resultados
    st.write("Aquí se mostrarán los resultados")

# seccionando la página
st.sidebar.title("Menú")
st.sidebar.subheader("Seleccione la sección que desea ver")
selected_section = st.sidebar.radio("Sección", ["Descargar archivos", "Subir archivos", "Visualizar resultados"], key="section")

if selected_section == "Descargar archivos":
    download_section()
elif selected_section == "Subir archivos":
    upload_section()
elif selected_section == "Visualizar resultados":
    results_section()