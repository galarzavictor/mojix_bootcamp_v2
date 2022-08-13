import streamlit as st

# Text Title
st.title("Tutorial de Streamlit")

# Header and Subheader
st.header("Es un Encabezado")
st.subheader("Es un Sub Encabezado")

# Text
st.text("Hola cuateess!!")

# Markdown
st.markdown("### Es un Markdown")

# Error Colorfull text
st.success("Exitooo")
st.info("Informacion")
st.warning("Mensaje de Advertencia")
st.error("Error: es peligroso")
st.exception("NameError('el nombre no ha sido definido')")

# Get Help Info about Python
st.help(range)

# Writing Text/Super Fxn
st.write("Text with write")
st.write(range(10))

# Images
from PIL import Image
img = Image.open("example.jpeg")
st.image(img,width=300,caption="Single Image")

# Videos
vid_file = open("example.mp4","rb").read()
# vid_bytes = vid_file.read()
st.video(vid_file)

# Audio
audio_file = open("miMusiquita01.mp3","rb").read()
st.audio(audio_file,format='audio/mp3')

# widget
# Checkbox
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")
	
# Radio Buttons
status = st.radio("What is your status",("Active","Inactive"))
if status == 'Active':
	st.success("You are Active")
else:
	st.warning("Inactive, Activate")

# SelectBox
occupation = st.selectbox("Cual tu ocupacion?",["Programador","Dentista","Data Scientist"])
st.write("You selected this option ",occupation)

# MultiSelect
location = st.multiselect("Donde trabajas?",("Londres","Nueva York","Bolivia","Nepal"))	
st.write("Tu elegiste ",len(location),"lugares")

# Slider
level = st.slider("What is your level",1,5)

# Buttons
st.button("Simple Button")
if st.button("About"):
	st.text("Streamlit is Cool")
	
# Text Input
firstname = st.text_input("Enter your firstname","Type here...")
if st.button("Submit"):
	result = firstname.title()
	st.success(result)

# Text Area
message = st.text_area("Enter your message","Type Here...")
if st.button("Enviar"):
	resultado = message.title()
	st.success(resultado)

# Date Input
import datetime
today = st.date_input("Today is",datetime.datetime.now())

# Time
the_time = st.time_input("The time is",datetime.time())

# Displaying JSON
st.text("Display JSON")
st.json({'name':"Jesse",'gender':"male"})	

