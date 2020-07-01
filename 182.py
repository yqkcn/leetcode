# Write your MySQL query statement below
" select t.Email as Email from (select Email, count(Email) as num from Person group by Email) t where t.num > 1 "