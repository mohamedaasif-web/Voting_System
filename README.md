# Voting System

A simple console-based Voting System developed using Python and SQLite. The application manages candidates, voters, voting operations, and election results.

## Technologies Used

* Python
* SQLite
* SQLite3

## Features

* Candidate Management
* Voter Registration
* Voting Process
* Duplicate Vote Prevention
* Vote Counting
* Election Result Calculation
* Winner Identification
* SQLite Database Management

## Project Overview

The Voting System is a Python-based application designed to manage a basic election process. It allows candidates and voters to be managed through a simple console interface and stores voting information using an SQLite database.

## Key Functionalities

### 1. Candidate Management

* Add and manage candidate information.
* Display available candidates.
* Maintain candidate vote counts.

### 2. Voter Management

* Register voters in the system.
* Validate voter information before voting.
* Prevent the same voter from voting more than once.

### 3. Voting Process

* Display available candidates.
* Allow registered voters to cast their vote.
* Store voting information in the SQLite database.

### 4. Election Results

* Calculate the total votes received by each candidate.
* Display candidate-wise voting results.
* Identify the candidate with the highest number of votes.

## Database

The project uses **SQLite** for storing application data.

The database is used to manage:

* Voter information
* Candidate information
* Voting records

## How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/mohamedaasif-web/Voting_System.git
```

### Step 2: Open the Project Folder

```bash
cd Voting_System
```

### Step 3: Run the Python Program

```bash
python voting_system.py
```

## Project Structure

```text
Voting_System/
│
├── voting_system.py
└── README.md
```

## Learning Outcomes

Through this project, I practiced:

* Python programming
* Functions and conditional statements
* Database connectivity using SQLite
* CRUD operations
* Input validation
* Basic voting logic
* Database-driven application development

## Future Enhancements

* Develop a graphical user interface.
* Add admin authentication.
* Generate detailed election reports.
* Add data export functionality.
* Improve database security and validation.

## Author

**S. Mohamed Aasif**

Full Stack Developer

## GitHub

https://github.com/mohamedaasif-web/Voting_System
