-- https://www.bilibili.com/video/BV1KQ4y1k7km?spm_id_from=333.788.recommend_more_video.3&vd_source=eae2c885960bda71fb3bd248c305cdbf
SELECT a.company, a.Salary
FROM 
    (
    SELECT company, Salary,
    dense_rank() OVER (PARTITION BY company ORDER BY Salary ASC) AS salary_rank,
    COUNT(Salary) OVER (PARTITION BY Company) AS employee_number
    FROM Employee
    ) AS a
WHERE a.salary_rank in (a.employee_number/2, a.employee_number/2+1, a.employee_number/2+0.5)