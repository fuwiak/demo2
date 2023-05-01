import streamlit as st

from streamlit_gallery import apps, components
from streamlit_gallery.utils.page import page_group

def main():
    page = page_group("p")


    if 'streamlit_gallery.utils.page_page_group_p' not in st.session_state:
        st.session_state['streamlit_gallery.utils.page_page_group_p'] = 0

    with st.sidebar:
        st.title("🎈 Aisullu Social Spy")

        with st.expander("✨ APPS", True):
            page.item("Streamlit gallery", apps.gallery, default=True)

        with st.expander("🧩 COMPONENTS", True):
            page.item("Ace editor", components.ace_editor)
            page.item("Disqus", components.disqus)
            page.item("Analytics📊", components.elements)
            page.item("Pandas AI🐼", components.pandas_profiling)
            page.item("GPT editor", components.quill_editor)
            page.item("Video analyzer", components.react_player)

        # with st.sidebar:
        #     token = st.text_input("Введите токен:",
        #                           value="1de87fc11de87fc11de87fc1ee1efb566d11de81de87fc179d10abdb96a9bbfea467460")
        #     # token = st.text_input("Введите токен:", value="2ff60f692ff60f692ff60f695e2ce4eed822ff62ff60f694c094cb35bc606f13492ff84")
        #     count = st.text_input("Введите количество постов:", value=100)



    page.show()

if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Gallery by Okld", page_icon="🎈", layout="wide")
    main()
