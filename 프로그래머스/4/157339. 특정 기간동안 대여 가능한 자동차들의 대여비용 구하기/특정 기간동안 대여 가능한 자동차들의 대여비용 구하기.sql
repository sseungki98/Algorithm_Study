# SELECT T4.CAR_ID, T4.CAR_TYPE, CEILING(T4.DAILY_FEE * 30 * (100-T3.DISCOUNT_RATE) / 100) AS FEE
# FROM
# (SELECT CRCDP.CAR_TYPE, CRCDP.DISCOUNT_RATE
# FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN CRCDP
# WHERE CRCDP.DURATION_TYPE = '30일 이상') T3 # 할인에서 30일 이상인 애들만
# JOIN
# (SELECT DISTINCT T1.CAR_ID, T1.CAR_TYPE, T1.DAILY_FEE
# FROM
# (SELECT *
# FROM CAR_RENTAL_COMPANY_CAR CRCR
# WHERE CRCR.CAR_TYPE IN ('세단','SUV')) T1 # 세단, SUV인 차들
# JOIN
# (SELECT CRCRH.CAR_ID
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY CRCRH
# WHERE CRCRH.START_DATE <= '2022-11-30' AND CRCRH.END_DATE >= '2022-11-01') T2 # 렌탈 히스토리 그냥 왜 엮은거지 ?
# ON T1.CAR_ID = T2.CAR_ID
# WHERE T2.START_DATE <= '2022-11-30' AND T2.END_DATE >= '2022-11-01') T4 # 2022-11-01 ~ 2022-11-30에 빌린애들
# ON T3.CAR_TYPE NOT IN T4.CAR_TYPE
# WHERE CEILING(T4.DAILY_FEE * 30 * (100-T3.DISCOUNT_RATE) / 100) >= 500000 AND CEILING(T4.DAILY_FEE * 30 * (100-T3.DISCOUNT_RATE) / 100) < 2000000
# ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC

SELECT CRCC.CAR_ID, CRCC.CAR_TYPE, ROUND(CRCC.DAILY_FEE * 30 * (100 - T1.DISCOUNT_RATE) / 100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR CRCC JOIN (
    SELECT CAR_TYPE, DISCOUNT_RATE
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN CRCDP
    WHERE CRCDP.DURATION_TYPE = '30일 이상' AND CRCDP.CAR_TYPE IN ('세단','SUV')
) T1 ON CRCC.CAR_TYPE = T1.CAR_TYPE
WHERE CRCC.CAR_ID NOT IN (
SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY CRCRH
WHERE CRCRH.START_DATE <= '2022-11-30' AND CRCRH.END_DATE >= '2022-11-01'
) AND (CRCC.DAILY_FEE * 30 * (100 - T1.DISCOUNT_RATE) / 100) >= 500000 AND (CRCC.DAILY_FEE * 30 * (100 - T1.DISCOUNT_RATE) / 100) < 2000000
ORDER BY FEE DESC, CRCC.CAR_TYPE, CRCC.CAR_ID DESC