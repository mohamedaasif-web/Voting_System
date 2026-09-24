import sqlite3
import csv

print("|==================================|")
print("|     Voting System Database       |")
print("|==================================|")

# Database Connect
conn = sqlite3.connect("voting.db")

# Cursor Create
cursor = conn.cursor()

# Create Candidates Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    party TEXT UNIQUE,
    votes INTEGER DEFAULT 0
)
""")

# Create Voters Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS voters(
    aadhar TEXT UNIQUE
)
""")

# Save Database
conn.commit()

# Default Candidates
default_candidates = [
    ("Aasif", "TVK"),
    ("Asan", "DMK"),
    ("Junaith", "ADMK"),
    ("Manoj", "NTK")
]

for name, party in default_candidates:

    cursor.execute(
        "SELECT * FROM candidates WHERE name=?",
        (name,)
    )

    data = cursor.fetchone()

    if data is None:

        cursor.execute(
            "INSERT INTO candidates(name,party,votes) VALUES(?,?,?)",
            (name, party, 0)
        )

conn.commit()


def show_candidates():

    print("\nCandidates List")
    print("-----------------------")

    cursor.execute("SELECT * FROM candidates")

    rows = cursor.fetchall()

    for row in rows:

        print(
            row[0],
            "->",
            row[1],
            "-",
            row[2],
            "| Votes :",
            row[3]
        )


def add_candidate():

    name = input("Enter Candidate Name : ").title().strip()

    while name == "" or name.isdigit():

        print("Invalid Candidate Name!")

        name = input("Enter Candidate Name : ").title().strip()

    party = input("Enter Party Name : ").upper().strip()

    while party == "" or party.isdigit():

        print("Invalid Party Name!")

        party = input("Enter Party Name : ").upper().strip()

    cursor.execute(
        "SELECT * FROM candidates WHERE name=? OR party=?",
        (name, party)
    )

    data = cursor.fetchone()

    if data:

        print("Candidate Already Exists!")
        return

    cursor.execute(
        "INSERT INTO candidates(name,party,votes) VALUES(?,?,?)",
        (name, party, 0)
    )

    conn.commit()

    print("Candidate Added Successfully!")


def update_candidate():

    show_candidates()

    candidate_id = input("Enter Candidate ID : ").strip()

    while candidate_id == "":

        print("ID Cannot Be Empty!")

        candidate_id = input("Enter Candidate ID : ").strip()

    candidate_id = int(candidate_id)

    cursor.execute(
        "SELECT * FROM candidates WHERE id=?",
        (candidate_id,)
    )

    data = cursor.fetchone()

    if data is None:

        print("Candidate Not Found!")
        return

    new_name = input("Enter New Candidate Name : ").title().strip()

    new_party = input("Enter New Party Name : ").upper().strip()

    cursor.execute("""
    UPDATE candidates
    SET name=?, party=?
    WHERE id=?
    """, (new_name, new_party, candidate_id))

    conn.commit()

    print("Candidate Updated Successfully!")


def cast_vote():

    show_candidates()

    aadhar = input("Enter 8 Digit Aadhar Number : ").strip()

    while not aadhar.isdigit() or len(aadhar) != 8:

        print("Invalid Aadhar Number!")

        aadhar = input("Enter 8 Digit Aadhar Number : ").strip()

    # Duplicate Check
    cursor.execute(
        "SELECT * FROM voters WHERE aadhar=?",
        (aadhar,)
    )

    voter = cursor.fetchone()

    if voter:

        print("You Already Voted!")
        return

    candidate_id = input("Enter Candidate ID : ").strip()

    while candidate_id == "":

        print("ID Cannot Be Empty!")

        candidate_id = input("Enter Candidate ID : ").strip()

    candidate_id = int(candidate_id)

    cursor.execute(
        "SELECT * FROM candidates WHERE id=?",
        (candidate_id,)
    )

    candidate = cursor.fetchone()

    if candidate is None:

        print("Candidate Not Found!")
        return

    # Add Vote
    cursor.execute("""
    UPDATE candidates
    SET votes = votes + 1
    WHERE id=?
    """, (candidate_id,))

    # Save Voter
    cursor.execute(
        "INSERT INTO voters(aadhar) VALUES(?)",
        (aadhar,)
    )

    conn.commit()

    print("Vote Added Successfully!")


def count_votes():

    candidate_id = input("Enter Candidate ID : ").strip()

    candidate_id = int(candidate_id)

    cursor.execute(
        "SELECT * FROM candidates WHERE id=?",
        (candidate_id,)
    )

    row = cursor.fetchone()

    if row:

        print(row[1], "-", row[3], "Votes")

    else:

        print("Candidate Not Found!")


def display_winner():

    cursor.execute("""
    SELECT * FROM candidates
    ORDER BY votes DESC
    LIMIT 1
    """)

    winner = cursor.fetchone()

    if winner[3] == 0:

        print("No Votes Yet!")

    else:

        print(
            winner[1],
            "Won With",
            winner[3],
            "Votes"
        )


def show_results():

    print("\nVoting Results")
    print("----------------------")

    cursor.execute("SELECT * FROM candidates")

    rows = cursor.fetchall()

    for row in rows:

        print(
            row[1],
            "-",
            row[2],
            "->",
            row[3],
            "Votes"
        )


def export_csv():

    cursor.execute("SELECT * FROM candidates")

    rows = cursor.fetchall()

    with open("voters.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "Party", "Votes"]
        )

        for row in rows:

            writer.writerow(row)

    print("CSV File Exported Successfully!")


while True:

    print("\n1.Show Candidates")
    print("2.Add Candidate")
    print("3.Update Candidate")
    print("4.Cast Vote")
    print("5.Count Votes")
    print("6.Display Winner")
    print("7.Show Results")
    print("8.Export CSV")
    print("9.Exit")

    choice = input("\nEnter Your Choice : ").strip()

    if choice == "1":

        show_candidates()

    elif choice == "2":

        add_candidate()

    elif choice == "3":

        update_candidate()

    elif choice == "4":

        cast_vote()

    elif choice == "5":

        count_votes()

    elif choice == "6":

        display_winner()

    elif choice == "7":

        show_results()

    elif choice == "8":

        export_csv()

    elif choice == "9":

        print("Thank You!")

        conn.close()

        break

    else:

        print("Invalid Choice!")