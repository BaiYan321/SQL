-- https://www.bilibili.com/video/BV1KQ4y1k7km?spm_id_from=333.788.recommend_more_video.3&vd_source=eae2c885960bda71fb3bd248c305cdbf

-- Method 1
SELECT Employee.Name
FROM (
    SELECT ManagerId
    FROM Employee
    GROUP BY ManagerId
    HAVING COUNT(ManagerId) >4
    ) a
LEFT JOIN Employee
ON a.ManagerId = Employee.Id

-- Method 2
SELECT Name
FROM Employee
WHERE Id in (
    SELECT ManagerId
    FROM Employee
    GROUP BY ManagerId
    HAVING COUNT(ManagerId) >4
    )