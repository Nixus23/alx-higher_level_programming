-- script lists all records in second_table doesn't list records without a name value
SELECT score, name FROM second_table WHERE name is not NULL ORDER BY score DESC;
