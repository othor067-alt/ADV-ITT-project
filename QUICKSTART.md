# Quick Start Guide - Dating Partner Finder

## 🚀 Getting Started (5 minutes)

### Step 1: Install Dependencies
Open terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

### Step 2: Verify Files
Make sure you have these files in the directory:
- ✅ `app.py` - Main application
- ✅ `random_india_data_5000(1).xlsx` - Candidate data
- ✅ `QR.jpg` - Payment QR code
- ✅ `requirements.txt` - Python packages

### Step 3: Run Application
```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## 📖 How to Use

### First Time Users
1. **Register**: Click on any profile's "Express Interest" button
2. **Fill Form**: Enter your Name, Gender, Age, City, Caste, and Marital Status
3. **View QR**: See the payment QR code
4. **Complete**: After payment, you're all set!

### Browsing Profiles

#### 1. **Filter Profiles**
   - Use sidebar filters on the left
   - Select Gender, Age Range, Height, Weight, City, Caste, Status
   - Click "Reset Filters" to clear all

#### 2. **Search by Name**
   - Type candidate name in search box
   - Results update instantly

#### 3. **Sort Results**
   - Sort by: Age (ascending/descending), Height, Weight, Name
   - Default: No sorting

#### 4. **View Profiles**
   - **Cards View**: Beautiful profile cards with match score
   - **Table View**: Spreadsheet format
   - Toggle using the View dropdown

#### 5. **Express Interest**
   - Click "💗 Express Interest" button on any profile
   - Complete payment (Rs. 11)
   - Profile owner gets notified!

---

## 💎 Services

### Premium Membership (Rs. 99)
✅ All features unlocked
✅ Priority support
✅ Enhanced profile visibility
✅ Advanced analytics

### Express Interest (Rs. 11 per profile)
✅ Notify profile owner
✅ Open direct channel
✅ Show in their dashboard
✅ Instant matching suggestions

### QR Profile (Rs. 99)
✅ Professional QR code
✅ Share on social media
✅ Track profile views
✅ Easy profile distribution

---

## 📊 Dashboard Metrics

At the top of Home page, you'll see:
- **Total Profiles**: All candidates in database
- **Matching Profiles**: Results after applying your filters
- **Average Age**: Mean age of filtered candidates
- **Average Height**: Mean height of filtered candidates

---

## ❤️ Match Score Explained

Your compatibility score (0-100%) is based on:

| Factor | Points | Scoring |
|--------|--------|---------|
| Age Similarity | 30 | ±2 years = 30pts, ±5 years = 20pts, ±10 years = 10pts |
| City Match | 25 | Same city = 25pts |
| Caste Match | 25 | Same caste = 25pts |
| Marital Status | 20 | Same status = 20pts |

**Example**: Same city (25) + Similar age (20) + Same caste (25) = **70% match**

---

## 🔐 Privacy & Security

- Phone numbers are **blurred** in display (XXX-XXXX-XXX)
- Your profile details are kept **secure**
- Payment processed via **QR code** for privacy
- No data is shared without your consent

---

## ⚙️ Troubleshooting

### Issue: "Error loading data"
**Solution**: Check if Excel file path is correct in app.py

### Issue: QR code not showing
**Solution**: Verify QR.jpg exists in the project directory

### Issue: Filters not working
**Solution**: Make sure Excel columns match exactly:
- Name, Gender, Age, Height_cm, Weight_kg, City, MobileNumber, Caste, MaritalStatus

### Issue: Slow performance
**Solution**: This is normal with 5000 profiles. Filter to narrow down results.

---

## 📱 Mobile Support

✅ Works on mobile browsers
✅ Responsive design
✅ Touch-friendly buttons
✅ Full functionality on mobile

---

## 🎨 UI Navigation

### Top Ribbon (Main Navigation)
- 🏠 **Home**: Browse profiles
- 🎯 **Services**: View pricing & features
- 📞 **Contact Us**: Get in touch

### Left Sidebar
- 👤 User profile (when logged in)
- 🔍 All filters
- 🚪 Logout button

### Dashboard Area
- 📊 Metrics
- 🔍 Search box
- ⬇️ Sort options
- 📋 View type selector

---

## 💳 Payment Details

**Payment Methods**:
- Scan QR code using any UPI app
- Works with Google Pay, PhonePe, Paytm

**When Payment is Required**:
1. ❤️ Express Interest: Rs. 11
2. 💎 Premium Membership: Rs. 99
3. 📱 QR Code Profile: Rs. 99

**After Payment**:
- Confirmation message appears
- Action is completed immediately
- Results are visible in your profile

---

## 🌟 Pro Tips

1. **Better Matches**: Set realistic filters based on your preferences
2. **Quick Browse**: Use Table View for fast scanning
3. **Deep Dive**: Use Card View to see detailed info
4. **Smart Sorting**: Sort by Height to find your ideal match
5. **Save Time**: Use Search if you know the name
6. **Pagination**: Only 20 profiles per page keeps it manageable

---

## 📞 Support

- **Email**: support@datingpartner.com
- **Phone**: +91-9876543210
- **Hours**: Mon-Fri 9AM-6PM, Sat 10AM-4PM
- **Chat**: 24/7 Live Chat Available

---

## 🎯 Next Steps

1. ✅ Install requirements
2. ✅ Run the app
3. ✅ Register your profile
4. ✅ Start browsing
5. ✅ Express interest
6. ✅ Find your match! 💕

---

**Good luck finding your perfect match!** 🥰
