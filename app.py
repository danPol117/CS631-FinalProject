import sqlite3
from pathlib import Path
from unittest import case

DB_PATH = Path(__file__).with_name("research_lab.db")

def get_connection_and_cursor():
    #Create connection to DB file
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  
    """Description of what the line right above this does
    
    Basically, it allows us to access the whatever the query fetches by col name 

    Without this line, it would return tuples like (0,Daniel,...,...,...), and we would have to access the cols 
    using things like row[0], row[1], which is annoying since you have to memorize positions

    With this line, queries return dicts like this {'member_id': 0, 'name': 'Daniel'}, and allows us 
    to access data like so row["name"] and so on, which is better
    """
    curs=conn.cursor()
    return conn, curs

def list_members():
    conn, cur = get_connection_and_cursor()
    cur.execute("SELECT * FROM Lab_Member")
    rows = cur.fetchall()
    for row in rows:
        print(dict(row))

def menu():
    print("\n1. Project and Member Management")
    print("2. Equipment Usage Tracking")
    print("3. Grant and Publication Reporting")
    print("4. Exit")
    choice = input("Enter choice: ")
    match choice:
        case "1":
            print("Project and Member Management selected")
            management_menu()
        case "2":
            print("Equipment Usage Tracking selected")
            equipment_menu()
        case "3":
            print("Grant and Publication Reporting selected")
            reporting_menu()
        case "4":
            print("Exiting...")
            return  
        case _:
            print("Invalid choice")
            menu()
            return
    

    """
    1. PROJECT AND MEMBER MANAGEMENT
    ✔ Query, add, update, and remove members and projects.
    ✔ Display the status of a project.
    ✔ Show members who have worked on projects funded by a given grant.
    ✔ Show mentorship relations among members who have worked on the same project.
    """
def management_menu():  # sourcery skip: extract-duplicate-method, extract-method
    print("1. Query Members")
    print("2. Add Member")
    print("3. Update Member")
    print("4. Remove Member")
    print("5. Query Projects")
    print("6. Add Project")
    print("7. Update Project")
    print("8. Remove Project")
    print("9. display status")
    print("10. Show members by grant")
    print("11. show mentorship relations")
    print("12. Back to Main Menu")
    choice = input("Enter choice: ")
    match choice:
        case "1":
            conn, cur = get_connection_and_cursor()
            cur.execute("SELECT * FROM Lab_Member")
            rows = cur.fetchall()
            for row in rows:
                print(dict(row))
            conn.close()
        case "2":
            conn, cur = get_connection_and_cursor()
            member_id = input("Enter member id: ")
            name = input("Enter name: ")
            join_date = input("Enter join date: ")
            member_type = input("Enter member type: ")
            mentor_id_input = input("Enter mentor id (or NULL): ")
            mentor_id = None if mentor_id_input.upper() == "NULL" else mentor_id_input
            cur.execute("INSERT INTO Lab_Member VALUES (?, ?, ?, ?, ?)", 
                        (member_id, name, join_date, member_type, mentor_id))
            conn.commit()
            conn.close()
        case "3":
            conn, cur = get_connection_and_cursor()
            member_id = input("Enter member id to update: ")
            name = input("Enter new name: ")
            join_date = input("Enter new join date: ")
            member_type = input("Enter new member type: ")
            mentor_id_input = input("Enter new mentor id (or NULL): ")
            mentor_id = None if mentor_id_input.upper() == "NULL" else mentor_id_input
            cur.execute("UPDATE Lab_Member SET Name=?, JoinDate=?, Mtype=?, mentor=? WHERE MID=?", 
                        (name, join_date, member_type, mentor_id, member_id))
            conn.commit()
            conn.close()
        case "4":
            conn, cur = get_connection_and_cursor()
            member_id = input("Enter member id to remove: ")
            cur.execute("DELETE FROM Lab_Member WHERE Mid=?", (member_id,))
            conn.commit()
            conn.close()
        case "5":
            conn, cur = get_connection_and_cursor()
            cur.execute("SELECT * FROM Project")
            rows = cur.fetchall()
            for row in rows:
                print(dict(row))
            conn.close()
        case "6":
            conn, cur = get_connection_and_cursor()
            project_id = input("Enter project id: ")
            title = input("Enter title: ")
            start_date = input("Enter start date: ")
            end_date_input = input("Enter end date (or NULL): ")
            end_date = None if end_date_input.upper() == "NULL" else end_date_input
            duration = input("Enter duration: ")
            leader_id = input("Enter leader id: ")
            cur.execute("INSERT INTO Project VALUES (?, ?, ?, ?, ?, ?)", 
                        (project_id, title, start_date, end_date, duration, leader_id))
            conn.commit()
            conn.close()
        case "7":
            conn, cur = get_connection_and_cursor()
            project_id = input("Enter project id to update: ")
            title = input("Enter new title: ")
            start_date = input("Enter new start date: ")
            end_date_input = input("Enter new end date (or NULL): ")
            end_date = None if end_date_input.upper() == "NULL" else end_date_input
            duration = input("Enter new duration: ")
            leader_id = input("Enter new leader id: ")
            cur.execute("UPDATE Project SET Title=?, Sdate=?, Edate=?, EDuration=?, Leader=? WHERE PID=?", 
                        (title, start_date, end_date, duration, leader_id, project_id))
            conn.commit()
            conn.close()
        case "8":
            conn, cur = get_connection_and_cursor()
            project_id = input("Enter project id to remove: ")
            cur.execute("DELETE FROM Project WHERE PID=?", (project_id,))
            conn.commit()
            conn.close()
        case "9":
            conn, cur = get_connection_and_cursor()
            #project_id = input("Enter Project id: ")
            cur.execute("SELECT PID, Title, CASE WHEN date(Sdate) > date('now') THEN 'Planned' WHEN Edate IS NULL OR date(Edate) >= date('now') THEN 'Ongoing' ELSE 'Completed' END AS Status FROM Project;")
            rows = cur.fetchall()
            for row in rows:
                print(dict(row))
            conn.close()
        case "10":
            conn, cur = get_connection_and_cursor()
            grant_id = input("Enter Grant id: ")
            cur.execute("SELECT * FROM Lab_Member WHERE MID IN (SELECT MID FROM Works WHERE PID IN (SELECT PID FROM Funds WHERE GID = ?))", (grant_id,))
            rows = cur.fetchall()
            for row in rows:
                print(dict(row))
            conn.close()
        case "11":
            conn, cur = get_connection_and_cursor()
            cur.execute("SELECT lm1.Name AS Mentee, lm2.Name AS Mentor FROM Lab_Member lm1 JOIN Lab_Member lm2  ON lm1.Mentor = lm2.MID WHERE lm1.MID IN (SELECT DISTINCT w1.MID FROM Works w1 JOIN Works w2 ON w1.PID = w2.PID WHERE w1.MID <> w2.MID);")
            rows = cur.fetchall()
            for row in rows:
                print(dict(row))
            conn.close()
        case "12":
            menu()
            return
        case _:
            print("Invalid choice")
            management_menu()
    menu()

    """
    2. EQUIPEMENT USAGE TRACKING
    • Query, add, update, and remove equipment and equipment usage.
    • Show status of a piece of equipment
    • Show members currently using a given piece of equipment and the projects they are working on.
    """
def equipment_menu():
    print("1. Query Equipment")
    print("2. Add Equipment")
    print("3. Update Equipment")
    print("4. Remove Equipment")
    print("5. Show Equipment Status")
    print("6. Show Members Using Equipment")
    print("7. Back to Main Menu")
    choice = input("Enter choice: ")

    match choice:
        case "1":
            # Query all equipment
            conn, cur = get_connection_and_cursor()
            cur.execute("SELECT * FROM Equipment")
            rows = cur.fetchall()
            for row in rows:
                print(dict(row))
            conn.close()

        case "2":
            # Add new equipment
            conn, cur = get_connection_and_cursor()
            eid = input("Enter equipment id: ")
            etype = input("Enter equipment type: ")
            ename = input("Enter equipment name: ")
            status = input("Enter status (OK/Down): ")
            pdate = input("Enter purchase date: ")

            cur.execute(
                "INSERT INTO Equipment VALUES (?, ?, ?, ?, ?)",
                (eid, etype, ename, status, pdate)
            )
            conn.commit()
            conn.close()

        case "3":
            # Update equipment
            conn, cur = get_connection_and_cursor()
            eid = input("Enter equipment id to update: ")
            etype = input("Enter new type: ")
            ename = input("Enter new name: ")
            status = input("Enter new status: ")
            pdate = input("Enter new purchase date: ")

            cur.execute(
                "UPDATE Equipment SET Etype=?, Ename=?, Status=?, pdate=? WHERE EID=?",
                (etype, ename, status, pdate, eid)
            )
            conn.commit()
            conn.close()

        case "4":
            # Remove equipment
            conn, cur = get_connection_and_cursor()
            eid = input("Enter equipment id to remove: ")
            cur.execute("DELETE FROM Equipment WHERE EID=?", (eid,))
            conn.commit()
            conn.close()

        case "5":
            # Show equipment status
            conn, cur = get_connection_and_cursor()
            eid = input("Enter equipment id: ")

            cur.execute("SELECT EID, Ename, Status FROM Equipment WHERE EID=?", (eid,))
            row = cur.fetchone()
            if row:
                print(dict(row))
            else:
                print("Equipment not found.")
            conn.close()

        case "6":
            # Show members currently using a piece of equipment AND their projects
            conn, cur = get_connection_and_cursor()
            eid = input("Enter equipment id: ")

            query = """
            SELECT 
                lm.Name AS Member,
                u.SDate AS Start,
                u.EDate AS End,
                p.Title AS Project
            FROM Uses u
            JOIN Lab_Member lm ON u.MID = lm.MID
            LEFT JOIN Works w ON lm.MID = w.MID
            LEFT JOIN Project p ON w.PID = p.PID
            WHERE u.EID = ?
            """
            cur.execute(query, (eid,))
            rows = cur.fetchall()

            if not rows:
                print("No members are using this equipment.")
            else:
                for row in rows:
                    print(dict(row))

            conn.close()

        case "7":
            menu()
            return

        case _:
            print("Invalid choice")
            equipment_menu()
            return
    menu()


    """
    3. GRANT AND PUBLICATION REPORTING.
    • Identify the name of the member(s) with the highest number of publications.
    • Calculate the average number of student publications per major.
    • Find the number of projects that were funded by a grant and were active during a given period of time.
    • Find the three most prolific members who have worked on a project funded by a given grant.
    """
def reporting_menu():
    print("1. Highest Number of Publications")
    print("2. Average Number of Student Publications per Major")
    print("3. Number of Projects Funded by Grant in Given Period")
    print("4. Three Most Prolific Members for Given Grant")
    print("5. Back to Main Menu")
    choice = input("Enter choice: ")
    match choice:
        case "1":
            conn, cur = get_connection_and_cursor()
            cur.execute("""
                SELECT lm.Name, COUNT(pu.PID) AS PubCount
                FROM Lab_Member lm
                JOIN Publishes pu ON lm.MID = pu.MID
                GROUP BY lm.MID
                HAVING PubCount = (
                    SELECT MAX(cnt)
                    FROM (SELECT COUNT(*) AS cnt FROM Publishes GROUP BY MID)
                )
            """)
            for row in cur.fetchall():
                print(dict(row))
            conn.close()

        case "2":
            conn, cur = get_connection_and_cursor()
            cur.execute("""
                SELECT sub.Major, AVG(pubcount) AS AvgPubs
                FROM (
                    SELECT s.Major AS Major, COUNT(pu.PID) AS pubcount
                    FROM Student s
                    LEFT JOIN Publishes pu ON s.MID = pu.MID
                    GROUP BY s.MID
                ) sub
                GROUP BY sub.Major
            """)
            for row in cur.fetchall():
                print(dict(row))
            conn.close()

        case "3":
            conn, cur = get_connection_and_cursor()
            gid = input("Enter grant id: ")
            start = input("Enter start date: ")
            end = input("Enter end date: ")
            cur.execute("""
                SELECT COUNT(*) AS ActiveProjectCount
                FROM Project p
                JOIN Funds f ON p.PID = f.PID
                WHERE f.GID = ?
                AND p.Sdate <= date(?)
                AND (p.Edate IS NULL OR p.Edate >= date(?))
            """, (gid, end, start))
            for row in cur.fetchall():
                print(dict(row))
            conn.close()

        case "4":
            conn, cur = get_connection_and_cursor()
            gid = input("Enter grant id: ")
            cur.execute("""
                SELECT lm.Name, COUNT(pu.PID) AS PubCount
                FROM Funds f
                JOIN Works w ON f.PID = w.PID
                JOIN Lab_Member lm ON w.MID = lm.MID
                LEFT JOIN Publishes pu ON lm.MID = pu.MID
                WHERE f.GID = ?
                GROUP BY lm.MID
                ORDER BY PubCount DESC
                LIMIT 3
            """, (gid,))
            for row in cur.fetchall():
                print(dict(row))
            conn.close()

        case "5":
            menu()
            return
        case _:
            print("Invalid choice")
            reporting_menu()
    menu()


if __name__ == "__main__":
    menu()
    #list_members()
    
