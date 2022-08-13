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
# audio file = open("examplemusic.mp3","rb").read()
# st.audio(audio_file,format='audio/mp3')

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
	
