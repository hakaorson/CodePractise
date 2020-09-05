CREATE TABLE Student (
    sid int PRIMARY KEY,
    sname CHAR(10),
    age int,
    gender int
);

CREATE TABLE Teacher (tid int PRIMARY KEY, tname CHAR(10));

CREATE TABLE Course (
    cid int PRIMARY KEY,
    cname CHAR(10),
    tid int,
    FOREIGN KEY (tid) REFERENCES Teacher (tid)
);

CREATE TABLE Student_Course_score (
    sid int,
    cid int,
    FOREIGN KEY (sid) REFERENCES Student (sid),
    FOREIGN KEY (cid) REFERENCES Course (cid),
    score int
);

INSERT INTO
    Teacher
VALUES
    (1, "A老师"),
    (2, "B老师"),
    (3, "C老师");

INSERT INTO
    Student
VALUES
    (1, "张三", 10, 1),
    (2, "李四", 15, 2),
    (3, "王五", 20, 1),
    (1032, "xx", 70, 2);

INSERT INTO
    Course
VALUES
    (1, "数学课", 1),
    (2, "语文课", 2),
    (3, "历史课", 1),
    (4, "aa", 3);

INSERT INTO
    Student_Course_score
VALUES
    (1, 1, 100),
    (1, 3, 70),
    (2, 2, 60),
    (2, 3, 80),
    (3, 2, 34),
    (1032, 1, 100),
    (1032, 3, 100),
    (1032, 4, 100);