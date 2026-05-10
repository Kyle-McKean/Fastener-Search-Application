# Project Overview
In a high-volume retail environment, associates frequently sort and organize fasteners such as bolts and screws. These items are categorized using internal 3-letter codes, but there is no quick reference system to map those codes to product descriptions and storage locations.
To address this inefficiency, I designed and built a mobile-friendly lookup application that allows associates to instantly retrieve fastener details using a simple code input.
________________________________________
## Problem
Associates in the fasteners aisle face several challenges:

•	Time-consuming manual identification of parts 

•	Frequent misplacement of inventory due to unclear mapping 

•	Lack of a centralized, accessible lookup system 

•	Increased cognitive load when handling large volumes of similar items 

This results in slower sorting times and reduced operational efficiency.

## Solution
I developed a lightweight, mobile-accessible web application that:

•	Accepts a 3-letter fastener code as input 

•	Instantly returns product details to accelerate locating shelf positions

•	Is optimized for quick use on a phone in a retail environment 

The solution prioritizes speed, simplicity, and usability over unnecessary complexity.

## Key Features
•	Fast lookup by code with near-instant response time 

•	Clean, mobile-first interface for in-aisle use 

•	Structured backend API for scalable data access 

•	Expandable database design for future enhancements 

# Technical Approach

## Initial Architecture
The application follows a simple full-stack architecture:
•	Frontend: React (mobile-first UI) 

•	Backend: Python (Flask) 

•	Database: SQLite (lightweight and local) 

•	Hosting: Amazon Web Services (S3, CloudFront, Elastic Beanstalk) 
## Data Design
I created a structured dataset of fasteners with the following fields:

•	Code (unique identifier) 

•	Material 

•	Size (inches)

•	Length (inches)

•	Name 

Data was manually collected and standardized to ensure consistency and accuracy.

# Development Process

### Phase 1: Data Collection

•	Collected and documented fastener data directly from the aisle 

•	Standardized naming conventions and location formats

### Phase 2: Local Backend Development

•	Built local API using Flask 

•	Implemented endpoint for code-based lookup 

•	Integrated SQLite database for fast local queries 

### Phase 3: Frontend Development

•	Designed a React interface through Vite

•	Focused on usability in a fast-paced environment 

•	Ensured responsiveness for mobile devices 

### Phase 4: Deployment

•	Deployed frontend via AWS Amplify

•	Modified Backend to deploy API with AWS APIGateway, Lambda, and DynamoDB

•	Tested application in real-world store conditions 

# Challenges and Solutions
### Data Inconsistency
Fastener naming and categorization were not standardized.

#### Solution:

•	Created consistent formatting rules for all entries 

•	Cleaned and normalized dataset manually 

### User Adoption
Associates need tools that are extremely simple.

#### Solution:

•	Focused on a single input and clear output 

•	Avoided unnecessary features in initial version 

### AWS Integration

Initially I attempted to implement the backend using AWS Elastic Beanstalk.

#### Problem:

•	AWS Elastic Beanstalk integration is costly and complex

#### Solution:

•	DynamoDB + Lambda integration is cheaper and simpler

# Results and Impact
•	Reduced lookup time for fasteners significantly 

•	Improved sorting accuracy by providing clear product identification

•	Created a scalable tool that can expand with additional features 

Beyond operational impact, this project demonstrates the ability to:

•	Identify real-world inefficiencies 

•	Design practical, user-centered solutions 

•	Build and deploy full-stack applications 


## Future Enhancements

•	Offline functionality for low connectivity 

•	Image display for visual identification 

•	Admin interface for updating inventory 


# Skills Overview

* **Languages & Frameworks:** Python, TypeScript, React, Flask, SQL, HTML/CSS
* **Cloud & AWS Services:** AWS Amplify, Lambda, API Gateway, DynamoDB, S3, Route 53, Elastic Beanstalk
* **Database & Data Handling:** SQLite, DynamoDB, JSON APIs, pandas
* **Development Skills:** Full-stack development, REST APIs, serverless architecture, responsive UI design
* **Deployment & Debugging:** Cloud deployment, API integration, CORS troubleshooting, environment configuration