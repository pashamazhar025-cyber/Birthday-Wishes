import streamlit as st
import os
import time

# ---------------- APP TITLE ----------------
st.set_page_config(page_title="Birthday App", layout="centered")
st.markdown(
    "<h1 style='text-align:center; color:#ff1493;'>\U0001F389 Welcome Dear \U0001F389</h1>",
    unsafe_allow_html=True
)

# ---------------- ENTER NAME ----------------
name = st.text_input("Enter your name:")

if name:
    # ---------------- COUNTDOWN ----------------
    for i in range(3, 0, -1):
        st.write(f"Starting in {i}…")
        time.sleep(1)
        st.empty()

    # ---------------- BIRTHDAY MESSAGE ----------------
    st.markdown(f"""
<div style='font-size:20px; text-align:center; margin-top:20px;'>

\U0001F389 Today is a very special day — it’s your 18th Birthday, Molvi G! \U0001F389<br><br>

May this year bring you endless happiness, success, and unforgettable memories. \U0001F496<br>
May you always stay strong, cheerful, and full of love for everyone around you. \U0001F31F<br>
May every step you take in life be guided by wisdom and may you achieve all your dreams.<br>
May laughter, joy, and positivity surround you every day. \U0001F388<br>
May you grow in strength, kindness, and courage, and may your heart always remain pure. \u2764\ufe0f<br><br>

<b>Urdu Wishes</b><br>
مولوی جی، آپ کی زندگی خوشیوں سے بھرپور ہو، ہر دن کامیابی اور سکون کے ساتھ آئے۔ \U0001F319<br>
اللہ آپ کی محنت کو کامیابی میں بدل دے، اور آپ کے ہر خواب کو حقیقت میں تبدیل کرے۔ \U0001F4AB<br>
آپ کے دوست اور خاندان ہمیشہ آپ کے ساتھ خوش رہیں، اور ہر لمحہ آپ کے لیے محبت اور خوشی لے کر آئے۔ \u2764\ufe0f<br>
اللہ آپ کو صحت مند، مضبوط اور ہمیشہ خوش رہنے والا دل عطا فرمائے۔ \U0001F339<br>
ہر دن آپ کے لیے نیا آغاز، نئی خوشیاں اور نئے مواقع لے کر آئے۔ \U0001F38A<br>
مولوی جی، اللہ آپ کو علم کی روشنی، دل کی سکونت اور ہر دعا کی قبولیت دے۔ \U0001F64F<br><br>

چھوٹی سی شاعری<br>
ہر دن آپ کے چہرے پر مسکان ہو، اور دل میں خوشی کے پھول کھلیں۔ \U0001F338<br><br>

</div>
""", unsafe_allow_html=True)

    # ---------------- SHOW MEMORIES BUTTON ----------------
    if st.button("Press to See Your Memories"):
        # ---------- DISPLAY ALL IMAGES IN ROOT ----------
        image_files = [f for f in os.listdir('.') if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]
        if image_files:
            st.markdown("<h2 style='text-align:center; color:blue;'>Your Pictures</h2>", unsafe_allow_html=True)
            for img in image_files:
                st.image(img, use_column_width=True)
                st.write("----")
        else:
            st.warning("No images found in the repository root.")

        # ---------- DISPLAY ALL VIDEOS IN ROOT ----------
        video_files = [f for f in os.listdir('.') if f.lower().endswith((".mp4", ".mov", ".mkv"))]
        if video_files:
            st.markdown("<h2 style='text-align:center; color:green;'>Your Videos</h2>", unsafe_allow_html=True)
            for vid in video_files:
                st.video(vid)
                st.write("----")
        else:
            st.warning("No videos found in the repository root.")

        # ---------------- FINAL GREETING MESSAGE ----------------
        st.markdown("""
<h1 style='text-align:center; color:red; margin-top:40px;'>
\U0001F54C Murshid G, Assalam o Alaikum \U0001F54C
</h1>
""", unsafe_allow_html=True)آپ کے دوست اور خاندان ہمیشہ آپ کے ساتھ خوش رہیں، اور ہر لمحہ آپ کے لیے محبت اور خوشی لے کر آئے۔ \u2764\ufe0f<br>
اللہ آپ کو صحت مند، مضبوط اور ہمیشہ خوش رہنے والا دل عطا فرمائے۔ \U0001F339<br>
ہر دن آپ کے لیے نیا آغاز، نئی خوشیاں اور نئے مواقع لے کر آئے۔ \U0001F38A<br>
مولوی جی، اللہ آپ کو علم کی روشنی، دل کی سکونت اور ہر دعا کی قبولیت دے۔ \U0001F64F<br><br>

چھوٹی سی شاعری<br>
ہر دن آپ کے چہرے پر مسکان ہو، اور دل میں خوشی کے پھول کھلیں۔ \U0001F338<br><br>

</div>
""", unsafe_allow_html=True)
         # ---------------- SHOW MEMORIES BUTTON ----------------
    if st.button("Press to See Your Memories"):
        # ---------- DISPLAY ALL IMAGES IN ROOT ----------
        image_files = [f for f in os.listdir('.') if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]
        if image_files:
            st.markdown("<h2 style='text-align:center; color:blue;'>Your Pictures</h2>", unsafe_allow_html=True)
            for img in image_files:
                st.image(img, use_column_width=True)
                st.write("----")
        else:
            st.warning("No images found in the repository root.")

        # ---------- DISPLAY ALL VIDEOS IN ROOT ----------
        video_files = [f for f in os.listdir('.') if f.lower().endswith((".mp4", ".mov", ".mkv"))]
        if video_files:
            st.markdown("<h2 style='text-align:center; color:green;'>Your Videos</h2>", unsafe_allow_html=True)
            for vid in video_files:
                st.video(vid)
                st.write("----")
        else:
            st.warning("No videos found in the repository root.")

        # ---------------- FINAL GREETING MESSAGE ----------------
        st.markdown("""
<h1 style='text-align:center; color:red; margin-top:40px;'>
\U0001F54C Murshid G, Assalam o Alaikum \U0001F54C
</h1>
""", unsafe_allow_html=True)
