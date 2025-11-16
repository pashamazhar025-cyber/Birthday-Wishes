# -*- coding: utf-8 -*-
import streamlit as st
import os
import time

# ---------------- APP CONFIG ----------------
st.set_page_config(page_title="Birthday App", layout="centered")

# ---------------- ENTER NAME ----------------
name = st.text_input("Enter your name:")

if name:
    # ---------------- WELCOME MESSAGE ----------------
    st.markdown(f"""
    <h1 style='text-align:center; color:#FF1493; font-size:60px; font-weight:bold;
               font-family: "Comic Sans MS", cursive, sans-serif; text-shadow: 3px 3px #FFD700;'>
        Welcome, {name}!
    </h1>
    """, unsafe_allow_html=True)
    
    time.sleep(2)  # pause to show welcome

    # ---------------- COUNTDOWN ----------------
    countdown_placeholder = st.empty()
    for i in range(3, 0, -1):
        countdown_placeholder.markdown(f"<h2 style='text-align:center; color:#FF4500;'>Starting in {i}...</h2>", unsafe_allow_html=True)
        time.sleep(1)
    countdown_placeholder.empty()  # remove countdown

    # ---------------- HOME PARTY BACKGROUND ----------------
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1615874959471-7f1950c5f41b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDF8fGJpcnRoZGF5JTIwaG9tZXxlbnwwfHx8fDE2OTk2ODU0MzA&ixlib=rb-4.0.3&q=80&w=1080');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # ---------------- BALLOONS ----------------
    st.balloons()

    # ---------------- HAPPY BIRTHDAY MESSAGE ----------------
    st.markdown(f"""
    <h1 style='text-align:center; color:#FFD700; font-size:60px; font-weight:bold; 
               font-family: "Comic Sans MS", cursive, sans-serif; text-shadow: 2px 2px #FF4500;'>
        Happy Birthday {name}!
    </h1>
    <br>
    """, unsafe_allow_html=True)

    # ---------------- BUTTON TO SHOW WISHES ----------------
    if st.button("🎁 See Your Wishes"):
        st.markdown(f"""
<div style='text-align:center; font-size:20px;'>

\U0001F389 Today is a very special day — it’s your 18th Birthday, Molvi G! \U0001F389<br><br>

May this year bring you endless happiness, success, and unforgettable memories. \U0001F496<br>
May you always stay strong, cheerful, and full of love for everyone around you. \U0001F31F<br>
May every step you take in life be guided by wisdom and may you achieve all your dreams.<br>
May laughter, joy, and positivity surround you every day. \U0001F388<br>
May you grow in strength, kindness, and courage, and may your heart always remain pure. \u2764\ufe0f<br><br>

<b>Urdu Wishes</b><br>
مولوی جی، آپ کی زندگی خوشیوں سے بھرپور ہو، ہر دن کامیابی اور سکون کے ساتھ آئے۔<br>
اللہ آپ کی محنت کو کامیابی میں بدل دے، اور آپ کے ہر خواب کو حقیقت میں تبدیل کرے۔<br>
آپ کے دوست اور خاندان ہمیشہ آپ کے ساتھ خوش رہیں، اور ہر لمحہ آپ کے لیے محبت اور خوشی لے کر آئے۔<br>
اللہ آپ کو صحت مند، مضبوط اور ہمیشہ خوش رہنے والا دل عطا فرمائے۔<br>
ہر دن آپ کے لیے نیا آغاز، نئی خوشیاں اور نئے مواقع لے کر آئے۔<br>
مولوی جی، اللہ آپ کو علم کی روشنی، دل کی سکونت اور ہر دعا کی قبولیت دے۔<br><br>

چھوٹی سی شاعری<br>
ہر دن آپ کے چہرے پر مسکان ہو، اور دل میں خوشی کے پھول کھلیں۔ \U0001F338<br><br>

</div>
""", unsafe_allow_html=True)

    # ---------------- BUTTON TO SHOW MEMORIES ----------------
    if st.button("📸 See Your Memories"):
        # ---------- DISPLAY IMAGES ----------
        image_files = [f for f in os.listdir('.') if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]
        if image_files:
            st.markdown("<h2 style='text-align:center; color:cyan;'>Your Pictures</h2>", unsafe_allow_html=True)
            for img in image_files:
                st.image(img, use_column_width=True)
                st.write("----")
        else:
            st.warning("No images found in the repository root.")

        # ---------- DISPLAY VIDEOS ----------
        video_files = [f for f in os.listdir('.') if f.lower().endswith((".mp4", ".mov", ".mkv"))]
        if video_files:
            st.markdown("<h2 style='text-align:center
