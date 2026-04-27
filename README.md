# Project Overview
In a high-volume retail environment, associates frequently sort and organize fasteners such as bolts and screws. These items are categorized using internal 3-letter codes, but there is no quick reference system to map those codes to product descriptions and storage locations.
To address this inefficiency, I designed and built a mobile-friendly lookup application that allows associates to instantly retrieve fastener details using a simple code input.
________________________________________
# Problem
Associates in the fasteners aisle face several challenges:
•	Time-consuming manual identification of parts 
•	Frequent misplacement of inventory due to unclear mapping 
•	Lack of a centralized, accessible lookup system 
•	Increased cognitive load when handling large volumes of similar items 
This results in slower sorting times and reduced operational efficiency.
________________________________________
# Solution
I developed a lightweight, mobile-accessible web application that:
•	Accepts a 3-letter fastener code as input 
•	Instantly returns product description, category, and location 
•	Is optimized for quick use on a phone in a retail environment 
The solution prioritizes speed, simplicity, and usability over unnecessary complexity.
________________________________________
# Key Features
•	Fast lookup by code with near-instant response time 
•	Clean, mobile-first interface for in-aisle use 
•	Structured backend API for scalable data access 
•	Expandable database design for future enhancements 
________________________________________
# Technical Approach
## Architecture
The application follows a simple full-stack architecture:
•	Frontend: React (mobile-first UI) 
•	Backend: Python (FastAPI) 
•	Database: SQLite (lightweight and local) 
•	Hosting: Amazon Web Services (S3, CloudFront, Elastic Beanstalk) 
## Data Design
I created a structured dataset of fasteners with the following fields:
•	Code (unique identifier) 
•	Description 
•	Category 
•	Size 
•	Location 
Data was manually collected and standardized to ensure consistency and accuracy.
________________________________________
# Development Process
### Phase 1: Data Collection
•	Collected and documented fastener data directly from the aisle 
•	Standardized naming conventions and location formats 
### Phase 2: Backend Development
•	Built REST API using FastAPI 
•	Implemented endpoint for code-based lookup 
•	Integrated SQLite database for fast local queries 
### Phase 3: Frontend Development
•	Designed a simple React interface 
•	Focused on usability in a fast-paced environment 
•	Ensured responsiveness for mobile devices 
### Phase 4: Deployment
•	Deployed frontend via S3 and CloudFront 
•	Deployed backend using Elastic Beanstalk 
•	Tested application in real-world store conditions 
________________________________________
# Challenges and Solutions
## Data Inconsistency
Fastener naming and categorization were not standardized.
Solution:
•	Created consistent formatting rules for all entries 
•	Cleaned and normalized dataset manually 
## User Adoption
Associates need tools that are extremely simple.
Solution:
•	Focused on a single input and clear output 
•	Avoided unnecessary features in initial version 
________________________________________
# Results and Impact
•	Reduced lookup time for fasteners significantly 
•	Improved sorting accuracy by providing clear location mapping 
•	Created a scalable tool that can expand with additional features 
Beyond operational impact, this project demonstrates the ability to:
•	Identify real-world inefficiencies 
•	Design practical, user-centered solutions 
•	Build and deploy full-stack applications 
________________________________________

# Future Enhancements
•	Barcode or QR code scanning 
•	Offline functionality for low connectivity 
•	Image display for visual identification 
•	Admin interface for updating inventory 
•	Migration to a cloud-hosted database 
________________________________________
# Lessons Learned
•	Simplicity is critical for tools used in fast-paced environments 
•	Data quality is as important as application functionality 
•	Real-world constraints (like WiFi and usability) should guide design decisions 
•	Building something practical is far more valuable than theoretical projects 
________________________________________
# Portfolio Value
This project highlights:
•	Full-stack development using React and Python 
•	API design and database modeling 
•	Cloud deployment using AWS 
•	Real-world problem solving in a retail environment 
•	Ability to translate business problems into technical solutions
