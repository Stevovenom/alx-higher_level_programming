-- Describes the named DATABASE
SELECT column_name, column_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0'
AND table_name = 'first_table';
