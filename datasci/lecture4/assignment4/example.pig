register s3n://uw-cse344-code/myudfs.jar


-- load the test file into Pig
raw = LOAD 's3n://uw-cse344-test/btc-2010-chunk-000' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse344/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by object column
objects = group ntriples by (object);

-- flatten the objects out (because group by produces a tuple of each object
-- in the first column, and we want each object ot be a string, not a tuple),
-- and count the number of tuples associated with each object
count_by_object = foreach objects generate flatten($0), COUNT($1) as count;

--order the resulting tuples by their count in descending order
count_by_object_ordered = order count_by_object by count desc;

-- store the results in the folder /user/hadoop/example-results
store count_by_object_ordered into '/user/hadoop/example-results' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_object_ordered into 's3n://superman-hw6/example-results';
