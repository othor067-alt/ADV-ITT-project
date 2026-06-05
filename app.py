import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import re
from PIL import Image
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Dating Partner Finder",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern matrimonial theme
st.markdown("""
    <style>
        /* Main styling */
        :root {
            --primary-color: #ff6b9d;
            --secondary-color: #fff0f3;
            --accent-color: #ffa6c1;
            --text-color: #333333;
            --light-gray: #f5f5f5;
        }
        
        /* Ribbon Navigation */
        .ribbon-container {
            display: flex;
            gap: 2rem;
            padding: 1.5rem 2rem;
            background: linear-gradient(135deg, #ff6b9d 0%, #ffa6c1 100%);
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 15px rgba(255, 107, 157, 0.2);
        }
        
        .ribbon-item {
            padding: 0.8rem 1.5rem;
            font-size: 1.1rem;
            font-weight: 600;
            color: white;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.3s ease;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid transparent;
        }
        
        .ribbon-item:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
            border: 2px solid white;
        }
        
        .ribbon-item.active {
            background: white;
            color: #ff6b9d;
            border: 2px solid white;
        }
        
        /* Dashboard cards */
        .metric-card {
            background: linear-gradient(135deg, #fff0f3 0%, #ffffff 100%);
            padding: 1.5rem;
            border-radius: 12px;
            border: 2px solid #ff6b9d;
            box-shadow: 0 4px 15px rgba(255, 107, 157, 0.1);
            text-align: center;
        }
        
        .metric-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: #ff6b9d;
            margin: 0.5rem 0;
        }
        
        .metric-label {
            font-size: 1rem;
            color: #666;
            font-weight: 500;
        }
        
        /* Profile cards */
        .profile-card {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 4px 20px rgba(255, 107, 157, 0.15);
            border: 2px solid #fff0f3;
            transition: all 0.3s ease;
            overflow: hidden;
        }
        
        .profile-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(255, 107, 157, 0.25);
        }
        
        .profile-header {
            display: flex;
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }
        
        .profile-image {
            width: 120px;
            height: 120px;
            border-radius: 12px;
            background: linear-gradient(135deg, #ff6b9d 0%, #ffa6c1 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 3rem;
            flex-shrink: 0;
        }
        
        .profile-info {
            flex: 1;
        }
        
        .profile-name {
            font-size: 1.5rem;
            font-weight: 700;
            color: #ff6b9d;
            margin-bottom: 0.5rem;
        }
        
        .profile-details {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.8rem;
            margin: 1rem 0;
            font-size: 0.95rem;
        }
        
        .detail-item {
            background: #fff0f3;
            padding: 0.6rem;
            border-radius: 8px;
            color: #333;
        }
        
        .detail-label {
            font-weight: 600;
            color: #ff6b9d;
        }
        
        /* Match score */
        .match-score-container {
            background: linear-gradient(135deg, #fff0f3 0%, #ffffff 100%);
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
        
        .match-score-text {
            font-size: 1.1rem;
            font-weight: 600;
            color: #ff6b9d;
            margin-bottom: 0.5rem;
        }
        
        .match-score-bar {
            width: 100%;
            height: 10px;
            background: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            margin: 0.5rem 0;
        }
        
        .match-score-fill {
            height: 100%;
            background: linear-gradient(90deg, #ff6b9d, #ffa6c1);
            border-radius: 10px;
            transition: width 0.3s ease;
        }
        
        /* Buttons */
        .express-interest-btn {
            background: linear-gradient(135deg, #ff6b9d 0%, #ffa6c1 100%);
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            font-size: 1rem;
            margin-top: 1rem;
        }
        
        .express-interest-btn:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 15px rgba(255, 107, 157, 0.4);
        }
        
        .reset-btn {
            background: #ff6b9d;
            color: white;
            padding: 0.8rem 1.5rem;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
        }
        
        /* Sidebar styling */
        .sidebar-title {
            color: #ff6b9d;
            font-weight: 700;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
            font-size: 1.1rem;
        }
        
        /* Contact section */
        .contact-section {
            background: linear-gradient(135deg, #fff0f3 0%, #ffffff 100%);
            padding: 2rem;
            border-radius: 15px;
            border: 2px solid #ff6b9d;
            margin: 2rem 0;
        }
        
        .contact-title {
            font-size: 2rem;
            font-weight: 700;
            color: #ff6b9d;
            margin-bottom: 1.5rem;
        }
        
        .contact-item {
            display: flex;
            gap: 1rem;
            margin: 1rem 0;
            font-size: 1.1rem;
        }
        
        .contact-icon {
            color: #ff6b9d;
            font-weight: 700;
            min-width: 30px;
        }
        
        /* Payment modal */
        .payment-modal {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
            border: 2px solid #ff6b9d;
        }
        
        /* Search box */
        .search-container {
            margin: 1.5rem 0;
        }
        
        /* Services section */
        .service-card {
            background: linear-gradient(135deg, #fff0f3 0%, #ffffff 100%);
            border: 2px solid #ff6b9d;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 4px 15px rgba(255, 107, 157, 0.1);
        }
        
        .service-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #ff6b9d;
            margin-bottom: 1rem;
        }
        
        .service-description {
            color: #333;
            font-size: 1rem;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'user_interests' not in st.session_state:
    st.session_state.user_interests = []
if 'page_number' not in st.session_state:
    st.session_state.page_number = 0

# Load data function
@st.cache_data
def load_data():
    """Load data from Excel file"""
    try:
        df = pd.read_excel(r"c:\Users\ICAI-PC\OneDrive\Desktop\it CALC\random_india_data_5000(1).xlsx")
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Helper function to blur phone numbers
def blur_phone(phone):
    """Blur phone number for display"""
    phone_str = str(phone)
    if len(phone_str) >= 10:
        return phone_str[:3] + "****" + phone_str[-3:]
    return "****" + phone_str[-3:]

# Calculate match score
def calculate_match_score(candidate, current_user):
    """Calculate compatibility score based on multiple factors"""
    if not current_user:
        return 0
    
    score = 0
    
    # Age similarity (0-30 points)
    age_diff = abs(candidate['Age'] - current_user['age'])
    if age_diff <= 2:
        score += 30
    elif age_diff <= 5:
        score += 20
    elif age_diff <= 10:
        score += 10
    else:
        score += 5
    
    # City match (0-25 points)
    if candidate['City'] == current_user['city']:
        score += 25
    
    # Caste match (0-25 points)
    if candidate['Caste'] == current_user['caste']:
        score += 25
    
    # Marital status match (0-20 points)
    if candidate['MaritalStatus'] == current_user['marital_status']:
        score += 20
    
    return min(int(score), 100)

# Function to display profile card
def display_profile_card(profile, match_score, col):
    """Display individual profile card"""
    with col:
        st.markdown("""
            <div class="profile-card">
        """, unsafe_allow_html=True)
        
        # Profile header with image
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("""
                <div class="profile-image">👤</div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div class="profile-info">
                    <div class="profile-name">{profile['Name']}</div>
                    <div style="color: #666; font-size: 0.9rem;">
                        <strong style="color: #ff6b9d;">{profile['Gender']}</strong> • <strong>{profile['Age']}</strong> years
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Profile details
        st.markdown(f"""
            <div class="profile-details">
                <div class="detail-item"><span class="detail-label">Height:</span> {profile['Height_cm']} cm</div>
                <div class="detail-item"><span class="detail-label">Weight:</span> {profile['Weight_kg']} kg</div>
                <div class="detail-item"><span class="detail-label">City:</span> {profile['City']}</div>
                <div class="detail-item"><span class="detail-label">Caste:</span> {profile['Caste']}</div>
                <div class="detail-item"><span class="detail-label">Status:</span> {profile['MaritalStatus']}</div>
                <div class="detail-item"><span class="detail-label">Phone:</span> {blur_phone(profile['MobileNumber'])}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Match score
        if st.session_state.current_user:
            st.markdown(f"""
                <div class="match-score-container">
                    <div class="match-score-text">💕 Match Score: {match_score}%</div>
                    <div class="match-score-bar">
                        <div class="match-score-fill" style="width: {match_score}%;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Express Interest button
        if st.button("💗 Express Interest", key=f"interest_{profile['Name']}_{profile['MobileNumber']}"):
            st.session_state.show_payment_modal = True
            st.session_state.selected_profile = profile
            st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

# Home Page
def show_home():
    """Display home page with dashboard and profiles"""
    st.title("❤️ Dating Partner Finder")
    
    # Load data
    df = load_data()
    if df is None:
        st.error("Unable to load data. Please check the Excel file.")
        return
    
    # Create filters in sidebar
    st.sidebar.markdown("### 🔍 Filters")
    
    # Gender filter
    genders = df['Gender'].unique().tolist()
    selected_genders = st.sidebar.multiselect(
        "Gender",
        options=genders,
        default=genders,
        key="gender_filter"
    )
    
    # Age range slider
    age_min, age_max = int(df['Age'].min()), int(df['Age'].max())
    age_range = st.sidebar.slider(
        "Age Range",
        min_value=age_min,
        max_value=age_max,
        value=(age_min, age_max),
        key="age_filter"
    )
    
    # Height range slider
    height_min, height_max = int(df['Height_cm'].min()), int(df['Height_cm'].max())
    height_range = st.sidebar.slider(
        "Height (cm)",
        min_value=height_min,
        max_value=height_max,
        value=(height_min, height_max),
        key="height_filter"
    )
    
    # Weight range slider
    weight_min, weight_max = int(df['Weight_kg'].min()), int(df['Weight_kg'].max())
    weight_range = st.sidebar.slider(
        "Weight (kg)",
        min_value=weight_min,
        max_value=weight_max,
        value=(weight_min, weight_max),
        key="weight_filter"
    )
    
    # City filter
    cities = sorted(df['City'].unique().tolist())
    selected_cities = st.sidebar.multiselect(
        "City",
        options=cities,
        default=cities,
        key="city_filter"
    )
    
    # Caste filter
    castes = sorted(df['Caste'].unique().tolist())
    selected_castes = st.sidebar.multiselect(
        "Caste",
        options=castes,
        default=castes,
        key="caste_filter"
    )
    
    # Marital Status filter
    statuses = df['MaritalStatus'].unique().tolist()
    selected_statuses = st.sidebar.multiselect(
        "Marital Status",
        options=statuses,
        default=statuses,
        key="status_filter"
    )
    
    # Reset Filters button
    if st.sidebar.button("🔄 Reset Filters", key="reset_btn"):
        st.session_state.page_number = 0
        st.rerun()
    
    # Apply filters
    filtered_df = df[
        (df['Gender'].isin(selected_genders)) &
        (df['Age'].between(age_range[0], age_range[1])) &
        (df['Height_cm'].between(height_range[0], height_range[1])) &
        (df['Weight_kg'].between(weight_range[0], weight_range[1])) &
        (df['City'].isin(selected_cities)) &
        (df['Caste'].isin(selected_castes)) &
        (df['MaritalStatus'].isin(selected_statuses))
    ].reset_index(drop=True)
    
    # Main content area
    # Dashboard metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Total Profiles</div>
                <div class="metric-value">{len(df):,}</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Matching Profiles</div>
                <div class="metric-value">{len(filtered_df):,}</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        avg_age = int(filtered_df['Age'].mean()) if len(filtered_df) > 0 else 0
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Average Age</div>
                <div class="metric-value">{avg_age}</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        avg_height = int(filtered_df['Height_cm'].mean()) if len(filtered_df) > 0 else 0
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Average Height</div>
                <div class="metric-value">{avg_height} cm</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Search, Sort, and View Options
    search_col, sort_col, view_col = st.columns([2, 2, 2])
    
    with search_col:
        search_name = st.text_input("🔍 Search by Name", placeholder="Enter candidate name")
    
    with sort_col:
        sort_by = st.selectbox(
            "Sort By",
            ["None", "Age (Low to High)", "Age (High to Low)", "Height", "Weight", "Name"],
            key="sort_select"
        )
    
    with view_col:
        view_type = st.selectbox(
            "View",
            ["Profile Cards", "Data Table"],
            key="view_select"
        )
    
    # Apply search filter
    if search_name:
        filtered_df = filtered_df[
            filtered_df['Name'].str.contains(search_name, case=False, na=False)
        ]
    
    # Apply sorting
    if sort_by == "Age (Low to High)":
        filtered_df = filtered_df.sort_values('Age', ascending=True)
    elif sort_by == "Age (High to Low)":
        filtered_df = filtered_df.sort_values('Age', ascending=False)
    elif sort_by == "Height":
        filtered_df = filtered_df.sort_values('Height_cm', ascending=False)
    elif sort_by == "Weight":
        filtered_df = filtered_df.sort_values('Weight_kg', ascending=False)
    elif sort_by == "Name":
        filtered_df = filtered_df.sort_values('Name', ascending=True)
    
    # Display results
    if len(filtered_df) == 0:
        st.warning("No profiles match your criteria. Please adjust filters.")
    else:
        if view_type == "Data Table":
            # Display as table with blurred phone numbers
            display_df = filtered_df.copy()
            display_df['MobileNumber'] = display_df['MobileNumber'].apply(blur_phone)
            st.dataframe(
                display_df,
                use_container_width=True,
                height=400,
                column_config={
                    'MobileNumber': st.column_config.TextColumn('Mobile Number'),
                }
            )
        else:
            # Display as profile cards with pagination
            profiles_per_page = 20
            total_pages = (len(filtered_df) + profiles_per_page - 1) // profiles_per_page
            
            # Pagination controls
            pag_col1, pag_col2, pag_col3 = st.columns([1, 3, 1])
            
            with pag_col1:
                if st.button("⬅️ Previous", key="prev_btn"):
                    st.session_state.page_number = max(0, st.session_state.page_number - 1)
                    st.rerun()
            
            with pag_col2:
                st.markdown(
                    f"<div style='text-align: center; padding: 0.5rem; color: #ff6b9d; font-weight: 600;'>"
                    f"Page {st.session_state.page_number + 1} of {total_pages} | "
                    f"Showing {min(profiles_per_page, len(filtered_df) - st.session_state.page_number * profiles_per_page)} "
                    f"of {len(filtered_df)} profiles</div>",
                    unsafe_allow_html=True
                )
            
            with pag_col3:
                if st.button("Next ➡️", key="next_btn"):
                    if st.session_state.page_number < total_pages - 1:
                        st.session_state.page_number += 1
                        st.rerun()
            
            st.markdown("---")
            
            # Display profile cards
            start_idx = st.session_state.page_number * profiles_per_page
            end_idx = min(start_idx + profiles_per_page, len(filtered_df))
            
            page_profiles = filtered_df.iloc[start_idx:end_idx]
            
            for i in range(0, len(page_profiles), 2):
                cols = st.columns(2)
                
                for j, col in enumerate(cols):
                    if i + j < len(page_profiles):
                        profile = page_profiles.iloc[i + j]
                        match_score = calculate_match_score(profile, st.session_state.current_user)
                        display_profile_card(profile, match_score, col)

# Services Page
def show_services():
    """Display services page"""
    st.title("🎯 Our Services")
    
    st.markdown("""
        <div class="service-card">
            <div class="service-title">💎 Premium Membership - Rs. 99</div>
            <div class="service-description">
                Get access to high-resolution profiles and unlock all features including:
                <ul>
                    <li>View complete profile details</li>
                    <li>Express interest to multiple profiles</li>
                    <li>Advanced filtering options</li>
                    <li>Priority customer support</li>
                    <li>QR code for easy profile sharing</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="service-card">
            <div class="service-title">❤️ Express Interest - Rs. 11 per profile</div>
            <div class="service-description">
                Show your interest to potential matches. When you express interest:
                <ul>
                    <li>Profile owner gets notified immediately</li>
                    <li>Direct communication channel opens</li>
                    <li>Match suggestions based on compatibility</li>
                    <li>Visible on their profile dashboard</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="service-card">
            <div class="service-title">📱 QR Code Profile Sharing - Rs. 99</div>
            <div class="service-description">
                Share your profile easily with a unique QR code:
                <ul>
                    <li>Professional QR code design</li>
                    <li>Easy sharing across social media</li>
                    <li>Track profile views</li>
                    <li>Customizable sharing options</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="service-card">
            <div class="service-title">🔍 Advanced Matching Algorithm</div>
            <div class="service-description">
                Our AI-powered matching system calculates compatibility based on:
                <ul>
                    <li>Age similarity scores</li>
                    <li>Geographic proximity</li>
                    <li>Caste and cultural compatibility</li>
                    <li>Marital status alignment</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🛒 Subscribe to Premium", key="subscribe_btn"):
            st.session_state.show_payment_modal = True
            st.session_state.payment_type = 'premium'
            st.rerun()
    
    with col2:
        if st.button("📥 Get QR Code", key="qr_btn"):
            st.session_state.show_payment_modal = True
            st.session_state.payment_type = 'qr'
            st.rerun()

# Contact Us Page
def show_contact():
    """Display contact page"""
    st.title("📞 Contact Us")
    
    st.markdown("""
        <div class="contact-section">
            <div class="contact-title">Get in Touch</div>
            
            <div class="contact-item">
                <span class="contact-icon">📍</span>
                <span>
                    <strong>Address:</strong><br>
                    Dating Partner Finder HQ<br>
                    123 Love Street, Romantic City<br>
                    India - 123456
                </span>
            </div>
            
            <div class="contact-item">
                <span class="contact-icon">📱</span>
                <span>
                    <strong>Phone:</strong><br>
                    +91-9876543210<br>
                    +91-9876543211 (Support)
                </span>
            </div>
            
            <div class="contact-item">
                <span class="contact-icon">✉️</span>
                <span>
                    <strong>Email:</strong><br>
                    info@datingpartner.com<br>
                    support@datingpartner.com
                </span>
            </div>
            
            <div class="contact-item">
                <span class="contact-icon">⏰</span>
                <span>
                    <strong>Business Hours:</strong><br>
                    Monday - Friday: 9:00 AM - 6:00 PM<br>
                    Saturday: 10:00 AM - 4:00 PM<br>
                    Sunday: Closed
                </span>
            </div>
            
            <div class="contact-item">
                <span class="contact-icon">💬</span>
                <span>
                    <strong>Customer Support:</strong><br>
                    24/7 Live Chat Available<br>
                    Response Time: Within 2 hours
                </span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Contact form
    st.markdown("### Send us a Message")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name", placeholder="Enter your full name")
        email = st.text_input("Email Address", placeholder="your.email@example.com")
        subject = st.text_input("Subject", placeholder="What is this about?")
        message = st.text_area("Message", placeholder="Type your message here...", height=150)
        
        if st.form_submit_button("📨 Send Message", use_container_width=True):
            if name and email and subject and message:
                st.success("✅ Thank you for your message! We'll get back to you soon.")
            else:
                st.error("❌ Please fill in all fields.")

# Horizontal Navigation
def show_navigation():
    """Display horizontal ribbon navigation"""
    pages = ['home', 'services', 'contact']
    page_labels = ['🏠 Home', '🎯 Services', '📞 Contact Us']
    
    cols = st.columns(len(pages))
    
    for i, (col, page, label) in enumerate(zip(cols, pages, page_labels)):
        with col:
            is_active = st.session_state.current_page == page
            style_class = "ribbon-item active" if is_active else "ribbon-item"
            
            if st.button(label, key=f"nav_{page}", use_container_width=True):
                st.session_state.current_page = page
                st.rerun()

# Payment Modal
def show_payment_modal():
    """Display payment modal"""
    if not st.session_state.get('show_payment_modal', False):
        return
    
    modal_placeholder = st.empty()
    
    with modal_placeholder.container():
        st.markdown("""
            <div style="background: rgba(0, 0, 0, 0.7); position: fixed; top: 0; left: 0; right: 0; bottom: 0; display: flex; align-items: center; justify-content: center; z-index: 1000;">
        """, unsafe_allow_html=True)
        
        col_left, col_center, col_right = st.columns([1, 2, 1])
        
        with col_center:
            st.markdown("""
                <div class="payment-modal">
            """, unsafe_allow_html=True)
            
            # Check if user is logged in
            if not st.session_state.current_user:
                st.markdown("### 📝 User Registration")
                st.info("Please register to continue with payment.")
                
                user_name = st.text_input("Full Name", placeholder="Enter your full name")
                user_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
                user_age = st.number_input("Age", min_value=18, max_value=100, step=1)
                user_city = st.text_input("City", placeholder="Enter your city")
                user_caste = st.text_input("Caste", placeholder="Enter your caste")
                user_marital_status = st.selectbox(
                    "Marital Status",
                    ["Single", "Divorced", "Widowed", "Separated"]
                )
                
                if st.button("✅ Complete Registration"):
                    if user_name and user_gender and user_age and user_city and user_caste:
                        st.session_state.current_user = {
                            'name': user_name,
                            'gender': user_gender,
                            'age': user_age,
                            'city': user_city,
                            'caste': user_caste,
                            'marital_status': user_marital_status
                        }
                        st.success("✅ Registration successful!")
                        st.rerun()
                    else:
                        st.error("❌ Please fill in all fields.")
            else:
                payment_type = st.session_state.get('payment_type', 'interest')
                
                if payment_type == 'interest':
                    st.markdown("### 💗 Express Interest")
                    st.write(f"**Selected Profile:** {st.session_state.selected_profile['Name']}")
                    st.write(f"**Amount:** Rs. 11")
                    
                    # Show QR code
                    try:
                        img = Image.open(r"c:\Users\ICAI-PC\OneDrive\Desktop\it CALC\QR.jpg")
                        st.image(img, width=200, caption="Scan to Pay")
                    except:
                        st.info("QR Code not available")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("✅ Payment Done"):
                            st.session_state.user_interests.append(st.session_state.selected_profile['Name'])
                            st.success("❤️ Interest expressed successfully! The profile owner has been notified.")
                            st.session_state.show_payment_modal = False
                            st.rerun()
                    
                    with col2:
                        if st.button("❌ Cancel"):
                            st.session_state.show_payment_modal = False
                            st.rerun()
                
                elif payment_type == 'premium':
                    st.markdown("### 💎 Premium Membership")
                    st.write("**Amount:** Rs. 99")
                    
                    # Show QR code
                    try:
                        img = Image.open(r"c:\Users\ICAI-PC\OneDrive\Desktop\it CALC\QR.jpg")
                        st.image(img, width=200, caption="Scan to Pay")
                    except:
                        st.info("QR Code not available")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("✅ Payment Done"):
                            st.success("💎 Premium membership activated!")
                            st.session_state.show_payment_modal = False
                            st.rerun()
                    
                    with col2:
                        if st.button("❌ Cancel"):
                            st.session_state.show_payment_modal = False
                            st.rerun()
                
                elif payment_type == 'qr':
                    st.markdown("### 📱 QR Code Profile")
                    st.write("**Amount:** Rs. 99")
                    
                    # Show QR code
                    try:
                        img = Image.open(r"c:\Users\ICAI-PC\OneDrive\Desktop\it CALC\QR.jpg")
                        st.image(img, width=200, caption="Scan to Pay")
                    except:
                        st.info("QR Code not available")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("✅ Payment Done"):
                            st.success("📱 QR code generated! Your profile is now easily shareable.")
                            st.session_state.show_payment_modal = False
                            st.rerun()
                    
                    with col2:
                        if st.button("❌ Cancel"):
                            st.session_state.show_payment_modal = False
                            st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)

# Main app
def main():
    # Display navigation ribbon
    st.markdown("""
        <div class="ribbon-container">
    """, unsafe_allow_html=True)
    
    # Create horizontal navigation buttons
    nav_cols = st.columns(3)
    
    with nav_cols[0]:
        if st.button("🏠 Home", use_container_width=True, key="nav_home_main"):
            st.session_state.current_page = 'home'
            st.rerun()
    
    with nav_cols[1]:
        if st.button("🎯 Services", use_container_width=True, key="nav_services_main"):
            st.session_state.current_page = 'services'
            st.rerun()
    
    with nav_cols[2]:
        if st.button("📞 Contact Us", use_container_width=True, key="nav_contact_main"):
            st.session_state.current_page = 'contact'
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Display current user info
    if st.session_state.current_user:
        st.sidebar.markdown("""
            <div style="background: linear-gradient(135deg, #ff6b9d 0%, #ffa6c1 100%); 
                        padding: 1rem; border-radius: 10px; color: white; margin-bottom: 1rem;">
                <div style="font-weight: 700; margin-bottom: 0.5rem;">👤 User Profile</div>
                <div style="font-size: 0.9rem;">
                    <strong>Name:</strong> {}<br>
                    <strong>Gender:</strong> {}<br>
                    <strong>Age:</strong> {}<br>
                    <strong>City:</strong> {}
                </div>
            </div>
        """.format(
            st.session_state.current_user['name'],
            st.session_state.current_user['gender'],
            st.session_state.current_user['age'],
            st.session_state.current_user['city']
        ), unsafe_allow_html=True)
        
        if st.sidebar.button("🚪 Logout", use_container_width=True):
            st.session_state.current_user = None
            st.session_state.user_interests = []
            st.rerun()
    
    # Route to appropriate page
    if st.session_state.current_page == 'home':
        show_home()
    elif st.session_state.current_page == 'services':
        show_services()
    elif st.session_state.current_page == 'contact':
        show_contact()
    
    # Show payment modal if needed
    show_payment_modal()

if __name__ == "__main__":
    main()
