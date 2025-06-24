# Library Management System

A comprehensive web-based library management system built with Django, featuring multi-role authentication, room booking, inventory management, and real-time analytics.

## 🚀 Features

### **Multi-Role Authentication System**
- **Admin**: Full system access with user management capabilities
- **Staff**: Library operations and management functions
- **Student**: Book browsing, borrowing, and room booking

### **Core Modules**
- 📚 **Book Management**: Complete CRUD operations with inventory tracking
- 🏢 **Room Management**: Room booking system with calendar integration
- 👥 **User Management**: Role-based access control with profile management
- 📊 **Analytics Dashboard**: Real-time charts and reports with Chart.js
- 🎁 **Donation System**: Track and manage book donations
- ♻️ **Recycling System**: Manage disposal of damaged/outdated books
- 📈 **Reporting**: Comprehensive reports with real database data

## 🛠️ Technology Stack

### **Backend**
- **Django 5.2.1** - Python web framework
- **Python 3.12** - Programming language
- **SQLite** - Primary database
- **Django ORM** - Database abstraction layer

### **Frontend**
- **HTML5** - Markup language
- **CSS3** - Styling and animations
- **JavaScript (ES6+)** - Client-side interactions
- **Bootstrap 5** - Responsive CSS framework
- **Bootstrap Icons** - Icon library
- **Chart.js** - Interactive charts and analytics
- **Font Awesome** - Additional icons

### **Architecture**
- **Django MVT Pattern** - Model-View-Template architecture
- **App-based Structure** - Modular Django applications
- **RESTful URLs** - Clean and semantic URL patterns
- **Signal-based Automation** - Automatic profile creation
- **Context Processors** - Global template data

## 📁 Project Structure

```
library_system/
├── admin_custom/           # Admin interface customization
│   ├── models.py          # Staff model with personal info
│   ├── views.py           # Admin dashboard and user management
│   └── templates/         # Admin-specific templates
├── core/                  # Core application logic
│   ├── models.py          # Main models (Book, Author, Publisher, etc.)
│   ├── views.py           # Core functionality views
│   ├── management/        # Django management commands
│   └── templates/         # Core templates
├── room_management/       # Room booking system
│   ├── models.py          # Room, Booking, Equipment models
│   ├── views.py           # Room operations and analytics
│   └── templates/         # Room management templates
├── student/               # Student portal
│   ├── models.py          # Student-specific models
│   ├── views.py           # Student functionality
│   └── templates/         # Student portal templates
├── library_sys/           # Django project settings
├── static/                # Static files (CSS, JS, images)
├── media/                 # User uploads (book covers, profiles)
├── templates/             # Global templates
│   ├── base.html          # Base template
│   ├── partials/          # Reusable components
│   └── registration/      # Auth templates
└── manage.py              # Django management script
```

## 🗄️ Database Schema

### **Key Models**
- **UserProfile**: Extended user information with role-based access
- **Book**: Complete book information with inventory tracking
- **Author/Publisher/Category**: Book categorization and metadata
- **Room**: Room information with equipment and capacity
- **RoomBooking**: Booking system with approval workflow
- **Donation**: Track donated books with donor information
- **Recycle**: Manage book disposal and recycling

### **Database Files**
- `library_management_clean.sql` - Clean database schema
- `library_management_mysql_workbench.sql` - MySQL Workbench export
- `ER_Diagram.mwb` - Entity-Relationship diagram

## 🚀 Quick Start

### **Prerequisites**
- Python 3.12+
- Django 5.2.1+
- Virtual environment (recommended)

### **Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/LyHeng1090/library-management-system.git
   cd library-management-system
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Load sample data (optional)**
   ```bash
   python manage.py add_study_books
   python manage.py add_rooms_simple
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open browser to `http://127.0.0.1:8000`
   - Admin interface: `http://127.0.0.1:8000/admin/`

## 👤 Default User Roles

### **Admin Access**
- Full system administration
- User management and role assignment
- System analytics and reports
- All CRUD operations

### **Staff Access**
- Book and inventory management
- Room management and bookings
- Donation and recycling operations
- Limited user management

### **Student Access**
- Browse and search books
- Request room bookings
- View personal borrowing history
- Update profile information

## 📊 Key Features in Detail

### **Dashboard Analytics**
- Real-time charts showing:
  - Daily borrowing/returning trends
  - Book category distribution
  - Room utilization rates
  - Monthly system statistics

### **Room Booking System**
- Calendar-based booking interface
- Conflict detection and validation
- Equipment tracking per room
- Maintenance scheduling
- Peak hours analysis

### **Inventory Management**
- Real-time stock tracking
- Book condition monitoring
- Donation workflow
- Recycling and disposal tracking
- Automated inventory alerts

### **Reporting System**
- Monthly trends analysis
- User activity reports
- Room utilization statistics
- Financial tracking (donations, recycling)

## 🔧 Management Commands

The system includes several custom Django management commands:

```bash
python manage.py add_study_books      # Add sample books
python manage.py add_rooms_simple     # Add sample rooms
python manage.py check_registration   # Verify user registration
python manage.py fix_user_profiles    # Fix profile issues
```

## 📱 Responsive Design

- **Mobile-first approach** with Bootstrap 5
- **Responsive navigation** adapting to screen size
- **Touch-friendly interfaces** for mobile devices
- **Progressive enhancement** for better performance

## 🔒 Security Features

- **Role-based access control** (RBAC)
- **CSRF protection** on all forms
- **User session management**
- **Input validation and sanitization**
- **Secure file upload handling**

## 📈 Performance Features

- **Database query optimization** with select_related and prefetch_related
- **Pagination** for large datasets
- **Static file compression** and caching
- **AJAX-powered interactions** for better UX
- **Lazy loading** for images and charts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive CSS framework
- Chart.js for the beautiful analytics charts
- Contributors and testers who helped improve the system

## 📞 Support

For support and questions, please contact the development team or create an issue in the repository.

---

**Built with  using Django and modern web technologies**
