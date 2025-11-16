import streamlit as st
import os
from PIL import Image
import time

# ---------------- APP TITLE ----------------
st.set_page_config(page_title="Birthday App", layout="centered")
st.markdown(
    "<h1 style='text-align:center; color:#ff1493;'>🎉 Welcome to the Birthday App 🎉</h1>",
    unsafe_allow_html=True
)

# ---------------- ENTER NAME ----------------
name = st.text_input("Enter your name:")

if name:
    # ---------------- SHOW MEMORIES BUTTON ----------------
    if st.button("📸 Press to See Your Memories"):
        # ---------------- COUNTDOWN ----------------
        for i in range(3, 0, -1):
            st.write(f"Starting in {i}…")
            time.sleep(1)
            st.empty()

        # ---------------- BIRTHDAY MESSAGE ----------------
        st.markdown(f"""
        <div style='font-size:20px; text-align:center; margin-top:20px;'>

        🎉 Today is a very special day — it’s your 18th Birthday, Molvi G! 🎉<br><br>

        Molvi G, may this year bring you endless happiness, success, and unforgettable memories. 💖<br>
        May you always stay strong, cheerful, and full of love for everyone around you. 🌟<br>
        May every step you take in life be guided by wisdom and may you achieve all your dreams. ✨<br>
        May laughter, joy, and positivity surround you every day. 🎈<br>
        May you grow in strength, kindness, and courage, and may your heart always remain pure. ❤️<br><br>

        🎉 <b>Urdu Wishes</b> 🎉<br>
        مولوی جی، آپ کی زندگی خوشیوں سے بھرپور ہو، ہر دن کامیابی اور سکون کے ساتھ آئے۔ 🌙<br>
        اللہ آپ کی محنت کو کامیابی میں بدل دے، اور آپ کے ہر خواب کو حقیقت میں تبدیل کرے۔ 💫<br>
        آپ کے دوست اور خاندان ہمیشہ آپ کے ساتھ خوش رہیں، اور ہر لمحہ آپ کے لیے محبت اور خوشی لے کر آئے۔ ❤️<br>
        اللہ آپ کو صحت مند، مضبوط اور ہمیشہ خوش رہنے والا دل عطا فرمائے۔ 🌹<br>
        ہر دن آپ کے لیے نیا آغاز، نئی خوشیاں اور نئے مواقع لے کر آئے۔ 🎊<br>
        مولوی جی، اللہ آپ کو علم کی روشنی، دل کی سکونت اور ہر دعا کی قبولیت دے۔ 🙏<br><br>

        🎶 <b>چھوٹی سی شاعری</b> 🎶<br>
        ہر دن آپ کے چہرے پر مسکان ہو، اور دل میں خوشی کے پھول کھلیں۔ 🌸<br><br>

        </div>
        """, unsafe_allow_html=True)

        # ---------- DISPLAY ALL IMAGES IN ROOT ----------
        image_files = [f for f in os.listdir('.') if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]
        if image_files:
            st.markdown("<h2 style='text-align:center; color:blue;'>📷 Your Pictures 📷</h2>", unsafe_allow_html=True)
            for img in image_files:
                st.image(img, use_column_width=True)
                st.write("----")
        else:
            st.warning("No images found in the repository root.")

        # ---------- DISPLAY ALL VIDEOS IN ROOT ----------
        video_files = [f for f in os.listdir('.') if f.lower().endswith((".mp4", ".mov", ".mkv"))]
        if video_files:
            st.markdown("<h2 style='text-align:center; color:green;'>🎥 Your Videos 🎥</h2>", unsafe_allow_html=True)
            for vid in video_files:
                st.video(vid)
                st.write("----")
        else:
            st.warning("No videos found in the repository root.")

        # ---------------- FINAL GREETING MESSAGE ----------------
        st.markdown("""
        <h1 style='text-align:center; color:red; margin-top:40px;'>
        🕌 Murshid G, Assalam o Alaikum 🕌
        </h1>
        """, unsafe_allow_html=True)        🎉 <b>Urdu Wishes</b> 🎉<br>
        مولوی جی، آپ کی زندگی خوشیوں سے بھرپور ہو، ہر دن کامیابی اور سکون کے ساتھ آئے۔ 🌙<br>
        اللہ آپ کی محنت کو کامیابی میں بدل دے، اور آپ کے ہر خواب کو حقیقت میں تبدیل کرے۔ 💫<br>
        آپ کے دوست اور خاندان ہمیشہ آپ کے ساتھ خوش رہیں، اور ہر لمحہ آپ کے لیے محبت اور خوشی لے کر آئے۔ ❤️<br>
        اللہ آپ کو صحت مند، مضبوط اور ہمیشہ خوش رہنے والا دل عطا فرمائے۔ 🌹<br>
        ہر دن آپ کے لیے نیا آغاز، نئی خوشیاں اور نئے مواقع لے کر آئے۔ 🎊<br>
        مولوی جی، اللہ آپ کو علم کی روشنی، دل کی سکونت اور ہر دعا کی قبولیت دے۔ 🙏<br><br>

        🎶 <b>چھوٹی سی شاعری</b> 🎶<br>
        ہر دن آپ کے چہرے پر مسکان ہو، اور دل میں خوشی کے پھول کھلیں۔ 🌸<br><br>

        <b>🎂 Happy 18th Birthday, Molvi G! 🎂</b><br>
        <b>With lots of love and prayers from your best friend, Pasha ❤️</b>

        </div>
        """, unsafe_allow_html=True)

        # ---------- DISPLAY ALL IMAGES IN ROOT ----------
        image_files = [f for f in os.listdir('.') if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]
        if image_files:
            st.markdown("<h2 style='text-align:center; color:blue;'>📷 Your Pictures 📷</h2>", unsafe_allow_html=True)
            for img in image_files:
                st.image(img, use_column_width=True)
                st.write("----")
        else:
            st.warning("No images found in the repository root.")

        # ---------- DISPLAY ALL VIDEOS IN ROOT ----------
        video_files = [f for f in os.listdir('.') if f.lower().endswith((".mp4", ".mov", ".mkv"))]
        if video_files:
            st.markdown("<h2 style='text-align:center; color:green;'>🎥 Your Videos 🎥</h2>", unsafe_allow_html=True)
            for vid in video_files:
                st.video(vid)
                st.write("----")
        else:
            st.warning("No videos found in the repository root.")
       # ---------------- FINAL MESSAGE ----------------
       st.markdown("""
       <h1 style='text-align:center; color:red; margin-top:40px;'>
       ❤️ MOLVI G, LOVE YOU ❤️
       </h1>
       """, unsafe_allow_html=True)
