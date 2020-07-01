# Write your MySQL query statement below
" select w1.Id from Weather w1, Weather w2 where DATE_SUB(w1.RecordDate, INTERVAL 1 DAY) = w2.RecordDate and w1.Temperature > w2.Temperature "