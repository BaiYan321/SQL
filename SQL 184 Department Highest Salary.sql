-- https://www.bilibili.com/video/BV1ZZ4y1c7YJ/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

SELECT a.Name, a.Salary, d.department
FROM
    (
    SELECT * , dense_rank() OVER (PARTITION BY Department ORDER BY Salary DESC) AS salary_rank
    FROM Employee
    ) AS a
INNER JOIN Department AS d
ON a.DepartmentId = d.Id
WHERE a.salary_rank = 1;

SELECT a.Name, a.highest_salary, d.department
FROM
    (
    SELECT Name, DepartmentId, MAX(Salary)
    FROM Employee
    GROUP BY DepartmentId
    ) AS a
INNER JOIN Department AS d
ON a.DepartmentId = d.Id;