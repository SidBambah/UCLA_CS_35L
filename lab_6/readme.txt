Sidharth Bambah
UID: 904 787 435

In the supplied main.c file, there was only support for one thread. Any attempt
to run the program with more than one thread resulted in an error message. Thus,
the focus of this homework was to implement the program in such a way so as to
support multiple threads.

To do this, I had to figure out which routine all of the threads would run. I 
created a routine function and inserted all of the commands given in the main 
function. Thus, each thread would run the routine supplied in this function. 
Originally, I had an issue in which local variables defined in the main function
could not be accessed. However, I learned that each thread would not have access
to any local variables defined in the main function. Thus, I had to place some of
these variables into the global domain in order to allow them to be accessible
by each of the individual threads.

Now that I had the routine set up, I had to create and run all of the threads. To
do this, I read the number of threads from the input into a variable and used this
as a bound of a for loop that creates numerous threads. To keep track of all of
these threads and their unique id's I set up two different arrays for each of these
parameters. It should be noted that each of these newly created threads was passed
the routine. Furthermore, I found that pthread_create takes a void* argument to
the function. Thus, I passed a reference to each element in the thread id array
and casted them to integer pointers.

I ran into the issue of printing the rendered variables in the routine of each of
the threads. I found that the buffer of the printf function will be manipulated by
each of the threads making it impossible to print the variables that needed to be
printed. In order to overcome this issue, I created a three dimensional array that
held all of the values for the image (width, height, and color) and stored each
value for each thread in this array. 

The issues prevalent after this had to do with small syntax errors and incorrect
definitions of variables. However, these issues were quickly resolved after I
read the compiler notes. Furthermore, I had a warning telling me that the routine
for each of the threads did not return the correct thing. In order to solve this, 
I had the routine return NULL satisfying the requirement for the function.

We can see that the performance of the program increased quite a bit with the
implementation of multithreading. This can be demonstrated by the timing outputs
given below:

time ./srt 1-test.ppm >1-test.ppm.tmp

real    0m48.179s
user    0m48.173s
sys     0m0.002s
mv 1-test.ppm.tmp 1-test.ppm
time ./srt 2-test.ppm >2-test.ppm.tmp

real    0m23.682s
user    0m47.070s
sys     0m0.001s
mv 2-test.ppm.tmp 2-test.ppm
time ./srt 4-test.ppm >4-test.ppm.tmp

real    0m11.643s
user    0m46.246s
sys     0m0.028s
mv 4-test.ppm.tmp 4-test.ppm
time ./srt 8-test.ppm >8-test.ppm.tmp

real    0m6.582s
user    0m49.943s
sys     0m0.008s

Clearly, there is an improvement in the timings due to the increase in thread
count. Each of the rendering tasks are parallelized resulting in a net increase
in efficiency for the program.