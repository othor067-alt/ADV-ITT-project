# 💗 Dating Partner Finder - Streamlit Web Application

A modern, professional matrimonial dating partner finder web application built with Streamlit and Python.

## Features

### 🏠 Home Page
- **Dashboard Metrics**: Total profiles, matching profiles, average age, and average height
- **Advanced Filters**: Gender, age range, height range, weight range, city, caste, marital status
- **Search Functionality**: Search profiles by candidate name
- **Sorting Options**: Sort by age, height, weight, and name
- **Pagination**: Display 20 profiles per page with navigation
- **Profile Cards**: Beautiful, modern profile card design with match score
- **Match Score**: AI-based compatibility scoring based on age, city, caste, and marital status

### 🎯 Services Page
- **Premium Membership** (Rs. 99): Access to all features and priority support
- **Express Interest** (Rs. 11): Show interest to potential matches with instant notifications
- **QR Code Profile** (Rs. 99): Generate shareable QR code for easy profile distribution

### 📞 Contact Us Page
- Complete contact information
- Business address and phone numbers
- Business hours
- Contact form for inquiries

### 💳 Payment System
- QR code-based payment gateway
- User registration before payment
- Secure payment processing display

## Installation

### Step 1: Install Python Packages
```bash
pip install -r requirements.txt
```

### Step 2: Prepare Data Files
Ensure the following files are in the same directory as app.py:
- `random_india_data_5000(1).xlsx` - Excel file with candidate data
- `QR.jpg` - QR code image for payments

### Step 3: Run the Application
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## Data Structure

The Excel file should contain the following columns:
- **Name**: Candidate's full name
- **Gender**: Male/Female
- **Age**: Age in years
- **Height_cm**: Height in centimeters
- **Weight_kg**: Weight in kilograms
- **City**: City name
- **MobileNumber**: Phone number (blurred in display)
- **Caste**: Caste information
- **MaritalStatus**: Marital status

## User Features

### Filtering & Search
- Multi-select filters for gender, city, caste, marital status
- Range sliders for age, height, weight
- Real-time search by name
- Reset filters button

### Viewing Options
- **Profile Cards**: Beautiful card-based layout with hover effects
- **Data Table**: Spreadsheet-style view with all information
- **Pagination**: Navigate through profiles efficiently

### Profile Information Display
- Candidate name and basic details
- Blurred phone numbers for privacy
- Compatibility match score (0-100%)
- Visual match score progress bar
- Express Interest button with payment integration

### User Registration
- One-time registration required before expressing interest
- Collects: Name, Gender, Age, City, Caste, Marital Status
- Information used for match score calculation

## Match Score Calculation

The compatibility score is calculated based on:
- **Age Similarity** (0-30 points): Closer age = higher score
- **City Match** (0-25 points): Same city = 25 points
- **Caste Match** (0-25 points): Same caste = 25 points
- **Marital Status Match** (0-20 points): Same status = 20 points

## Privacy & Security

- Phone numbers are blurred in all displays (XXX-XXXX-XXX format)
- User data is stored in session state
- Payment processing through QR code
- Express interest requires user registration

## UI/UX Design

- **Color Scheme**: Modern pink and white palette (#ff6b9d, #ffa6c1)
- **Responsive Design**: Works on desktop and tablet devices
- **Smooth Animations**: Hover effects and transitions
- **Professional Typography**: Clean, readable fonts
- **Rounded Elements**: Soft, modern card designs with shadows

## Navigation

### Ribbon Navigation (Top)
- **Home**: Main profile browsing page
- **Services**: Premium features and pricing
- **Contact Us**: Company contact information

### Sidebar
- User profile display (when logged in)
- Advanced filtering options
- Logout button

## Payment Integration

All payments are processed via QR code scanning:
1. User clicks "Express Interest" or service button
2. Registration form appears (first-time users)
3. QR code displayed for payment
4. After payment confirmation, action is completed

## Technical Stack

- **Framework**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Data Storage**: Excel (openpyxl)
- **Image Processing**: Pillow
- **Caching**: Streamlit @st.cache_data decorator

## Performance

- Large dataset (5000+ profiles) loads efficiently
- Caching mechanism for Excel data
- Smooth filtering and sorting
- Lightweight UI rendering

## Troubleshooting

### Application won't start
- Ensure all requirements are installed: `pip install -r requirements.txt`
- Check Python version (3.8+)

### Data not loading
- Verify Excel file path is correct
- Check Excel file has all required columns
- Ensure file is not corrupted

### QR code not showing
- Verify QR.jpg exists in the correct directory
- Check file permissions

## Future Enhancements

- Real payment gateway integration (Razorpay, PayPal)
- Email notifications for expressed interests
- Profile verification system
- Chat functionality
- Video profile support
- Advanced analytics for users
- Mobile app version

## License

This project is created for matrimonial purpose and follows all privacy regulations.

---

**Contact Support**: support@datingpartner.com | +91-9876543210
