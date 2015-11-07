**Image compression using k-means**

- The aim is to compress the image using k-means algorithm. The original image requires 24 bits for all 128*128 pixels. Thus, the total number of bits required for storage of this image is 128*128*24 = 393,216 bits.
- For compressing the image, we choose 16 colours to represent the image. (Randomly selecting 16 out of all 128*128 values)
- Thus, the storage required for this compressed image is 16*24 + 128*128*4 = 65920 bits
	- 16 colours each of which needs 24 bits ( 8 bits each for RGB ) 
	- For all 128*128 pixels, each pixel now needs just 4 bits to represent ( 2^4 = 16 colours).
	
- For modelling this problem in terms of k-means algorithm, assume 16 colours to be 16 clusters. ( We can vary this ).
- The image is represented by mX3 matrix where m is the total number of pixels in the image ( 128*128 ) and 3 columns refer to RGB values ( 0-255 ).
- Following k-means algorithm, assign each pixel to one of the 16 clusters. 
- Running the algorithm will give us the new RGB values for each of the 16 colours.
- The image thus formed is the compressed image.


**References**
- Machine Learning course, Coursera, by Andrew Ng, Stanford University. 