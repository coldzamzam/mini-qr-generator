import streamlit as st
import qrcode
from io import BytesIO
import base64

def generate_qr_code(data):
    """
    Fungsi untuk menghasilkan gambar QR code dari data yang diberikan.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

st.set_page_config(page_title="Mini QR Code Generator", page_icon="🔗")

st.title("🔗 Mini QR Code Generator")
st.write("Input text or URL to generate a QR code.")

# Input text from user
user_input = st.text_input("Text or URL:", "")

if user_input:
    # Display the text to be generated as QR (optional)
    st.write(f"Generate QR Code for: `{user_input}`")

    # Generate QR code
    qr_img = generate_qr_code(user_input)

    # Simpan gambar QR ke buffer in-memory
    buf = BytesIO()
    qr_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Tampilkan gambar QR di Streamlit
    st.image(byte_im, caption="Your QR Code", use_container_width=True)

    # Opsi untuk download gambar QR
    st.download_button(
        label="Download QR Code",
        data=byte_im,
        file_name="qrcode.png",
        mime="image/png"
    )
else:
    st.info("Please enter text or URL to generate QR Code.")

st.markdown("---")
st.write("Created with ❤️ by Coldzamzam.")