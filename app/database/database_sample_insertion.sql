
-- Sample data insertion
INSERT INTO Department (dept_name) VALUES 
('Computer Science'),
('Mathematics'),
('Physics'),
('Chemistry');

INSERT INTO Administrator (username, password) VALUES 
('admin', 'admin123');

INSERT INTO Teacher (username, password, office_hour, office_no) VALUES 
('teacher1', 'teacher123', 'Mon-Wed 10:00-12:00', 'A101'),
('teacher2', 'teacher123', 'Tue-Thu 14:00-16:00', 'B202');

INSERT INTO Student (student_id, username, password, department_id) VALUES 
(64220006, 'student1', 'student123', 1),
(64210004, 'student2', 'student123', 2);

INSERT INTO Lecture (lecture_name, department_id) VALUES 
('Data Structures', 1),
('Calculus I', 2),
('Physics I', 3),
('General Chemistry', 4);

INSERT INTO teach (teacher_id, lecture_id) VALUES 
(1, 1),
(1, 2),
(2, 3),
(2, 4);

INSERT INTO take (student_id, lecture_id, pass_grade) VALUES 
(1, 1, 85.5),
(1, 2, 92.0),
(2, 2, 78.5),
(2, 3, 88.0);
