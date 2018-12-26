 This is the first step to a self-driving car vision. The best library out there for coding such kinds of stuff in python. I have used OPEN CV library to code this car algorithm.
What is the first thing that comes into your mind while you are getting directions for your car? its watching lanes in front of you on the road.
So, I need to constantly feed my PC with the lanes in front of me.
The algorithm I used for detecting the lane is very straightforward.
I have used the edge detection techniques.

Want to add a caption to this image? Click the Settings icon.
 Consider an image as a matrix of pixels, where each element of the matrix is a value ranging from 0-255, as a single color channel has the value from 0(lighter) to 255(darker).
There are three color channels (Red Green Blue)
so an image matrix is a 3 Dimensional matrix in which, the 3rd dimension is for the color channels R, G, and B.
Step 1: Grayscale
Before doing any operations we convert the 3d colored image matrix to 2d gray-scale matrix .where each pixel has a value from 0-255, where 0 is for Black and 255 is for White.
This step is done to reduce the computations for processing the image as its easy to process all pixels of the 3d matrix then a 2d gray-scale image matrix.
For additional reading click here

GrayScale Image

 Step 2: Blur image
Secondly, we need to blur the image to remove all the noise from the image and make the image smooth.
To Blur the image we use the Algorithm of filters(or kernel)
Where a custom sized kernel is declared (usually 3 x 3). Which is hovered over the image and multiplied with the matrix and produce the new matrix with blur kernel multiplied
We use Gaussian Blur kernel which takes an average of the pixels around it
the filter looks like
For additional reading click here



 The above image shows the multiplication technique of matrices. 

The Blurred image

Step 3: Applying Canny Edge Detection
For additional reading on this click ion
This technique is used to find edges.
this technique uses a kernel to detect Rapid intensity change to find edges it converts the image to something like this to make it easy to detect edges.
For additional reading on this clickhere

After Canny edge detection 

Step 4 : Add a Polygonal mask 
We apply polygonal mask on the image where the lanes are there.
By applying the polygonal mask on the region of interest we get a image where there is only the lanes present .For example here we take we take a trapezoid to mask the image and get the desired output. 
Intuition here is Applying bitwise and operator between images
[Image 1 &Image 2 (mask )= Image 3]
For further information click here





Step 5: Find lines from the points which are lit up(White)
We use the Hough Lines technique to find the lines.
In this, the family of lines passing from a specific point  present in the x y plane is represented as a family of points on a line in the intercept slope plane (points here are plotted with intercepts as y-axis and slope as x-axis) 


Hough Graph 
 The following are the lines found from the points in the canny cropped image 


Lines present
 
Step 6: Optimize the lines
To optimize the lines we need to take find all the coordinates of the lines plotted first.
Then find all the intercepts and slopes of the lines 
Differentiate right and left lines with help of the slope,i.e., +ve slope lines are left line and 
-ve slope lines are right lines.
Find the average slope of left and right line and plot the averaged line with the help of averaged slope and intercept found.
Hence will obtain such an image
 

Average right and left line

 Step 7: The final step
Now feed a live video of road or lanes of road to the computer from a camera
and chop the video into frames and input each frame of video into the steps 1-6.
so the output is a collection of this plotted frames resulting in a video
