-- 코드를 입력하세요
SELECT T2.AUTHOR_ID, AUTHOR.AUTHOR_NAME, T2.CATEGORY, SUM(T2.PRICE * T2.SALES) AS TOTAL_SALES
FROM 
(
SELECT B.BOOK_ID, B.CATEGORY, B.AUTHOR_ID, B.PRICE, T1.SALES
FROM BOOK B JOIN
(SELECT BOOK_ID, SALES
FROM BOOK_SALES
WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 1) T1
ON B.BOOK_ID = T1.BOOK_ID) T2 JOIN AUTHOR
ON AUTHOR.AUTHOR_ID = T2.AUTHOR_ID
GROUP BY AUTHOR.AUTHOR_NAME, T2.CATEGORY
ORDER BY T2.AUTHOR_ID, T2.CATEGORY DESC