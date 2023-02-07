import streamlit as st
import random
import base64

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_img = get_img_as_base64("unlucky.jpg")
side_img = get_img_as_base64("unlucky.jpg")

page_bg_img = f"""
    <style>
    .body {{
        font-size:200px;
    }}

    [data-testid="stAppViewContainer"]
    {{
        background-image: url("data:image/jpg;base64,{bg_img}");
        background-position: center;
        background-repeat: no-repeat;
        }}
    .coolesttitle{{
        font-size:50px;
    }}
    </style>"""

st.markdown(page_bg_img , unsafe_allow_html=True)


students = ["Federico",
            "Catalina",
            "Marti",
            "Rodrigo",
            "Ludwig",
            "Justin",
            "AlbertoP",
            "AlbertoR",
            "Francesco",
            "Denes",
            "Roberto"]


st.title("Recap's Little Wheel of Fortune!")

box = st.button("Click me!")
max_iter = 2000
magic_number = 3
if box:
    selected_students = []
    cnt = 0
    while True:
        cnt += 1
        student = random.choice(students)

        selected_students.append(student)
        if cnt > max_iter:
            break

        if selected_students.count(student) == magic_number:
            break

    st.markdown("Nobody gets justice. People only get good luck or bad luck.")

    st.markdown(f"Fortune Winner: '{student}'")
    st.balloons()
