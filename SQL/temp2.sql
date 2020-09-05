-- SELECT distinct
--     r.sid
-- FROM
--     Student_Course_score l
--     INNER JOIN Student_Course_score r ON l.cid = r.cid
-- WHERE l.sid = 1032 AND r.sid !=1032
-- SELECT
--     *
-- FROM
--     Student_Course_score
-- WHERE
--     cid IN (
--         SELECT
--             distinct c.cid
--         FROM
--             Teacher t
--             INNER JOIN Course c ON t.tid = c.tid
--         WHERE
--             t.tname = "A老师"
--     );
SELECT
    sid,
    AVG(score) as avg
FROM
    Student_Course_score
WHERE
    score < 90
GROUP BY
    sid;