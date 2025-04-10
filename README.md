

---

```markdown
# University Dispensary Management System

## Project Overview
The University Dispensary Management System (UDMS) is a comprehensive web application designed to manage university medical facilities, including patients, doctors, appointments, medicines, and prescriptions. This system allows for efficient management and retrieval of essential healthcare data, enhancing the operational efficiency of university dispensaries.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd university-dispensary-management-system
   ```

2. **Install Python Dependencies**
   Ensure you have Python and pip installed, then install the required libraries:
   ```bash
   pip install Flask flask-cors mysql-connector-python
   ```

3. **Set Up MySQL Database**
   Create a MySQL database named `university_dispancery_management_system`. Ensure the following user credentials are configured:
   - Host: `localhost`
   - User: `root`
   - Password: `root`

   Additionally, create the necessary tables based on your application requirements for patients, doctors, appointments, medicines, and prescriptions.

4. **Run the Flask Application**
   Start the application using:
   ```bash
   python app.py
   ```

5. **Access the Application**
   Open your browser and navigate to `http://localhost:8000/` to access the application.

## Usage
The application provides various endpoints to retrieve data:
- **GET /api/patients**: Retrieve a list of all patients.
- **GET /api/doctors**: Retrieve a list of all doctors.
- **GET /api/appointments**: Retrieve a list of all appointments.
- **GET /api/medicines**: Retrieve a list of all medicines.
- **GET /api/prescriptions**: Retrieve all prescriptions.

The front-end is built using HTML and leverages Tailwind CSS for styles and Font Awesome for icons.

## Features
- Dashboard overview with total counts for patients, doctors, and appointments.
- Individual pages for managing and viewing patients, doctors, appointments, medicines, and prescriptions.
- Search functionality across all records for easy access.
- Conditional styling based on medicine stock levels.

## Dependencies
The following dependencies are required for the project, as specified in the `requirements.txt` or directly installed:
- Flask
- Flask-CORS
- mysql-connector-python

## Project Structure
```
university-dispensary-management-system/
│
├── app.py                           # Main application file
├── index.html                       # Dashboard home page
├── patients.html                    # Patient records page
├── doctors.html                     # Doctors directory page
├── appointments.html                # Appointments schedule page
├── medicines.html                   # Medicine inventory page
└── prescriptions.html                # Prescription records page
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any features or bug fixes.

## Acknowledgments
- Special thanks to the contributors and libraries used in this project.

---
For additional information or questions, please open an issue on the project's GitHub repository.
```
