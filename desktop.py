import streamlit as st
from streamlit_drawable_canvas import st_canvas

n = 1
st.header("Kiru's Drawing Space")

if n ==1:
  bg_color = "white"
  pen_color = "black"
  shape = "freedraw" 


pen_size = int(st.number_input("Pen Size"))
width = int(st.number_input("Width"))
height = int(st.number_input("Height"))

if n ==1:
   pen_size = 5
   width = 1500
   height = 1500

n += 1
st.title("Background color")
cl1, cl2, cl3, cl4, cl5, cl6 = st.columns(6)
with cl1:
   white = st.button("white-bg")
   if white:
       bg_color = "white"
with cl2: 
   blue = st.button("blue-bg")
   if blue:
       bg_color = "blue"
with cl3:
   red = st.button("red-bg")
   if red:
       bg_color = "red"
with cl4:
   green = st.button("green-bg")
   if green:
       bg_color = "green"
with cl5:
   yellow = st.button("yellow-bg")
   if yellow:
       bg_color = "yellow"
with cl6:
   black = st.button("black-bg")
   if black:
       bg_color = "black"


st.title("Pen color")
c1, c2, c3, c4, c5, c6 = st.columns(6)
with c1:
   white1 = st.button("white")
   if white1:
       pen_color = "white"
with c2:
   blue1 = st.button("blue")
   if blue1:
       pen_color = "blue"
with c3:
   red1 = st.button("red")
   if red1:
       pen_color = "red"
with c4:
   green1 = st.button("green")
   if green1:
       pen_color = "green"
with c5:
   yellow1 = st.button("yellow")
   if yellow1:
       pen_color = "yellow"
with c6:
   black1 = st.button("black")
   if black1:
       pen_color = "black"

st.title("Shapes")
col1, col2, col3, col4 = st.columns(4)
with col1:
   circle = st.button("circle")
   if circle:
       shape = "circle" 
with col2:
   rect = st.button("rectangle")
   if rect:
       shape = "rect"
with col3:
   point = st.button("point")
   if point:
       shape = "point"
with col4:
   free_draw = st.button("freedraw")
   if free_draw:
       shape = "freedraw"

st.write("")
colu1, colu2, colu4, colu3, colu5 = st.columns(5)
with colu4:
    st.button("OK")

canvas = st_canvas(
        fill_color=bg_color,
        stroke_width=pen_size,
        stroke_color=pen_color,
        background_color=bg_color,
        height=height,
        width=width,
        drawing_mode=shape,
        key="canvas"
)