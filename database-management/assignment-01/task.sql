-- Active: 1794030384000@@127.0.0.1@3306@test
CREATE TABLE student(
    id CHAR(6) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE,
    age INT, 
    CONSTRAINT check_age CHECK(age > 18)
);

CREATE TABLE library(
    book_id CHAR(6) PRIMARY KEY,
    book_name VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    student_id CHAR(6),
    CONSTRAINT fk_library_student FOREIGN KEY(student_id) REFERENCES student(id)
);

CREATE TABLE fees(
    fee_id CHAR(6) PRIMARY KEY,
    amount INT NOT NULL,
    student_id CHAR(6),
    CONSTRAINT fk_fees_student FOREIGN KEY(student_id) REFERENCES student(id)
)

INSERT INTO student (id, name, email, age) VALUES
('S00001', 'Alice Johnson', 'alice@example.com', 20),
('S00002', 'Bob Smith', 'bob@example.com', 22),
('S00003', 'Charlie Brown', 'charlie@example.com', 19);



INSERT INTO library (book_id, book_name, author, student_id) VALUES
('B00001', 'Introduction to SQL', 'John Doe', 'S00001'),
('B00002', 'Database Systems', 'Jane Smith', 'S00002'),
('B00003', 'Algorithms Unlocked', 'Thomas Cormen', NULL);

INSERT INTO fees (fee_id, amount, student_id) VALUES
('F00001', 500, 'S00001'),
('F00002', 750, 'S00002'),
('F00003', 300, 'S00001');


SELECT * from library;