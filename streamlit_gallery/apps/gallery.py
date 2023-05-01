import streamlit as st

from PIL import Image
from pathlib import Path

image1 = Image.open('./media/images/mountains.png')
image2 = Image.open('./media/images/AI_logo.png')


def main():
    st.markdown((Path(__file__).parents[2] / "README.md").read_text())
    st.image(image1,
             caption='Creator: User Neil Iris (@neil_ingham) from Unsplash')
    st.image(image2, caption='Powered by Quaantum AI', width=50)


if __name__ == "__main__":
    main()
