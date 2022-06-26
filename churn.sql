-- test 
select * from churn;

-- examine country
select "Country",count("Country") from churn
GROUP BY "Country";

-- all data is in the US

--examine states
select "State", count("State") from churn
GROUP BY "State";

-- all data is localised to Californa


-- we will examine where in Californa the data is collected from
select "City", count("City") from churn
GROUP BY "City";

-- data is spread across 1129 cities 


-- EXAMINING GENDER
-- gender counts
select "Gender" ,count("Gender") from churn 
GROUP BY "Gender";
-- we have a fairly even distribution of gender 

-- age breakdown of gender
select "Gender" ,count("Senior Citizen") from churn 
GROUP BY "Gender", "Senior Citizen";
-- roughly 14% of each gender is Senior Citizen

-- relationship status 
select "Gender" ,count("Partner") from churn 
GROUP BY "Gender", "Partner";
-- fairly even breakdown of partner status  

-- which gender is more likely to churn 
SELECT "Gender", AVG("Churn Score") from churn
group by "Gender";
-- Both have an average score of 58.7 , meaning gender alone doesnt provide insight into churn prediction 

-- CHURN EXAMINATION 

-- CHURN VS loyal customer profile
-- what is the churn rate? percentage using window function
 SELECT DISTINCT "Churn Value",
        ROUND(100.00*(count(*) over (partition by "Churn Value") / count(*) over ()::numeric),2)
   FROM churn
   ORDER BY "Churn Value";

-- Tenure
select "Churn Value", ROUND(AVG("Tenure Months"),0)
FROM CHURN 
GROUP BY "Churn Value";
-- loyal 38, churn 18

--Spending
select "Churn Value", ROUND(AVG("Monthly Charges")::numeric,2)
FROM CHURN 
GROUP BY "Churn Value";
-- loyal 61, churn 74 

-- revenue by group 
select "Churn Value", ROUND(SUM("Monthly Charges")::numeric,2)
FROM CHURN 
GROUP BY "Churn Value";


-- which gender is more likely to churn 
SELECT "Gender", AVG("Churn Score") from churn
group by "Gender";
-- Both have an average score of 58.7 , meaning gender alone doesnt provide insight into churn prediction 

-- are older or younger people more likely to churn
SELECT "Senior Citizen", AVG("Churn Score") from churn
group by "Senior Citizen";
-- older people are more likely to churn

-- does location affect churn rate 
SELECT "City", AVG("Churn Score") as churn_score from churn
group by "City"
ORDER BY churn_score DESC
LIMIT 20;

-- 10 point churn difference between place 1 and 20 indicting churn may be affected by location
-- however we must also consider that many of the cities have small samples sizes and thus probably shouldnt draw too 
-- many concluesions from the score difference 


-- does dependants affect churn rate
SELECT "Dependents", AVG("Churn Score") as churn_score from churn
group by "Dependents"
ORDER BY churn_score DESC;

-- suprisingly people without dependants are more likely to churn 


-- contract view
SELECT "Churn Label", "Contract",count("Churn Value")
from churn 
group by "Churn Label","Contract"
order by "Contract";

-- payment method view
SELECT "Churn Label", "Payment Method",count("Churn Value")
from churn 
group by "Churn Label","Payment Method"
order by "Payment Method", "Churn Label" DESC;