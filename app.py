# import streamlit as st
# import base64
# import pandas as pd
# from datetime import datetime

# # ==== Set page config ====
# st.set_page_config(page_title="💘 Friendship Predictor 🔮", layout="centered")


# # ==== Background Image ====
# def add_bg(image_file):
#     with open(image_file, "rb") as img:
#         b64_img = base64.b64encode(img.read()).decode()
#         st.markdown(f"""
#             <style>
#             .stApp {{
#                 background-image: url("data:image/png;base64,{b64_img}");
#                 background-size: cover;
#                 background-position: center;
#                 background-repeat: no-repeat;
#             }}
#             </style>
#         """, unsafe_allow_html=True)

# # Optional: add_bg("bg.png")

# st.title("💘 Friendship Predictor 🔮 ")
# st.markdown("### 🤖 Dekhein kya dosti banegi ya sirf 'seen' hi rahega?")

# # ==== Layout ====
# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("🧍‍♂️ Tumhari Info")
#     user = {
#         "name": st.text_input("Naam", key="user_name"),
#         "age": st.slider("Age", 10, 30, 18, key="user_age"),
#         "city": st.text_input("Sheher", key="user_city"),
#         "status": st.selectbox("Status", ["single", "relationship", "confused"], key="user_status"),
#         "nature": st.select_slider("Nature", options=["funny", "serious", "rude", "romantic", "caring"], key="user_nature"),
#         "communication": st.selectbox("Communication Style", ["talkative", "shy", "normal"], key="user_comm"),
#         "hobbies": st.multiselect("Hobbies", ["gaming", "music", "drawing", "coding", "poetry", "funny videos", "travel"], key="user_hobbies"),
#         "mbti": st.selectbox("MBTI Type (Optional)", ["", "INTJ", "INFP", "ENFP", "ESTJ", "ISFJ"], key="user_mbti"),
#     }

# with col2:
#     st.subheader("👧 Uski Info")
#     girl = {
#         "name": st.text_input("Naam", key="girl_name"),
#         "age": st.slider("Uski Age", 10, 30, 18, key="girl_age"),
#         "city": st.text_input("Sheher", key="girl_city"),
#         "status": st.selectbox("Uska Status", ["single", "relationship", "complicated"], key="girl_status"),
#         "nature": st.select_slider("Nature", options=["funny", "serious", "rude", "romantic", "caring"], key="girl_nature"),
#         "response": st.selectbox("Reply Style", ["quick", "late", "seen only"], key="girl_response"),
#         "looking": st.selectbox("Wo kya dhoond rahi hai?", ["fun", "serious", "study partner", "nothing"], key="girl_looking"),
#         "hobbies": st.multiselect("Hobbies", ["gaming", "music", "drawing", "coding", "poetry", "funny videos", "travel"], key="girl_hobbies"),
#         "mbti": st.selectbox("MBTI Type (Optional)", ["", "INTJ", "INFP", "ENFP", "ESTJ", "ISFJ"], key="girl_mbti"),
#     }

# # ==== Prediction Logic ====
# def predict_friendship(user, girl):
#     score = 0
#     reasons = []

#     if abs(user["age"] - girl["age"]) <= 2:
#         score += 20
#         reasons.append("✅ Age difference perfect!")

#     if user["city"].strip().lower() == girl["city"].strip().lower():
#         score += 15
#         reasons.append("✅ Same city — easy meetup!")

#     if user["status"] == "single" and girl["status"] == "single":
#         score += 20
#         reasons.append("✅ Dono hi single — ready to mingle!")

#     if user["nature"] == girl["nature"]:
#         score += 10
#         reasons.append("✅ Matching natures!")
#     elif (user["nature"], girl["nature"]) in [("funny", "serious"), ("serious", "funny")]:
#         score += 5
#         reasons.append("✅ Opposites attract!")

#     if girl["looking"] == "fun" and user["nature"] == "funny":
#         score += 10
#         reasons.append("✅ Tum ho full-time entertainer!")

#     if girl["response"] == "quick" and user["communication"] == "talkative":
#         score += 10
#         reasons.append("✅ She’ll respond fast to your energy!")

#     common_hobbies = set(user["hobbies"]) & set(girl["hobbies"])
#     if common_hobbies:
#         score += len(common_hobbies) * 4
#         reasons.append(f"✅ Common hobbies: {', '.join(common_hobbies)}")

#     # MBTI logic (just for fun)
#     if user["mbti"] and girl["mbti"] and user["mbti"][:2] == girl["mbti"][:2]:
#         score += 5
#         reasons.append("✅ Compatible personalities (MBTI)!")

#     return min(score, 100), reasons

# # ==== Predict Button ====
# if st.button("💌 Predict Friendship Now!"):
#     score, reasons = predict_friendship(user, girl)

#     st.subheader("📊 Friendship Score")
#     st.write(f"### ❤️ **{score} / 100**")
#     st.progress(score)

#     if score >= 80:
#         st.success("🌟 Strong chance! Try sending a meme or voice note!")
#     elif score >= 60:
#         st.warning("⚡ Okay chance — try a light chat.")
#     else:
#         st.error("💔 Weak connection — friendship might not go far.")

#     st.markdown("### 🔍 Why This Score?")
#     for r in reasons:
#         st.write(r)

#     st.markdown("### 📝 Match Summary")
#     st.info(f"{user['name']} ({user['nature']}) & {girl['name']} ({girl['nature']}) — Compatibility score: **{score}%**")

#     # Save to CSV (optional)
#     result = {
#         "user_name": user["name"],
#         "girl_name": girl["name"],
#         "score": score,
#         "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }
#     df = pd.DataFrame([result])
#     df.to_csv("friendship_results.csv", mode='a', header=False, index=False)

#     st.markdown("---")
#     st.caption("🔐 Your data is not stored online — local only.")

# # ==== Reset Button ====
# if st.button("🔁 Reset"):
#     st.experimental_rerun()
# import streamlit as st
# import base64
# import pandas as pd
# from datetime import datetime

# # ==== Set page config ====
# st.set_page_config(page_title="💞 Connection Predictor", layout="centered")

# # ==== Background Image with romantic soft feel ====
# def add_bg(image_file):
#     with open(image_file, "rb") as img:
#         b64_img = base64.b64encode(img.read()).decode()
#         st.markdown(f"""
#             <style>
#             .stApp {{
#                 background-image: url("data:image/png;base64,{b64_img}");
#                 background-size: cover;
#                 background-position: center;
#                 background-repeat: no-repeat;
#             }}
#             </style>
#         """, unsafe_allow_html=True)

# # Optional: add_bg("light_love_bg.png")  # Add a light soft-pink love background

# st.title("💞 Connection Predictor")
# st.markdown("### 🌟 Jaanein kya aap dono ke beech ek achi dosti, ya kuch aur ban sakta hai?")

# # ==== Input: First Person Info ====
# st.header("🧑 Aapki Maloomat")

# you = {
#     "name": st.text_input("Aapka Naam"),
#     "gender": st.selectbox("Aap ka jins kya hai?", ["Male", "Female", "Other"]),
#     "age": st.slider("Aapki Umar", 10, 40, 18),
#     "city": st.text_input("Sheher ka Naam"),
#     "address": st.text_input("Sheher ka Mukammal Address"),
#     "relationship_duration": st.text_input("Kya pehle kisi rishte mein thay? Kitne waqt tak?"),
#     "status": st.selectbox("Aapka Halat-e-Zindagi (Status)", ["Akele (Single)", "Rishtay mein (Committed)", "Samajh nahi aata"]),
#     "nature": st.selectbox("Aapka Mizaj (Nature)", ["Hansmukh", "Sanjeeda", "Romantic", "Narma mizaj", "Thoda rude"]),
#     "communication": st.selectbox("Aap baat cheet mein kaisay hain?", ["Zyada bolne wale", "Kam bolne wale", "Miyan mein"]),
#     "hobbies": st.multiselect("Aapko kya pasand hai?", ["Music", "Coding", "Drawing", "Poetry", "Funny Videos", "Gaming", "Travel"]),
# }

# # ==== Input: Second Person Info ====
# st.header("🧑‍🤝‍🧑 Doosri Shakhsiyat ki Maloomat")

# them = {
#     "name": st.text_input("Unka Naam", key="them_name"),
#     "gender": st.selectbox("Unka jins kya hai?", ["Male", "Female", "Other"], key="them_gender"),
#     "age": st.slider("Unki Umar", 10, 40, 18, key="them_age"),
#     "city": st.text_input("Unka Sheher", key="them_city"),
#     "address": st.text_input("Unka Mukammal Address", key="them_address"),
#     "relationship_duration": st.text_input("Kya unka koi purana rishta tha? Kab aur kitna chala?", key="them_relation"),
#     "status": st.selectbox("Unka Halat-e-Zindagi", ["Akele (Single)", "Rishtay mein (Committed)", "Mushkil mein (Confused)"] , key="them_status"),
#     "nature": st.selectbox("Unka Mizaj (Nature)", ["Hansmukh", "Sanjeeda", "Romantic", "Narma mizaj", "Thoda rude"], key="them_nature"),
#     "response": st.selectbox("Unka jawab denay ka style?", ["Jaldi jawab detay hain", "Thoda late", "Sirf dekhtay hain"], key="them_response"),
#     "looking": st.selectbox("Wo zindagi mein kya dhoond rahay hain?", ["Sirf dosti", "Gehri baat cheet", "Study partner", "Kuch nahi"], key="them_looking"),
#     "hobbies": st.multiselect("Unki pasandida cheezein?", ["Music", "Coding", "Drawing", "Poetry", "Funny Videos", "Gaming", "Travel"], key="them_hobbies"),
# }

# # ==== Matching Logic ====
# def predict_connection(you, them):
#     score = 0
#     advice = []

#     if abs(you['age'] - them['age']) <= 2:
#         score += 20
#         advice.append("Umar ka farq kam hai — baat ban sakti hai.")

#     if you['city'].strip().lower() == them['city'].strip().lower():
#         score += 15
#         advice.append("Dono ka sheher ek hai — milne ka asaan moqa.")

#     if "Akele" in you['status'] and "Akele" in them['status']:
#         score += 20
#         advice.append("Dono akele hain — naye rishtay ki gunjaish hai.")

#     if you['nature'] == them['nature']:
#         score += 10
#         advice.append("Dono ka mizaj milta julta hai.")
#     else:
#         score += 5
#         advice.append("Agar mizaj alag hain to bhi balance ho sakta hai.")

#     common_hobbies = set(you['hobbies']) & set(them['hobbies'])
#     if common_hobbies:
#         score += len(common_hobbies) * 4
#         advice.append(f"Common shauq: {', '.join(common_hobbies)}")

#     if them['response'] == "Jaldi jawab detay hain" and you['communication'] == "Zyada bolne wale":
#         score += 10
#         advice.append("Aap bolenge aur wo sunenge — achi pairing.")

#     if them['looking'] in ["Sirf dosti", "Gehri baat cheet"]:
#         score += 10
#         advice.append("Wo bhi kisi connection ke liye tayyar lagte hain.")

#     return min(score, 100), advice

# # ==== Predict Button ====
# if st.button("💌 Ab Check Karen"):
#     score, advice = predict_connection(you, them)
#     st.subheader("📊 Nateeja")
#     st.write(f"### 💖 Compatibility Score: **{score} / 100**")
#     st.progress(score)

#     if score >= 80:
#         st.success("🎉 Bohat achi baat hai! Shuruat ek ache msg se karein ya koi choti gift de kar rasta saaf karein.")
#         st.image("happy.png", width=200)
#     elif score >= 50:
#         st.warning("😊 Chance hai... lekin pehle halka halka baat cheet karein, samajhne ki koshish karein.")
#         st.image("neutral.png", width=200)
#     else:
#         st.error("😔 Filhal to mushkil lagta hai... lekin ek ache dost ki tarah aage barhna behtar hoga.")
#         st.image("sad.png", width=200)

#     st.markdown("---")
#     st.markdown("### 🔍 Tafseelat:")
#     for a in advice:
#         st.write("- ", a)

#     # Optional: Save
#     result = {
#         "your_name": you['name'],
#         "their_name": them['name'],
#         "score": score,
#         "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }
#     df = pd.DataFrame([result])
#     df.to_csv("connection_results.csv", mode='a', header=False, index=False)

#     st.caption("📌 Yeh data sirf aapke local system par save hota hai.")
# import streamlit as st
# import base64
# Sulemanfaraz
# # ---- Set page config ----
# st.set_page_config(page_title="HeartMatch AI 💖", layout="centered")

# # ---- Background image ----
# def add_bg(image_file):
#     with open(image_file, "rb") as img:
#         b64_img = base64.b64encode(img.read()).decode()
#         bg_style = f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/png;base64,{b64_img}");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-position: center;
#         }}
#         </style>
#         """
#         st.markdown(bg_style, unsafe_allow_html=True)

# # Set background (optional - add your background file to same folder)
# # add_bg("bg.png")

# # ---- App Title ----
# st.markdown("<h1 style='text-align: center;'>💖 HeartMatch AI</h1>", unsafe_allow_html=True)
# st.markdown("<h4 style='text-align: center;'>Friendship & Vibes Compatibility Predictor 🔮</h4>", unsafe_allow_html=True)
# st.markdown("##### Let's see if there's a vibe... or just 'seen'. 👀")

# # ---- Your Info ----
# st.header("🧍‍♂️ Your Details")
# user = {
#     "name": st.text_input("Your Name"),
#     "age": st.slider("Your Age", 10, 30, 20),
#     "city": st.text_input("Your City"),
#     "status": st.selectbox("Relationship Status", ["Single", "Taken", "Confused"]),
#     "nature": st.select_slider("Your Nature", ["Funny", "Serious", "Romantic", "Caring", "Rude"]),
#     "communication": st.selectbox("Communication Style", ["Talkative", "Shy", "Balanced"]),
#     "hobbies": st.multiselect("Your Hobbies", ["Gaming", "Music", "Art", "Coding", "Poetry", "Travel", "Funny Videos"]),
#     "mbti": st.text_input("MBTI Personality Type (optional)", help="Like INFJ, ENTP etc. Take free test at 16personalities.com"),
#     "openness": st.slider("How open are you emotionally?", 0, 10, 5),
#     "love_language": st.selectbox("Your Love Language", ["Words", "Time", "Gifts", "Touch", "Support"])
# }

# # ---- Girl Info ----
# st.header("👧 Their Details")
# girl = {
#     "name": st.text_input("Their Name"),
#     "age": st.slider("Their Age", 10, 30, 20),
#     "city": st.text_input("Their City"),
#     "status": st.selectbox("Their Relationship Status", ["Single", "Taken", "Complicated"]),
#     "nature": st.select_slider("Their Nature", ["Funny", "Serious", "Romantic", "Caring", "Rude"]),
#     "response": st.selectbox("How they usually reply?", ["Quick", "Late", "Seen only"]),
#     "looking": st.selectbox("What are they looking for?", ["Fun", "Friendship", "Support", "Nothing"]),
#     "hobbies": st.multiselect("Their Hobbies", ["Gaming", "Music", "Art", "Coding", "Poetry", "Travel", "Funny Videos"]),
#     "openness": st.slider("How open do you think they are emotionally?", 0, 10, 5),
#     "love_language": st.selectbox("Their Love Language", ["Words", "Time", "Gifts", "Touch", "Support"])
# }

# # ---- Prediction Logic ----
# def predict_friendship(user, girl):
#     score = 0
#     reasons = []

#     if abs(user["age"] - girl["age"]) <= 2:
#         score += 15
#         reasons.append("✅ Close in age, that's a good start!")

#     if user["city"].strip().lower() == girl["city"].strip().lower():
#         score += 10
#         reasons.append("✅ You live in the same city — easy to meet!")

#     if user["status"] == "Single" and girl["status"] == "Single":
#         score += 15
#         reasons.append("✅ Both are single — green signal! 💚")

#     if user["nature"] == girl["nature"]:
#         score += 10
#         reasons.append("✅ Matching personalities! Easy bonding.")
#     elif (user["nature"], girl["nature"]) in [("Funny", "Serious"), ("Serious", "Funny")]:
#         score += 7
#         reasons.append("✅ Opposites attract! Interesting vibe.")

#     if girl["looking"] == "Fun" and user["nature"] == "Funny":
#         score += 10
#         reasons.append("✅ They're looking for fun, and you're the fun one!")

#     if girl["response"] == "Quick" and user["communication"] == "Talkative":
#         score += 7
#         reasons.append("✅ You love talking, and they reply quickly!")

#     shared = set(user["hobbies"]) & set(girl["hobbies"])
#     if shared:
#         score += len(shared) * 3
#         reasons.append(f"✅ Shared hobbies: {', '.join(shared)}")

#     openness_diff = abs(user["openness"] - girl["openness"])
#     if openness_diff <= 2:
#         score += 8
#         reasons.append("✅ Emotionally on the same level!")

#     if user["love_language"] == girl["love_language"]:
#         score += 10
#         reasons.append("✅ Same love language! That’s deep 💞")

#     return score, reasons

# # ---- Predict Button ----
# if st.button("💌 Predict Now"):
#     score, reasons = predict_friendship(user, girl)

#     st.subheader("📊 Your Result")
#     st.markdown(f"### ❤️ Friendship Score: **{score} / 100**")

#     if score >= 75:
#         st.success("💖 Strong vibes! Looks like a great match for friendship and maybe more.")
#     elif score >= 50:
#         st.warning("💛 Average match. Try starting with light conversation and see where it goes.")
#     else:
#         st.error("💔 Low chance, but hey — every friendship starts with hello!")

#     st.markdown("### 🔍 Why This Score?")
#     for r in reasons:
#         st.write(r)

#     st.markdown("### 🌈 What You Can Do:")
#     if score >= 75:
#         st.write("Send a fun meme or ask her favorite song — let the spark begin! 🌟")
#     elif score >= 50:
#         st.write("Be kind, consistent, and funny. Let trust build naturally. 🕊️")
#     else:
#         st.write("It may not match well now — but friendship isn’t about scores. Be genuine. 🌻")
# # import streamlit as st
# # from PIL import Image
# # import random

# # st.set_page_config(page_title="HeartMatch AI ❤️", page_icon="💖", layout="centered")
# # st.markdown("""
# #     <style>
# #     body {
# #         background-color: #fff0f5;
# #     }
# #     .main {
# #         background-color: #ffe4e1;
# #         border-radius: 12px;
# #         padding: 20px;
# #         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
# #     }
# #     </style>
# # """, unsafe_allow_html=True)

# # st.title("💖 HeartMatch AI - Friendship & Compatibility Profiler")
# # st.subheader("Discover emotional & personality alignment based on deep psychology 🔍")
# # st.markdown("---")

# # st.markdown("### 📸 Upload Your Picture (Optional)")
# # pic = st.file_uploader("This helps personalize your result, not used for prediction.", type=["jpg", "jpeg", "png"])

# # if pic:
# #     image = Image.open(pic)
# #     st.image(image, width=150, caption="Your Uploaded Picture")

# # st.markdown("---")
# # st.markdown("## 👤 Your Identity")
# # name = st.text_input("Your Name")
# # gender = st.selectbox("Gender", ["Male", "Female", "Other"])
# # age = st.slider("Your Age", 16, 60, 25)
# # city = st.text_input("City")
# # edu = st.selectbox("Education Level", ["Matric", "Intermediate", "Bachelor", "Master", "PhD"])
# # financial = st.selectbox("Financial Status", ["Low", "Middle", "Stable", "Wealthy"])

# # st.markdown("---")
# # st.markdown("## 🧠 Personality & Emotional Behavior")

# # stress_response = st.selectbox("How do you usually respond to stress?", [
# #     "Stay calm and look for solutions",
# #     "Get emotional or cry",
# #     "Shut down or isolate",
# #     "Become angry or irritable"
# # ])

# # emotion_openness = st.selectbox("How emotionally open are you with close people?", [
# #     "Very open",
# #     "Somewhat open",
# #     "Only when necessary",
# #     "I keep things to myself"
# # ])

# # conflict_style = st.selectbox("In conflict, you tend to:", [
# #     "Talk it out calmly",
# #     "Avoid confrontation",
# #     "Get aggressive",
# #     "Shut down silently"
# # ])

# # attachment = st.selectbox("When someone gets emotionally close:", [
# #     "I feel safe",
# #     "I get anxious about losing them",
# #     "I push them away",
# #     "I get too attached too fast"
# # ])

# # trust_openness = st.selectbox("Do you open up easily to others?", [
# #     "Yes, very easily",
# #     "Takes me time",
# #     "Only to few",
# #     "Not really"
# # ])

# # love_language = st.multiselect("What makes you feel emotionally close?", [
# #     "Time together",
# #     "Deep conversations",
# #     "Support in hard times",
# #     "Physical closeness",
# #     "Small acts of care"
# # ])

# # st.markdown("---")
# # st.markdown("## 🧩 Core Values")
# # values = st.multiselect("What do you value most in a bond?", [
# #     "Loyalty", "Respect", "Growth", "Fun", "Trust", "Peace", "Adventure", "Understanding"
# # ])

# # st.markdown("---")
# # st.markdown("## 🔮 Optional: MBTI Personality Type")
# # mbti = st.text_input("If known, write your MBTI (like INFJ, ENFP, ISTP etc.)")
# # st.caption("MBTI is a popular personality typing model used in psychology to understand core behavior.")

# # if st.button("🔍 Predict My Friendship Compatibility"):
# #     st.markdown("---")
# #     st.subheader(f"✨ {name}, Here’s Your Deep Friendship Compatibility Report")

# #     score = random.randint(65, 98)  # placeholder logic — can be replaced with real ML

# #     st.metric("Compatibility Score", f"{score}%")

# #     st.markdown("### ✅ Personality Insights:")
# #     st.write("- You handle stress by: ", stress_response)
# #     st.write("- Emotional openness: ", emotion_openness)
# #     st.write("- In conflicts, you usually: ", conflict_style)
# #     st.write("- Trust style: ", trust_openness)
# #     st.write("- Attachment pattern: ", attachment)

# #     st.markdown("### ❤️ Love Language & Core Values:")
# #     st.write("- Love languages: ", ", ".join(love_language))
# #     st.write("- Core values: ", ", ".join(values))

# #     st.markdown("---")
# #     st.markdown("### 🧠 Final Analysis:")
# #     st.success("You show a balanced emotional depth and loyalty, indicating strong potential for deep, lasting bonds.")
# #     st.info("Focus on people who match your trust and communication level — your heart is deep, so protect it wisely 💖")

# #     if score > 85:
# #         st.balloons()
# #         st.success("This is a soulmate-level match zone! You have what it takes to build something rare and beautiful.")
# #     elif score > 75:
# #         st.warning("You have emotional potential — just maintain understanding in tough moments.")
# #     else:
# #         st.error("You may need someone more emotionally aligned with you. Trust your intuition — and keep shining 🌟")

# # st.markdown("""
# # ---
# # <p style='text-align: center;'>Made with ❤️ by HeartMatch AI - Where Emotions Matter Most</p>
# # # """, unsafe_allow_html=True)
# # import streamlit as st
# # from PIL import Image
# # import base64

# # st.set_page_config(page_title="HeartMatch AI ❤️‍🔥", page_icon="❤️", layout="centered")

# # # Custom background style
# # page_bg = f"""
# # <style>
# # [data-testid="stAppViewContainer"] > .main {{
# #     background-color: #ffe6e6;
# #     background-image: linear-gradient(to right, #ffcccc, #ffe6e6);
# # }}
# # [data-testid="stHeader"] {{
# #     background-color: rgba(0,0,0,0);
# # }}
# # </style>
# # """
# # st.markdown(page_bg, unsafe_allow_html=True)

# # st.title("❤️ HeartMatch AI - Find Your Friendship Vibe")
# # st.markdown("Welcome! Answer a few deep & romantic questions to find how well your vibe matches your partner. ✨")

# # # Upload photo (optional)
# # photo = st.file_uploader("Upload your photo (optional):", type=["jpg", "jpeg", "png"])
# # if photo:
# #     st.image(photo, width=200)

# # st.subheader("🧍 Your Info")
# # your_name = st.text_input("Your Name")
# # your_gender = st.selectbox("Your Gender", ["Male", "Female", "Other"])
# # your_age = st.number_input("Your Age", min_value=12, max_value=100)
# # your_education = st.selectbox("Your Education", ["Matric", "Intermediate", "Graduate", "Post-Graduate", "Other"])
# # your_financial = st.selectbox("Your Financial Status", ["Low", "Medium", "Stable", "Wealthy"])

# # st.subheader("👩 Partner Info")
# # partner_name = st.text_input("Partner's Name")
# # partner_gender = st.selectbox("Partner's Gender", ["Male", "Female", "Other"])
# # partner_age = st.number_input("Partner's Age", min_value=12, max_value=100)
# # partner_education = st.selectbox("Partner's Education", ["Matric", "Intermediate", "Graduate", "Post-Graduate", "Other"])
# # partner_financial = st.selectbox("Partner's Financial Status", ["Low", "Medium", "Stable", "Wealthy"])

# # st.subheader("🧠 Your Personality")
# # deeper_1 = st.selectbox("How do you usually handle problems?", ["Calmly", "Get emotional", "Get angry", "Ignore it"])
# # deeper_2 = st.selectbox("What do you value most in people?", ["Loyalty", "Fun", "Deep conversations", "Kindness"])
# # deeper_3 = st.selectbox("How much do you trust new people?", ["Quickly trust", "Trust slowly", "Very cautious", "Don't trust easily"])
# # deeper_4 = st.selectbox("How do you show care for someone?", ["Spend time", "Give gifts", "Say kind words", "Physical affection", "Help them"])
# # deeper_5 = st.selectbox("Do you like deep talks or fun talks more?", ["Deep talks", "Fun talks", "Both equally"])

# # st.subheader("❤️ What do you feel about your partner?")
# # partner_behavior = st.selectbox("How do they handle problems?", ["Calmly", "Get emotional", "Get angry", "Ignore it"])
# # partner_value = st.selectbox("What do you think they value in a person?", ["Loyalty", "Fun", "Deep conversations", "Kindness"])
# # partner_trust = st.selectbox("How do they trust others?", ["Quickly trust", "Trust slowly", "Very cautious", "Don't trust easily"])
# # partner_care = st.selectbox("How do they show care?", ["Spend time", "Give gifts", "Say kind words", "Physical affection", "Help them"])
# # partner_talk = st.selectbox("What kind of talks they enjoy more?", ["Deep talks", "Fun talks", "Both equally"])

# # mbti = st.text_input("MBTI Type (Optional) - e.g. INFJ, ENTP")

# # if st.button("💘 Predict Friendship Score"):
# #     score = 0

# #     if deeper_1 == partner_behavior:
# #         score += 20
# #     if deeper_2 == partner_value:
# #         score += 20
# #     if deeper_3 == partner_trust:
# #         score += 15
# #     if deeper_4 == partner_care:
# #         score += 20
# #     if deeper_5 == partner_talk:
# #         score += 15

# #     if your_financial == partner_financial:
# #         score += 5
# #     if your_education == partner_education:
# #         score += 5

# #     final_msg = ""
# #     if score >= 80:
# #         final_msg = "🌟 You two have a beautiful connection! You both think, feel, and express care in a similar way. This makes your bond naturally strong. Keep being open and kind to each other."
# #     elif score >= 60:
# #         final_msg = "💖 You have a good emotional match! Some differences are there, but your intentions are in sync. Try to understand each other more deeply, and your bond can grow strong."
# #     elif score >= 40:
# #         final_msg = "🌀 There's some mismatch in your emotional styles. But if you both are willing to adjust and understand, it can still work out. Take your time to know each other."
# #     else:
# #         final_msg = "💔 Your emotional and personality styles are quite different. It's not impossible, but it may take more effort to understand each other deeply. Communication is key."

# #     st.subheader(f"🔮 Your Compatibility Score: {score}%")
# #     st.markdown(final_msg)

# #     if score >= 60:
# #         st.image("https://i.pinimg.com/originals/d7/04/75/d7047551e53988c3b65f6d2cc7707f36.gif", width=250)
# #     else:
# #         st.image("https://media.tenor.com/JWQOvnl-9xEAAAAd/anime-heartbreak.gif", width=250)

# #     st.markdown("---")
# #     st.caption("This result is based on emotional behavior and values. It's a friendly prediction, not a guarantee. Real friendship grows with understanding 💕")
# # import streamlit as st
# # from PIL import Image
# # import base64

# # st.set_page_config(page_title="HeartMatch AI ❤️‍🔥", page_icon="❤️", layout="centered")

# # # Custom background style
# # page_bg = f"""
# # <style>
# # [data-testid="stAppViewContainer"] > .main {{
# #     background-color: #ffe6e6;
# #     background-image: linear-gradient(to right, #ff4d4d, #ffe6e6);
# # }}
# # [data-testid="stHeader"] {{
# #     background-color: rgba(0,0,0,0);
# # }}
# # </style>
# # """
# # st.markdown(page_bg, unsafe_allow_html=True)

# # st.title("❤️ HeartMatch AI - Find Your Friendship Vibe")
# # st.markdown("Welcome! Answer a few deep & romantic questions to find how well your vibe matches your partner. ✨")

# # # Upload photo (optional)
# # photo = st.file_uploader("Upload your photo (optional):", type=["jpg", "jpeg", "png"])
# # if photo:
# #     st.image(photo, width=200)

# # st.subheader("🧍 Your Info")
# # your_name = st.text_input("Your Name")
# # your_gender = st.selectbox("Your Gender", ["Male", "Female", "Other"])
# # your_age = st.number_input("Your Age", min_value=12, max_value=100)
# # your_education = st.selectbox("Your Education", ["Matric", "Intermediate", "Graduate", "Post-Graduate", "Other"])
# # your_financial = st.selectbox("Your Financial Status", ["Low", "Medium", "Stable", "Wealthy"])
# # your_lifestyle = st.selectbox("Your Lifestyle Type", ["Simple", "Balanced", "Modern", "Luxury"])
# # your_love_language = st.selectbox("Your Love Language", ["Words", "Gifts", "Time", "Touch", "Acts of service"])
# # your_communication = st.selectbox("How do you usually communicate feelings?", ["Clearly", "Hide them", "Through actions", "Through humor"])

# # talk_openness = st.selectbox("Are you open to romantic discussions?", ["Yes", "Sometimes", "Rarely", "No"])
# # future_goals = st.selectbox("Do you believe in long-term commitment?", ["Yes", "Not sure", "No"])

# # st.subheader("👩 Partner Info")
# # partner_name = st.text_input("Partner's Name")
# # partner_gender = st.selectbox("Partner's Gender", ["Male", "Female", "Other"])
# # partner_age = st.number_input("Partner's Age", min_value=12, max_value=100)
# # partner_education = st.selectbox("Partner's Education", ["Matric", "Intermediate", "Graduate", "Post-Graduate", "Other"])
# # partner_financial = st.selectbox("Partner's Financial Status", ["Low", "Medium", "Stable", "Wealthy"])
# # partner_lifestyle = st.selectbox("Partner's Lifestyle Type", ["Simple", "Balanced", "Modern", "Luxury"])
# # partner_love_language = st.selectbox("Partner's Love Language", ["Words", "Gifts", "Time", "Touch", "Acts of service"])
# # partner_communication = st.selectbox("How does your partner communicate feelings?", ["Clearly", "Hide them", "Through actions", "Through humor"])

# # st.subheader("🧠 Your Personality")
# # deeper_1 = st.selectbox("How do you usually handle problems?", ["Calmly", "Get emotional", "Get angry", "Ignore it"])
# # deeper_2 = st.selectbox("What do you value most in people?", ["Loyalty", "Fun", "Deep conversations", "Kindness"])
# # deeper_3 = st.selectbox("How much do you trust new people?", ["Quickly trust", "Trust slowly", "Very cautious", "Don't trust easily"])
# # deeper_4 = st.selectbox("How do you show care for someone?", ["Spend time", "Give gifts", "Say kind words", "Physical affection", "Help them"])
# # deeper_5 = st.selectbox("Do you like deep talks or fun talks more?", ["Deep talks", "Fun talks", "Both equally"])

# # st.subheader("❤️ What do you feel about your partner?")
# # partner_behavior = st.selectbox("How do they handle problems?", ["Calmly", "Get emotional", "Get angry", "Ignore it"])
# # partner_value = st.selectbox("What do you think they value in a person?", ["Loyalty", "Fun", "Deep conversations", "Kindness"])
# # partner_trust = st.selectbox("How do they trust others?", ["Quickly trust", "Trust slowly", "Very cautious", "Don't trust easily"])
# # partner_care = st.selectbox("How do they show care?", ["Spend time", "Give gifts", "Say kind words", "Physical affection", "Help them"])
# # partner_talk = st.selectbox("What kind of talks they enjoy more?", ["Deep talks", "Fun talks", "Both equally"])

# # mbti = st.text_input("MBTI Type (Optional) - e.g. INFJ, ENTP")

# # if st.button("💘 Predict Friendship Score"):
# #     score = 0

# #     if deeper_1 == partner_behavior:
# #         score += 20
# #     if deeper_2 == partner_value:
# #         score += 20
# #     if deeper_3 == partner_trust:
# #         score += 15
# #     if deeper_4 == partner_care:
# #         score += 20
# #     if deeper_5 == partner_talk:
# #         score += 15

# #     if your_financial == partner_financial:
# #         score += 5
# #     if your_education == partner_education:
# #         score += 5
# #     if your_lifestyle == partner_lifestyle:
# #         score += 5
# #     if your_love_language == partner_love_language:
# #         score += 5
# #     if your_communication == partner_communication:
# #         score += 5

# #     final_msg = ""
# #     if score >= 85:
# #         final_msg = "💞 You both think, feel, and show love in such similar ways. It's a magical match — like soulmates! You should cherish and support each other always."
# #     elif score >= 65:
# #         final_msg = "💖 You have strong emotional chemistry! You connect on many levels. A little more time and openness will make your bond even stronger."
# #     elif score >= 45:
# #         final_msg = "🌙 There's a good base here, but some differences too. Try to understand each other more. Real love grows when both sides try."
# #     else:
# #         final_msg = "💔 You both may see love and emotions differently. It's not impossible, but building deep connection may take effort, patience, and honest talks."

# #     st.subheader(f"🔮 Your Compatibility Score: {score}%")
# #     st.markdown(final_msg)

# #     if score >= 60:
# #         st.image("https://i.pinimg.com/originals/d7/04/75/d7047551e53988c3b65f6d2cc7707f36.gif", width=250)
# #     else:
# #         st.image("https://media.tenor.com/JWQOvnl-9xEAAAAd/anime-heartbreak.gif", width=250)

# #     st.markdown("---")
# #     st.caption("This result is based on how well your emotional responses and values match. It's not a prediction of fate, but a fun and thoughtful way to understand your bond better. ❤️")
# # import streamlit as st
# # from PIL import Image

# # st.set_page_config(page_title="HeartMatch AI ❤️‍🔥", page_icon="❤️", layout="centered")

# # # Custom background style
# # page_bg = f"""
# # <style>
# # [data-testid="stAppViewContainer"] > .main {{
# #     background-color: #ffcccc;
# #     background-image: linear-gradient(to right, #ff4d4d, #ff9999);
# # }}
# # [data-testid="stHeader"] {{
# #     background-color: rgba(0,0,0,0);
# # }}
# # </style>
# # """
# # st.markdown(page_bg, unsafe_allow_html=True)

# # st.title("❤️ HeartMatch AI - Friendship Compatibility Checker")
# # st.markdown("Enter your and your partner's details to get a vibe match score! Let's find out if it's a bond worth exploring. 💑")

# # # Upload photo (optional)
# # photo = st.file_uploader("Upload your photo (optional):", type=["jpg", "jpeg", "png"])
# # if photo:
# #     st.image(photo, width=200)

# # st.header("🧍 Your Info")
# # your_name = st.text_input("Your Name")
# # your_gender = st.selectbox("Your Gender", ["Male", "Female", "Other"])
# # your_age = st.number_input("Your Age", min_value=12, max_value=100)
# # your_education = st.selectbox("Your Education", ["Matric", "Intermediate", "Graduate", "Post-Graduate", "Other"])
# # your_financial = st.selectbox("Your Financial Status", ["Low", "Medium", "Stable", "Wealthy"])
# # your_lifestyle = st.selectbox("Your Lifestyle", ["Simple", "Balanced", "Modern", "Luxury"])
# # your_love_language = st.selectbox("Your Love Language", ["Words", "Gifts", "Time", "Touch", "Acts of service"])
# # your_communication = st.selectbox("How do you express your feelings?", ["Clearly", "Hide them", "Through actions", "Through humor"])

# # talk_openness = st.selectbox("Are you open to romantic talks?", ["Yes", "Sometimes", "Rarely", "No"])
# # future_goals = st.selectbox("Do you believe in long-term commitment?", ["Yes", "Not sure", "No"])

# # st.header("💁 Partner's Info")
# # partner_name = st.text_input("Partner's Name")
# # partner_gender = st.selectbox("Partner's Gender", ["Male", "Female", "Other"])
# # partner_age = st.number_input("Partner's Age", min_value=12, max_value=100)
# # partner_education = st.selectbox("Partner's Education", ["Matric", "Intermediate", "Graduate", "Post-Graduate", "Other"])
# # partner_financial = st.selectbox("Partner's Financial Status", ["Low", "Medium", "Stable", "Wealthy"])
# # partner_lifestyle = st.selectbox("Partner's Lifestyle", ["Simple", "Balanced", "Modern", "Luxury"])
# # partner_love_language = st.selectbox("Partner's Love Language", ["Words", "Gifts", "Time", "Touch", "Acts of service"])
# # partner_communication = st.selectbox("How does your partner express feelings?", ["Clearly", "Hide them", "Through actions", "Through humor"])

# # st.header("🧠 Personality Matching")
# # deep_1 = st.selectbox("How do you handle problems?", ["Calmly", "Get emotional", "Get angry", "Ignore it"])
# # deep_2 = st.selectbox("What do you value most in others?", ["Loyalty", "Fun", "Deep conversations", "Kindness"])
# # deep_3 = st.selectbox("How do you trust new people?", ["Quickly trust", "Trust slowly", "Very cautious", "Don't trust easily"])
# # deep_4 = st.selectbox("How do you show care?", ["Spend time", "Give gifts", "Say kind words", "Physical affection", "Help them"])
# # deep_5 = st.selectbox("What kind of talks do you like more?", ["Deep talks", "Fun talks", "Both equally"])

# # partner_deep_1 = st.selectbox("Partner: How do they handle problems?", ["Calmly", "Get emotional", "Get angry", "Ignore it"])
# # partner_deep_2 = st.selectbox("Partner: What do they value?", ["Loyalty", "Fun", "Deep conversations", "Kindness"])
# # partner_deep_3 = st.selectbox("Partner: How do they trust others?", ["Quickly trust", "Trust slowly", "Very cautious", "Don't trust easily"])
# # partner_deep_4 = st.selectbox("Partner: How do they show care?", ["Spend time", "Give gifts", "Say kind words", "Physical affection", "Help them"])
# # partner_deep_5 = st.selectbox("Partner: What talks they like?", ["Deep talks", "Fun talks", "Both equally"])

# # mbti = st.text_input("MBTI Type (Optional) e.g. INFJ, ENFP")

# # if st.button("💘 Predict Friendship Score", key="predict_button"):
# #     score = 0
# #     explanations = []

# #     if deep_1 == partner_deep_1:
# #         score += 20
# #         explanations.append("✔️ You both handle problems the same way.")
# #     if deep_2 == partner_deep_2:
# #         score += 20
# #         explanations.append("✔️ You value the same traits in others.")
# #     if deep_3 == partner_deep_3:
# #         score += 15
# #         explanations.append("✔️ Your trust levels match.")
# #     if deep_4 == partner_deep_4:
# #         score += 20
# #         explanations.append("✔️ You show love in similar ways.")
# #     if deep_5 == partner_deep_5:
# #         score += 15
# #         explanations.append("✔️ You enjoy similar types of conversations.")

# #     # Lifestyle matches
# #     if your_financial == partner_financial:
# #         score += 5
# #     if your_education == partner_education:
# #         score += 5
# #     if your_lifestyle == partner_lifestyle:
# #         score += 5
# #     if your_love_language == partner_love_language:
# #         score += 5
# #     if your_communication == partner_communication:
# #         score += 5

# #     # Compatibility result
# #     st.subheader(f"🔮 Your Compatibility Score: {score}%")
# #     st.markdown("\n".join(explanations))

# #     if score >= 85:
# #         st.success("💞 Perfect emotional match! Your connection feels like destiny.")
# #         st.image("https://i.pinimg.com/originals/d7/04/75/d7047551e53988c3b65f6d2cc7707f36.gif", width=250)
# #     elif score >= 65:
# #         st.success("💖 Strong compatibility! With time and care, this bond can grow beautifully.")
# #         st.image("https://media.tenor.com/1YH6U3S3zrAAAAAC/love-couple.gif", width=250)
# #     elif score >= 45:
# #         st.warning("🌙 Some differences exist. Communication and patience will help build a strong bond.")
# #         st.image("https://media.tenor.com/4NhwNdA_zfEAAAAM/anime-love-hold.gif", width=250)
# #     else:
# #         st.error("💔 Compatibility is low. A lot of effort is needed to understand each other.")
# #         st.image("https://media.tenor.com/JWQOvnl-9xEAAAAd/anime-heartbreak.gif", width=250)

# #     st.markdown("---")
# #     st.caption("🧠 Note: This score is based on your and your partner's emotional, lifestyle, and communication patterns. It's just a fun and thoughtful way to reflect on your bond — not a final decision. 💕")
# # import streamlit as st
# # from PIL import Image

# # st.set_page_config(page_title="HeartMatch AI ❤️‍🔥", page_icon="❤️", layout="centered")

# # # Custom background style
# # page_bg = f"""
# # <style>
# # [data-testid="stAppViewContainer"] > .main {{
# #     background-color: #ffcccc;
# #     background-image: linear-gradient(to right, #ff4d4d, #ff9999);
# # }}
# # [data-testid="stHeader"] {{
# #     background-color: rgba(0,0,0,0);
# # }}
# # </style>
# # """
# # st.markdown(page_bg, unsafe_allow_html=True)

# # st.title("❤️ HeartMatch AI - Friendship Compatibility Checker")
# # st.markdown("Enter your and your partner's details to get a vibe match score! Let's find out if it's a bond worth exploring. 💑")

# # # Upload photo (optional)
# # photo = st.file_uploader("Upload your photo (optional):", type=["jpg", "jpeg", "png"])
# # if photo:
# #     st.image(photo, width=200)

# # st.header("🧍 Your Info")
# # your_name = st.text_input("Your Name")
# # your_gender = st.selectbox("Your Gender", ["Male", "Female", "Other"])
# # your_age = st.number_input("Your Age", min_value=12, max_value=100)
# # your_education = st.selectbox("Your Education", ["Matric", "Intermediate", "Graduate", "Post-Graduate", "Other"])
# # your_financial = st.selectbox("Your Financial Status", ["Low", "Medium", "Stable", "Wealthy"])
# # your_lifestyle = st.selectbox("Your Lifestyle", ["Simple", "Balanced", "Modern", "Luxury"])
# # your_love_language = st.selectbox("Your Love Language", ["Words", "Gifts", "Time", "Touch", "Acts of service"])
# # your_communication = st.selectbox("How do you express your feelings?", ["Clearly", "Hide them", "Through actions", "Through humor"])
# # talk_openness = st.selectbox("Are you open to romantic talks?", ["Yes", "Sometimes", "Rarely", "No"])
# # future_goals = st.selectbox("Do you believe in long-term commitment?", ["Yes", "Not sure", "No"])

# # st.header("💁 Partner's Info")
# # partner_name = st.text_input("Partner's Name")
# # partner_gender = st.selectbox("Partner's Gender", ["Male", "Female", "Other"])
# # partner_age = st.number_input("Partner's Age", min_value=12, max_value=100)
# # partner_education = st.selectbox("Partner's Education", ["Matric", "Intermediate", "Graduate", "Post-Graduate", "Other"])
# # partner_financial = st.selectbox("Partner's Financial Status", ["Low", "Medium", "Stable", "Wealthy"])
# # partner_lifestyle = st.selectbox("Partner's Lifestyle", ["Simple", "Balanced", "Modern", "Luxury"])
# # partner_love_language = st.selectbox("Partner's Love Language", ["Words", "Gifts", "Time", "Touch", "Acts of service"])
# # partner_communication = st.selectbox("How does your partner express feelings?", ["Clearly", "Hide them", "Through actions", "Through humor"])
# # partner_talk_openness = st.selectbox("Partner: Are they open to romantic talks?", ["Yes", "Sometimes", "Rarely", "No"])
# # partner_future_goals = st.selectbox("Partner: Do they believe in long-term commitment?", ["Yes", "Not sure", "No"])

# # st.header("🧠 Personality Matching")
# # deep_1 = st.selectbox("How do you handle problems?", ["Calmly", "Get emotional", "Get angry", "Ignore it"])
# # deep_2 = st.selectbox("What do you value most in others?", ["Loyalty", "Fun", "Deep conversations", "Kindness"])
# # deep_3 = st.selectbox("How do you trust new people?", ["Quickly trust", "Trust slowly", "Very cautious", "Don't trust easily"])
# # deep_4 = st.selectbox("How do you show care?", ["Spend time", "Give gifts", "Say kind words", "Physical affection", "Help them"])
# # deep_5 = st.selectbox("What kind of talks do you like more?", ["Deep talks", "Fun talks", "Both equally"])

# # partner_deep_1 = st.selectbox("Partner: How do they handle problems?", ["Calmly", "Get emotional", "Get angry", "Ignore it"])
# # partner_deep_2 = st.selectbox("Partner: What do they value?", ["Loyalty", "Fun", "Deep conversations", "Kindness"])
# # partner_deep_3 = st.selectbox("Partner: How do they trust others?", ["Quickly trust", "Trust slowly", "Very cautious", "Don't trust easily"])
# # partner_deep_4 = st.selectbox("Partner: How do they show care?", ["Spend time", "Give gifts", "Say kind words", "Physical affection", "Help them"])
# # partner_deep_5 = st.selectbox("Partner: What talks they like?", ["Deep talks", "Fun talks", "Both equally"])

# # mbti = st.text_input("MBTI Type (Optional) e.g. INFJ, ENFP")

# # if st.button("💘 Predict Friendship Score", key="predict_button"):
# #     score = 0
# #     explanations = []

# #     if deep_1 == partner_deep_1:
# #         score += 20
# #         explanations.append("✔️ You both handle problems the same way.")
# #     if deep_2 == partner_deep_2:
# #         score += 20
# #         explanations.append("✔️ You value the same traits in others.")
# #     if deep_3 == partner_deep_3:
# #         score += 15
# #         explanations.append("✔️ Your trust levels match.")
# #     if deep_4 == partner_deep_4:
# #         score += 20
# #         explanations.append("✔️ You show love in similar ways.")
# #     if deep_5 == partner_deep_5:
# #         score += 15
# #         explanations.append("✔️ You enjoy similar types of conversations.")

# #     if your_financial == partner_financial:
# #         score += 5
# #     if your_education == partner_education:
# #         score += 5
# #     if your_lifestyle == partner_lifestyle:
# #         score += 5
# #     if your_love_language == partner_love_language:
# #         score += 5
# #     if your_communication == partner_communication:
# #         score += 5
# #     if talk_openness == partner_talk_openness:
# #         score += 5
# #     if future_goals == partner_future_goals:
# #         score += 5

# #     st.subheader(f"🔮 Your Compatibility Score: {score}%")
# #     st.markdown("\n".join(explanations))

# #     if score >= 85:
# #         st.success("💞 Perfect emotional match! Your connection feels like destiny.")
# #         st.image("https://i.pinimg.com/originals/d7/04/75/d7047551e53988c3b65f6d2cc7707f36.gif", width=250)
# #     elif score >= 65:
# #         st.success("💖 Strong compatibility! With time and care, this bond can grow beautifully.")
# #         st.image("https://media.tenor.com/1YH6U3S3zrAAAAAC/love-couple.gif", width=250)
# #     elif score >= 45:
# #         st.warning("🌙 Some differences exist. Communication and patience will help build a strong bond.")
# #         st.image("https://media.tenor.com/4NhwNdA_zfEAAAAM/anime-love-hold.gif", width=250)
# #     else:
# #         st.error("💔 Compatibility is low. A lot of effort is needed to understand each other.")
# #         st.image("https://media.tenor.com/JWQOvnl-9xEAAAAd/anime-heartbreak.gif", width=250)

# #     st.markdown("---")
# #     st.caption("🧠 This result is based on how well your personalities, emotions, and lifestyle choices align. It's a fun way to explore emotional chemistry, not a final judgment. Talk, understand, and grow together. 💕")
# import streamlit as st
# from PIL import Image

# st.set_page_config(page_title="HeartMatch AI ❤️‍🔥", page_icon="❤️", layout="centered")

# # Background color
# st.markdown("""
# <style>
# [data-testid="stAppViewContainer"] > .main {
#     background-color: #ffe6e6;
#     background-image: linear-gradient(to right, #ff4d4d, #ff9999);
# }
# [data-testid="stHeader"] {
#     background-color: rgba(0,0,0,0);
# }
# </style>
# """, unsafe_allow_html=True)

# st.title("❤️ HeartMatch AI - Friendship Compatibility Predictor")
# st.markdown("Explore how emotionally compatible you and your partner might be. Just answer a few simple questions and get a score with an explanation! 💑")

# # Profile photo upload (optional)
# photo = st.file_uploader("Upload your photo (optional):", type=["jpg", "jpeg", "png"])
# if photo:
#     st.image(photo, width=200)

# # ---- Your Info ----
# st.header("🧍 Your Info")
# your_name = st.text_input("Your Name")
# your_age = st.number_input("Your Age", min_value=12, max_value=100)
# your_gender = st.selectbox("Your Gender", ["Male", "Female", "Other"])
# your_education = st.selectbox("Education Level", ["Matric", "Intermediate", "Graduate", "Post-Graduate"])
# your_financial = st.selectbox("Financial Status", ["Low", "Medium", "Stable", "Wealthy"])
# your_lifestyle = st.selectbox("Lifestyle", ["Simple", "Balanced", "Modern", "Luxury"])
# your_love_language = st.selectbox("Your Love Language", ["Words", "Gifts", "Time", "Touch", "Acts of Service"])
# your_communication = st.selectbox("How do you express emotions?", ["Clearly", "Hide them", "Through actions", "With humor"])
# talk_openness = st.selectbox("Are you open to romantic talks?", ["Yes", "Sometimes", "Rarely", "No"])
# future_goals = st.selectbox("Do you believe in long-term relationships?", ["Yes", "Not sure", "No"])

# # ---- Partner Info ----
# st.header("💁 Partner Info")
# partner_name = st.text_input("Partner's Name")
# partner_age = st.number_input("Partner's Age", min_value=12, max_value=100)
# partner_gender = st.selectbox("Partner's Gender", ["Male", "Female", "Other"])
# partner_education = st.selectbox("Partner's Education", ["Matric", "Intermediate", "Graduate", "Post-Graduate"])
# partner_financial = st.selectbox("Partner's Financial Status", ["Low", "Medium", "Stable", "Wealthy"])
# partner_lifestyle = st.selectbox("Partner's Lifestyle", ["Simple", "Balanced", "Modern", "Luxury"])
# partner_love_language = st.selectbox("Partner's Love Language", ["Words", "Gifts", "Time", "Touch", "Acts of Service"])
# partner_communication = st.selectbox("How does your partner express emotions?", ["Clearly", "Hide them", "Through actions", "With humor"])
# partner_talk_openness = st.selectbox("Is your partner open to romantic talks?", ["Yes", "Sometimes", "Rarely", "No"])
# partner_future_goals = st.selectbox("Do they want long-term commitment?", ["Yes", "Not sure", "No"])

# # ---- Personality Check ----
# st.header("🧠 Personality & Emotional Match")
# q1 = st.selectbox("How do you handle problems?", ["Calmly", "Get emotional", "Get angry", "Ignore it"])
# q2 = st.selectbox("What do you value most in others?", ["Loyalty", "Fun", "Deep talks", "Kindness"])
# q3 = st.selectbox("How do you trust people?", ["Quickly", "Slowly", "Very cautiously", "Rarely"])
# q4 = st.selectbox("How do you show care?", ["Time", "Gifts", "Kind words", "Physical affection", "Helping"])
# q5 = st.selectbox("What conversations do you enjoy?", ["Deep talks", "Fun talks", "Both"])

# pq1 = st.selectbox("Partner: How do they handle problems?", ["Calmly", "Get emotional", "Get angry", "Ignore it"])
# pq2 = st.selectbox("Partner: What do they value?", ["Loyalty", "Fun", "Deep talks", "Kindness"])
# pq3 = st.selectbox("Partner: How do they trust others?", ["Quickly", "Slowly", "Very cautiously", "Rarely"])
# pq4 = st.selectbox("Partner: How do they show care?", ["Time", "Gifts", "Kind words", "Physical affection", "Helping"])
# pq5 = st.selectbox("Partner: Conversations they enjoy?", ["Deep talks", "Fun talks", "Both"])

# mbti = st.text_input("MBTI Personality (optional) e.g. INFJ, ENFP")

# # ---- Prediction Logic ----
# def predict_friendship(user, girl):
#     score = 0
#     reasons = []

#     if abs(user["age"] - girl["age"]) <= 2:
#         score += 15
#         reasons.append("✅ Close in age, that's a good start!")

#     if user["city"].strip().lower() == girl["city"].strip().lower():
#         score += 10
#         reasons.append("✅ You live in the same city — easy to meet!")

#     if user["status"] == "Single" and girl["status"] == "Single":
#         score += 15
#         reasons.append("✅ Both are single — green signal! 💚")

#     if user["nature"] == girl["nature"]:
#         score += 10
#         reasons.append("✅ Matching personalities! Easy bonding.")
#     elif (user["nature"], girl["nature"]) in [("Funny", "Serious"), ("Serious", "Funny")]:
#         score += 7
#         reasons.append("✅ Opposites attract! Interesting vibe.")

#     if girl["looking"] == "Fun" and user["nature"] == "Funny":
#         score += 10
#         reasons.append("✅ They're looking for fun, and you're the fun one!")

#     if girl["response"] == "Quick" and user["communication"] == "Talkative":
#         score += 7
#         reasons.append("✅ You love talking, and they reply quickly!")

#     shared = set(user["hobbies"]) & set(girl["hobbies"])
#     if shared:
#         score += len(shared) * 3
#         reasons.append(f"✅ Shared hobbies: {', '.join(shared)}")

#     openness_diff = abs(user["openness"] - girl["openness"])
#     if openness_diff <= 2:
#         score += 8
#         reasons.append("✅ Emotionally on the same level!")

#     if user["love_language"] == girl["love_language"]:
#         score += 10
#         reasons.append("✅ Same love language! That’s deep 💞")

#     return score, reasons

# # ---- Predict Button ----
# if st.button("💌 Predict Now"):
#     score, reasons = predict_friendship(user, girl)

#     st.subheader("📊 Your Result")
#     st.markdown(f"### ❤️ Friendship Score: **{score} / 100**")

#     if score >= 75:
#         st.success("💖 Strong vibes! Looks like a great match for friendship and maybe more.")
#     elif score >= 50:
#         st.warning("💛 Average match. Try starting with light conversation and see where it goes.")
#     else:
#         st.error("💔 Low chance, but hey — every friendship starts with hello!")

#     st.markdown("### 🔍 Why This Score?")
#     for r in reasons:
#         st.write(r)

#     st.markdown("### 🌈 What You Can Do:")
#     if score >= 75:
#         st.write("Send a fun meme or ask her favorite song — let the spark begin! 🌟")
#     elif score >= 50:
#         st.write("Be kind, consistent, and funny. Let trust build naturally. 🕊️")
#     else:
#         st.write("It may not match well now — but friendship isn’t about scores. Be genuine. 🌻")
import streamlit as st
from PIL import Image

st.set_page_config(page_title="HeartMatch ❤️‍🔥", page_icon="❤️", layout="centered")
# Background style
st.markdown("""
<style>
[data-testid="stAppViewContainer"] > .main {
    background: linear-gradient(to right, #b30000, #ff1a1a);
    background-color: #ffcccc;
}
[data-testid="stHeader"] {
    background-color: #ff0066;
}
</style>
""", unsafe_allow_html=True)
# # Background style
# st.markdown("""
# <style>
# [data-testid="stAppViewContainer"] > .main {
#     background-color: #ffe6e6;
#     background-image: linear-gradient(to right, #ff4d4d, #ff9999);
# }
# [data-testid="stHeader"] {
#     background-color: rgba(0,0,0,0);
# }
# </style>
# """, unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center; color: #e6005c; font-size: 48px;'>❤️ HeartMatch AI ❤️</h1>
    <h2 style='text-align: center; color: #ff0066; font-size: 30px;'>💞 Friendship Compatibility Predictor 💞</h2>
    <p style='text-align: center; font-size: 18px; color: #333;'>Explore how emotionally compatible you and your partner might be.<br>
    Just answer a few simple questions and get a score with an explanation! 💑</p>
""", unsafe_allow_html=True)

# st.title(           "        ❤️ HeartMatch ❤️"        )
# st.title( "💞Friendship Compatibility Predictor💞")
# st.markdown("Explore how emotionally compatible you and your partner might be. Just answer a few simple questions and get a score with an explanation! 💑")

# Profile photo upload (optional)
photo = st.file_uploader("Upload your photo (optional):", type=["jpg", "jpeg", "png"])
if photo:
    st.image(photo, width=200)

# ---- Your Info ----
st.header("🧍 Your Info")
your_name = st.text_input("Your Name")
your_age = st.number_input("Your Age", min_value=12, max_value=100)
your_city = st.text_input("Your City")
your_status = st.selectbox("Your Relationship Status", ["Single", "Taken", "Complicated"])
your_gender = st.selectbox("Your Gender", ["Male", "Female", "Other"])
your_education = st.selectbox("Education Level", ["Matric", "Intermediate", "Graduate", "Post-Graduate"])
your_financial = st.selectbox("Financial Status", ["Low", "Medium", "Stable", "Wealthy"])
your_lifestyle = st.selectbox("Lifestyle", ["Simple", "Balanced", "Modern", "Luxury"])
your_love_language = st.selectbox("Your Love Language", ["Words", "Gifts", "Time", "Touch", "Acts of Service"])
your_communication = st.selectbox("How do you express emotions?", ["Clearly", "Hide them", "Through actions", "With humor"])
talk_openness = st.selectbox("Are you open to romantic talks?", ["Yes", "Sometimes", "Rarely", "No"])
future_goals = st.selectbox("Do you believe in long-term relationships?", ["Yes", "Not sure", "No"])
your_nature = st.selectbox("Your Personality", ["Funny", "Serious", "Calm", "Adventurous"])
your_response = st.selectbox("Your texting style?", ["Quick", "Slow", "Depends"])
your_openness = st.slider("How emotionally open are you?", 0, 10, 5)
your_hobbies = st.multiselect("Your Hobbies", ["Music", "Movies", "Books", "Traveling", "Gaming", "Cooking", "Fitness"])

# ---- Partner Info ----
st.header("💁 Partner Info")
partner_name = st.text_input("Partner's Name")
partner_age = st.number_input("Partner's Age", min_value=12, max_value=100)
partner_city = st.text_input("Partner's City")
partner_status = st.selectbox("Partner's Relationship Status", ["Single", "Taken", "Complicated"])
partner_gender = st.selectbox("Partner's Gender", ["Male", "Female", "Other"])
partner_education = st.selectbox("Partner's Education", ["Matric", "Intermediate", "Graduate", "Post-Graduate"])
partner_financial = st.selectbox("Partner's Financial Status", ["Low", "Medium", "Stable", "Wealthy"])
partner_lifestyle = st.selectbox("Partner's Lifestyle", ["Simple", "Balanced", "Modern", "Luxury"])
partner_love_language = st.selectbox("Partner's Love Language", ["Words", "Gifts", "Time", "Touch", "Acts of Service"])
partner_communication = st.selectbox("How does your partner express emotions?", ["Clearly", "Hide them", "Through actions", "With humor"])
partner_talk_openness = st.selectbox("Is your partner open to romantic talks?", ["Yes", "Sometimes", "Rarely", "No"])
partner_future_goals = st.selectbox("Do they want long-term commitment?", ["Yes", "Not sure", "No"])
partner_nature = st.selectbox("Partner's Personality", ["Funny", "Serious", "Calm", "Adventurous"])
partner_response = st.selectbox("Partner's texting style?", ["Quick", "Slow", "Depends"])
partner_openness = st.slider("How emotionally open is your partner?", 0, 10, 5)
partner_hobbies = st.multiselect("Partner's Hobbies", ["Music", "Movies", "Books", "Traveling", "Gaming", "Cooking", "Fitness"])
partner_looking = st.selectbox("What is your partner looking for?", ["Fun", "Serious", "Friendship"])

# ---- MBTI ----
mbti = st.text_input("MBTI Personality (optional) e.g. INFJ, ENFP")

# ---- Logic ----
def predict_friendship(user, girl):
    score = 0
    reasons = []

    if abs(user["age"] - girl["age"]) <= 2:
        score += 15
        reasons.append("✅ Close in age, that's a good start!")

    if user["city"].strip().lower() == girl["city"].strip().lower():
        score += 10
        reasons.append("✅ You live in the same city — easy to meet!")

    if user["status"] == "Single" and girl["status"] == "Single":
        score += 15
        reasons.append("✅ Both are single — green signal! 💚")

    if user["nature"] == girl["nature"]:
        score += 10
        reasons.append("✅ Matching personalities! Easy bonding.")
    elif (user["nature"], girl["nature"]) in [("Funny", "Serious"), ("Serious", "Funny")]:
        score += 7
        reasons.append("✅ Opposites attract! Interesting vibe.")

    if girl["looking"] == "Fun" and user["nature"] == "Funny":
        score += 10
        reasons.append("✅ They're looking for fun, and you're the fun one!")

    if girl["response"] == "Quick" and user["communication"] == "Clearly":
        score += 7
        reasons.append("✅ You love talking, and they reply quickly!")

    shared = set(user["hobbies"]) & set(girl["hobbies"])
    if shared:
        score += len(shared) * 3
        reasons.append(f"✅ Shared hobbies: {', '.join(shared)}")

    openness_diff = abs(user["openness"] - girl["openness"])
    if openness_diff <= 2:
        score += 8
        reasons.append("✅ Emotionally on the same level!")

    if user["love_language"] == girl["love_language"]:
        score += 10
        reasons.append("✅ Same love language! That’s deep 💞")

    return score, reasons

# ---- Predict Button ----
if st.button("💌 Predict Now"):
    user = {
        "age": your_age,
        "city": your_city,
        "status": your_status,
        "nature": your_nature,
        "response": your_response,
        "communication": your_communication,
        "hobbies": your_hobbies,
        "openness": your_openness,
        "love_language": your_love_language,
    }
    girl = {
        "age": partner_age,
        "city": partner_city,
        "status": partner_status,
        "nature": partner_nature,
        "response": partner_response,
        "communication": partner_communication,
        "hobbies": partner_hobbies,
        "openness": partner_openness,
        "love_language": partner_love_language,
        "looking": partner_looking,
    }

    score, reasons = predict_friendship(user, girl)

    st.subheader("📊 Your Result")
    st.markdown(f"### ❤️ Friendship Score: **{score} / 100**")

    if score >= 75:
        st.success("💖 Strong vibes! Looks like a great match for friendship and maybe more.")
    elif score >= 50:
        st.warning("💛 Average match. Try starting with light conversation and see where it goes.")
    else:
        st.error("💔 Low chance, but hey — every friendship starts with hello!")

    st.markdown("### 🔍 Why This Score?")
    for r in reasons:
        st.write(r)

    st.markdown("### 🌈 What You Can Do:")
    if score >= 75:
        st.write("Send a fun meme or ask her favorite song — let the spark begin! 🌟")
    elif score >= 50:
        st.write("Be kind, consistent, and funny. Let trust build naturally. 🕊️")
    else:
        st.write("It may not match well now — but friendship isn’t about scores. Be genuine. 🌻")
