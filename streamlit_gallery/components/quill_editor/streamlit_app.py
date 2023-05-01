import streamlit as st

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
        token = st.text_input("Введите токен OPENAI:",
                              value="1de87fc11de87fc11de87fc1ee1efb566d11de81de87fc179d10abdb96a9bbfea467460")
        # token = st.text_input("Введите токен:", value="2ff60f692ff60f692ff60f695e2ce4eed822ff62ff60f694c094cb35bc606f13492ff84")
        count = st.text_input("Введите количество постов:", value=100)


if __name__ == "__main__":
    main()
