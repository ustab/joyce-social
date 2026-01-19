import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="EVEYES 360 - Joyce Social", page_icon="🚀")

# Başlık ve Dil Seçeneği
st.title("🚀 Joyce Social Page")
dil = st.sidebar.selectbox("Dil Seçiniz / Select Language", ["Türkçe", "English", "Español", "Français", "Yoruba"])

# Basit Veri Saklama (Session State)
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {"user": "Joyce_Client", "content": "Harika bir arayüz oldu! 😍", "likes": 120},
        {"user": "EVEYES_360", "content": "Geleceğin teknolojisini kodluyoruz.", "likes": 360}
    ]

# Gönderi Paylaşma Alanı
with st.form("post_form"):
    user = st.text_input("User_Name")
    content = st.text_area("Comment")
    submitted = st.form_submit_button("sharing")
    if submitted and user and content:
        st.session_state.posts.append({"user": user, "content": content, "likes": 0})
        st.success("Gönderi Paylaşıldı!")

# Akışı Gösterme
st.subheader("📱 NEWS")
for i, post in enumerate(st.session_state.posts):
    with st.container():
        st.write(f"### 👤 @{post['user']}")
        st.write(post['content'])
        col1, col2 = st.columns([1, 4])
        if col1.button(f"❤️ {post['likes']}", key=f"like_{i}"):
            post['likes'] += 1
            st.rerun()
        st.divider()



