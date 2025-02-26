from together import Together
import streamlit as st 


st.set_page_config(page_title="AI Image Generator", page_icon="🎨")

client = Together(api_key = "88a1069d6468d3f7827919e0bb483e75ed87268ebaa6ea556dea8a7150db12a1")
st.title("🎨 AI Image Generator with Together.AI")
prompt = st.text_area("Enter your image description:")

hide_st_style = """ 
    <style> 
    #MainMenu {visibility: hidden;} 
    footer {visibility: hidden;} 
    .stAppHeader  {visibility: hidden;}
    </style> 
""" 
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stApp {
       background: linear-gradient(109.6deg, rgb(204, 228, 247) 11.2%, rgb(237, 246, 250) 100.2%);

    }
    button{
    background-color: #f0ffff;
    }
    </style>

    """,
    unsafe_allow_html=True
)


if st.button("Generate Image"):
    if prompt:
        try:
            response = client.images.generate(prompt=prompt, model="black-forest-labs/FLUX.1-schnell", steps=4)
            st.image(response.data[0].url, caption="Generated Image")
            st.balloons()
        except Exception as e:
             st.error(e)
    else:
        st.error("Please enter an image description.")

