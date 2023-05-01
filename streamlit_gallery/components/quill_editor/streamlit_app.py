import streamlit as st
import openai
from streamlit_gallery.utils.readme import readme
from streamlit_quill import st_quill


def main():
    # with readme("streamlit-quill", st_quill, __file__):
    c1, c2 = st.columns([3, 1])

    c2.subheader("Parameters")

    with c1:
        content = st_quill(
            placeholder="Write your text here",
            html=c2.checkbox("Return HTML", False),
            readonly=c2.checkbox("Read only", False),
            key="quill",
        )

        if content:
            st.subheader("Content")


            st.text(content)
    with st.sidebar:
        token_opeai = st.text_input("Введите токен OPENAI:",
                              value="1de87fc11de87fc11de87fc1ee1efb566d11de81de87fc179d10abdb96a9bbfea467460")


if __name__ == "__main__":
    main()
