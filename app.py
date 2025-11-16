# -*- coding: utf-8 -*-
import streamlit as st
import os
import time

# ---------------- APP CONFIG ----------------
st.set_page_config(page_title="Birthday App", layout="centered")

# ---------------- WELCOME BEFORE NAME ----------------
st.markdown("""
<div style='text-align:center; margin-top:50px;'>
    <h1 style='font-size:70px; font-weight:bold; color:#FF1493;
               font-family: "Comic Sans MS", cursive, sans-serif;
               text-shadow: 3px 3px #FFD700;'>
        🎉 Welcome to the Birthday App! 🎉
    </h1>
</div>
""", unsafe_allow_html=True)

# ---------------- ENTER NAME ----------------
st.markdown("<br>", unsafe_allow_html=True)
name = st.text_input("Enter your name here:")

if name:
    # ---------------- HAPPY BIRTHDAY MESSAGE ----------------
    st.markdown(f"""
    <div style='text-align:center; margin-top:50px;'>
        <h1 style='font-size:90px; font-weight:bold; color:#FF4500;
                   font-family: "Comic Sans MS", cursive, sans-serif;
                   text-shadow: 4px 4px #FFD700;'>
            Happy Birthday Dear {name}!
        </h1>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- BUTTON TO SHOW WISHES ----------------
    if st.button("🎁 See Your Wishes"):
        st.markdown(f"""
<div style='text-align:center; font-size:20px; margin-top:30px;'>

🎉 Today is a very special day — it’s your 18th Birthday, Molvi G! 🎉<br><br>

May this year bring you endless happiness, success, and unforgettable memories.<br>
May you always stay strong, cheerful, and full of love for everyone around you.<br>
May every step you take in life be guided by wisdom and may you achieve all your dreams.<br>
May laughter, joy, and positivity surround you every day.<br>
May you grow in strength, kindness, and courage, and may your heart always remain pure.<br><br>

<b>Urdu Wishes</b><br>
مولوی جی، آپ کی زندگی خوشیوں سے بھرپور ہو، ہر دن کامیابی اور سکون کے ساتھ آئے۔<br>
اللہ آپ کی محنت کو کامیابی میں بدل دے، اور آپ کے ہر خواب کو حقیقت میں تبدیل کرے۔<br>
آپ کے دوست اور خاندان ہمیشہ آپ کے ساتھ خوش رہیں، اور ہر لمحہ آپ کے لیے محبت اور خوشی لے کر آئے۔<br>
اللہ آپ کو صحت مند، مضبوط اور ہمیشہ خوش رہنے والا دل عطا فرمائے۔<br>
ہر دن آپ کے لیے نیا آغاز، نئی خوشیاں اور نئے مواقع لے کر آئے۔<br>
مولوی جی، اللہ آپ کو علم کی روشنی، دل کی سکونت اور ہر دعا کی قبولیت دے۔<br><br>

چھوٹی سی شاعری<br>
ہر دن آپ کے چہرے پر مسکان ہو، اور دل میں خوشی کے پھول کھلیں۔<br><br>

</div>
""", unsafe_allow_html=True)

    # ---------------- BUTTON TO SHOW MEMORIES ----------------
    if st.button("📸 See Your Memories"):
        # ---------- DISPLAY IMAGES ----------
        image_files = [f for f in os.listdir('.') if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]
        if image_files:
            st.markdown("<h2 style='text-align:center; color:blue;'>Your Pictures</h2>", unsafe_allow_html=True)
            for img in image_files:
                st.image(img, use_column_width=True)
                st.write("----")
        else:
            st.warning("No images found in the repository root.")

        # ---------- DISPLAY VIDEOS ----------
        video_files = [f for f in os.listdir('.') if f.lower().endswith((".mp4", ".mov", ".mkv"))]
        if video_files:
            st.markdown("<h2 style='text-align:center; color:green;'>Your Videos</h2>", unsafe_allow_html=True)
            for vid in video_files:
                st.video(vid)
                st.write("----")
        else:
            st.warning("No videos found in the repository root.")

        # ---------------- FINAL GREETING ----------------
        st.markdown("""
<h1 style='text-align:center; color:red; margin-top:40px;'>
 Allah Hafiz 
</h1>
""", unsafe_allow_html=True)
