Drop Table IF EXISTS Grant;
DROP TABLE IF EXISTS Funds;
DROP TABLE IF EXISTS Project;
DROP TABLE IF EXISTS Works;
DROP TABLE IF EXISTS Lab_Member;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Collaborator;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Uses;
DROP TABLE IF EXISTS Equipment;
DROP TABLE IF EXISTS Publishes;
DROP TABLE IF EXISTS Publication;

CREATE Table Grant (
    GID     INTEGER PRIMARY KEY,
    SOURCE     INTEGER,
    BUDGET     REAL,
    StartDate  DATE,
    Duration   INTEGER,
);

Create Table Funds (
    GID     INTEGER PRIMARY KEY,
    PID    INTEGER PRIMARY KEY,
    FOREIGN Key GID REFERENCES Grant(GID),
    FOREIGN Key PID REFERENCES Project(PID)
)

Create Table Project (
    PID     INTEGER PRIMARY KEY,
    Title     TEXT NOT NULL,
    Sdate   DATE NOT NULL,
    Edate   DATE,
    Eduration INTEGER,
    Leader  INTEGER,
    FOREIGN KEY (Leader) REFERENCES Faculty(MID)
);

Create Table Works(
    PID    INTEGER PRIMARY KEY,
    MID    INTEGER PRIMARY KEY,
    Role   TEXT,
    Hours INTEGER,
    FOREIGN KEY (PID) REFERENCES Project(PID),
    FOREIGN KEY (MID) REFERENCES Lab_Member(MID)
)

CREATE TABLE Lab_Member (
    MID   INTEGER PRIMARY KEY,
    Name        TEXT NOT NULL,
    JoinDate    DATE,
    Mtype       TEXT,
    Mentor     INTEGER,
    FOREIGN KEY (Mentor) REFERENCES Lab_Member(MID)
);

Create Table Student (
    MID     INTEGER PRIMARY KEY,
    SID     INTEGER NOT NULL,
    Level  TEXT,
    Major  TEXT,
    FOREIGN KEY (MID) REFERENCES Lab_Member(MID)
);

Create Table Collaborator (
    MID     INTEGER PRIMARY KEY,
    Affiliation  TEXT,
    Biography    TEXT,
    FOREIGN KEY (MID) REFERENCES Lab_Member(MID)
);

Create Table Faculty (
    MID     INTEGER PRIMARY KEY,
    Department   TEXT,
    FOREIGN KEY (MID) REFERENCES Lab_Member(MID)
);

Create Table Uses (
    MID     INTEGER PRIMARY KEY,
    EID     INTEGER PRIMARY KEY,
    SDate  DATE NOT NULL,
    Edate  DATE,
    Purpose TEXT,
    FOREIGN KEY (MID) REFERENCES Lab_Member(MID),
    FOREIGN KEY (EID) REFERENCES Equipment(EID)
);

Create Table Equipment (
    EID     INTEGER PRIMARY KEY,
    Etype    TEXT NOT NULL,
    Ename   TEXT NOT NULL,
    Status  TEXT NOT NULL
    pdate DATE
);

Create Table Publishes (
    MID    INTEGER PRIMARY KEY,
    PID    INTEGER PRIMARY KEY,
    Sdate  DATE NOT NULL,
    Edate  DATE,
    Purpose TEXT,
    FOREIGN KEY (MID) REFERENCES Lab_Member(MID),
    FOREIGN KEY (PID) REFERENCES Publication(PID)
);

Create Table Publication (
    PID     INTEGER PRIMARY KEY,
    Title     TEXT NOT NULL,
    Venue   TEXT,
    Date   DATE NOT NULL,
    DOI    TEXT
);
