# Alter table:
ALTER TABLE students ADD COLUMN email VARCHAR(100) 
ALTER TABLE students MODIFY COLUMN score DECIMAL(6, 2)
ALTER TABLE students DROP COLUMN email

# Update table
UPDATE students SET score = 88.5 WHERE student_id = 1

# Order by
SELECT * FROM students ORDER BY name ASC
SELECT * FROM students ORDER BY score DESC

# delete
DELETE from students WHERE grade = "C"

# group by
SELECT grade, MIN(score) FROM students GROUP BY grade
SELECT grade, MAX(score) FROM students GROUP BY grade
select grade, SUM(score) FROM students GROUP BY grade
SELECT grade, AVG(score) FROM students GROUP BY grade
