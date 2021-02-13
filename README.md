# K-means clustering: Image Compression

# About

This project is an introduction to K-means clustering through its Python implementation. Also, it includes its application to image compression. 

# Algorithm

![K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/Kmeans_animation.gif](K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/Kmeans_animation.gif)

1. Initialization: Randomly sample k colors from the input image. These are the initial k means

![K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/Untitled.png](K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/Untitled.png)

2. For each pixel in the image, assign it to its nearest mean given by

![K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/Untitled%201.png](K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/Untitled%201.png)

3. Update the means using the pixel assignments from Step 2. 

![K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/Untitled%202.png](K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/Untitled%202.png)

4. Repeat Steps 2 and 3 until convergence.

# Image Compression

![K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/1-Saint-Basils-Cathedral.jpg](K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/1-Saint-Basils-Cathedral.jpg)

The image above may contain over 16 million colors. However, sometimes we do not need to store all the values but still maintain the important information of an image. Therefore, we can compress an image. 

![K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/original_colorSpace.png](K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/original_colorSpace.png)

As it is shown above, the original color space is very rich in colors, in fact there are 255 * 255 * 255 possible colors. Using K-means clustering algorithm we can generalize all these colors by their corresponding centroids. Thus, the image is compressed by this approach. 

![K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/compressed_colorSpace.png](K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/compressed_colorSpace.png)

Finally, we obtain out compressed image

![K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/compressed_example.png](K-means%20clustering%20Image%20Compression%20da6f1926505340cc91e47339f4718272/compressed_example.png)