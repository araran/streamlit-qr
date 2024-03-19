import streamlit as st
from streamlit.logger import get_logger
from streamlit_qrcode_scanner import qrcode_scanner

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="QRコードスキャン",
        page_icon="👋",
    )

    st.write("# QRコードスキャン 👋")

    st.sidebar.success("オマケのデモです。\n選択してください。")

    st.markdown("マイナンバーカードの裏のQRコートを撮影し必要事項を入力してください。")
    st.image("9284b-546x346.png")

    qr_code = qrcode_scanner(key='qrcode_scanner')

    name = st.text_input('名前', '氏名')

    container = st.container(border=True)
    if qr_code:
        container.write("読み取り番号: " , qr_code)
    container.write('名前: ', name)
    container.button("登録", type="primary")

if __name__ == "__main__":
    run()
