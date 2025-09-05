
import streamlit as st

# Page config
st.set_page_config(
    page_title="AI Image Studio Lite",
    page_icon="🎨",
    layout="wide"
)

# Get API key from Streamlit secrets
api_key = st.secrets["STABILITY_API_KEY"]

# Sidebar navigation
st.sidebar.title("🎨 AI Image Studio Lite")
page = st.sidebar.selectbox(
    "Choose a feature:",
    ["🏠 Home", "✨ Generate", "📈 Upscale", "✏️ Edit", "🎛️ Control"]
)

# Main content based on selected page
if page == "🏠 Home":
    st.title("🎨 AI Image Studio Lite")
    st.write("Your personal AI-powered image creation suite - Fast deployment version")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.subheader("✨ Generate")
        st.write("Create images from text prompts using the latest AI models")
        
    with col2:
        st.subheader("📈 Upscale")
        st.write("Enhance image resolution and quality")
        
    with col3:
        st.subheader("✏️ Edit")
        st.write("Advanced editing with masking and inpainting")
        
    with col4:
        st.subheader("🎛️ Control")
        st.write("Precise control over image generation")

elif page == "✨ Generate":
    st.header("✨ Image Generation")
    from modules.generate import show_generation_interface
    show_generation_interface(api_key)

elif page == "📈 Upscale":
    st.header("📈 Image Upscaling")  
    st.write("Upscaling feature coming soon...")

elif page == "✏️ Edit":
    st.header("✏️ Image Editing")
    st.write("Editing features coming soon...")

elif page == "🎛️ Control":
    st.header("🎛️ Advanced Control")
    st.write("Control features coming soon...")
