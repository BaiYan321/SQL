-- https://www.bilibili.com/video/BV1Xa4y1n7Dh/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        SELECT max(a.Salary)
        FROM
            (SELECT Distinct Salary
            FROM Employee
            ORDER BY Salary DESC
            LIMIT 1 OFFSET(N-1) AS a)
    );
END