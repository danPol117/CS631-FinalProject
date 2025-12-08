INSERT INTO Lab_Member (MID, Name, JoinDate, Mtype, Mentor) VALUES
(1, 'Alice',  '2020-01-15', 'Faculty',     NULL),
(2, 'Bob',    '2021-03-01', 'Faculty',     NULL),
(3, 'Carol',  '2022-08-20', 'Faculty',     NULL),
(4, 'David',  '2023-02-10', 'Faculty',     NULL),
(5, 'Eve',    '2021-09-01', 'Student',     1),
(6, 'Frank',  '2022-01-10', 'Student',     2),
(7, 'Grace',  '2022-05-05', 'Student',     3),
(8, 'Henry',  '2023-09-01', 'Student',     2),
(9, 'Ivy',    '2020-06-01', 'Collaborator',1),
(10,'Jack',   '2021-11-15', 'Collaborator',2),
(11,'Karen',  '2019-04-20', 'Collaborator',3),
(12,'Leo',    '2024-01-12', 'Student',     4);


INSERT INTO Faculty (MID, Department) VALUES
(1, 'CS'),
(2, 'EE'),
(3, 'BIO'),
(4, 'DS');


INSERT INTO Student (MID, SID, Level, Major) VALUES
(5, 1001, 'UG', 'CS'),
(6, 1002, 'GR', 'EE'),
(7, 1003, 'GR', 'BIO'),
(8, 1004, 'UG', 'CS'),
(12,1005, 'GR', 'DS');


INSERT INTO Collaborator (MID, Affiliation, Biography) VALUES
(9,  'TechLab', 'Works on simple AI tools.'),
(10, 'CityLab', 'Helps with testing.'),
(11, 'BioLab',  'Assists with biology work.');


INSERT INTO Grant (GID, SOURCE, BUDGET, StartDate, Duration) VALUES
(101, 1, 50000, '2021-01-01', 12),
(102, 2, 30000, '2021-09-15', 18),
(103, 1, 75000, '2022-03-01', 24),
(104, 3, 20000, '2023-01-10', 12),
(105, 2, 40000, '2023-06-01', 18);

INSERT INTO Project (PID, Title, Sdate, Edate, Eduration, Leader) VALUES
(201, 'Imaging',   '2021-02-01', '2023-01-31', 24, 1),
(202, 'Sensors',   '2021-10-01', '2023-09-30', 24, 2),
(203, 'Genomics',  '2022-04-01', NULL,          36, 3),
(204, 'Robotics',  '2023-02-15', NULL,          30, 2),
(205, 'HealthAI',  '2023-07-01', NULL,          24, 1),
(206, 'Wearables', '2022-09-01', '2024-08-31',  24, 4);


INSERT INTO Equipment (EID, Etype, Ename, Status, pdate) VALUES
(301, 'Scope',  'Microscope',   'OK', '2020-05-10'),
(302, 'Server', 'GPU Server',   'OK', '2021-02-20'),
(303, 'Printer','3D Printer',   'Down', '2021-11-05'),
(304, 'Kit',    'Sensor Kit',   'OK', '2022-03-18'),
(305, 'Robot',  'Lab Robot',    'OK', '2023-01-12'),
(306, 'Seq',    'Sequencer',    'OK', '2022-07-25');


INSERT INTO Publication (PID, Title, Venue, Date, DOI) VALUES
(401, 'Paper A', 'ConfA', '2022-06-15', '10.1/a'),
(402, 'Paper B', 'ConfB', '2023-03-20', '10.1/b'),
(403, 'Paper C', 'ConfC', '2023-09-05', '10.1/c'),
(404, 'Paper D', 'ConfD', '2024-01-10', '10.1/d'),
(405, 'Paper E', 'ConfE', '2024-04-22', '10.1/e'),
(406, 'Paper F', 'ConfF', '2023-11-30', '10.1/f');


INSERT INTO Funds (GID, PID) VALUES
(101, 201),
(101, 202),
(102, 202),
(103, 203),
(103, 206),
(104, 204),
(105, 205),
(105, 206);


INSERT INTO Works (PID, MID, Role, Hours) VALUES
(201, 1, 'PI', 100),
(201, 5, 'RA', 80),
(202, 2, 'PI', 120),
(202, 8, 'RA', 60),
(203, 3, 'PI', 110),
(203, 7, 'RA', 70),
(203, 11,'EXT',50),
(204, 2, 'PI', 90),
(205, 1, 'PI', 95),
(205, 6, 'RA', 85),
(206, 4, 'PI', 100),
(206, 9, 'EXT',60);


INSERT INTO Uses (MID, EID, SDate, Edate, Purpose) VALUES
(5, 301, '2022-01-10','2022-01-12','Imaging'),
(7, 306, '2023-02-05','2023-02-10','Seq'),
(6, 302, '2022-09-01','2022-09-05','Train'),
(3, 306, '2023-06-01','2023-06-05','Seq'),
(8, 304, '2023-10-05','2023-10-06','Test'),
(4, 305, '2023-04-12','2023-04-13','Demo'),
(10,305,'2023-05-01','2023-05-02','Test'),
(9, 303, '2022-04-11','2022-04-12','Print'),
(12,304,'2024-02-01','2024-02-03','Test');


INSERT INTO Publishes (MID, PID, Sdate, Edate, Purpose) VALUES
(1, 401, '2021-09-01','2022-06-15','Write'),
(5, 401, '2021-10-01','2022-06-15','Help'),
(2, 402, '2022-01-05','2023-03-20','Write'),
(8, 402, '2022-03-01','2023-03-20','Help'),
(3, 403, '2022-06-01','2023-09-05','Write'),
(7, 403, '2022-08-01','2023-09-05','Help'),
(4, 404, '2023-03-01','2024-01-10','Write'),
(6, 405, '2023-06-01','2024-04-22','Help'),
(1, 405, '2023-05-01','2024-04-22','Write'),
(12,406,'2023-04-01','2023-11-30','Help'),
(4, 406,'2023-01-15','2023-11-30','Write');
