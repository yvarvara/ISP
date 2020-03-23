# Pixel-Art

#### Task

the clustering task can be described as follows: the task of grouping a set of objects into subsets (clusters) in such a way that objects from one cluster are more similar to each other than to objects from other clusters by some criterion.

In this project, I would like to conduct a study of several methods for solving this problem, adding a game component to the project.

#### Used technologies

+ The application is implemented using Python programming language
+ MongoDB is used to work with the database
+ Tkinter library is used to create the graphical interface

## Project description

the game allows you to create images by painting pixels on the canvas with a certain color. With a help of clusterization we get an image divided into many blocks that the user can color. To solve this problem, we will use the most popular K- means clustering algorithm. The app supports saving created images and the ability to continue drawing after restarting the program.
One of the main goals of this application is also to demonstrate the operation of the clustering methods considered, which are used to split an image into the required number of colors.

## Usage

1. Main page displays previously processed images, the drawing window opens when the image is clicked. There are Settings button (opens a list of difficulty levels) and Creating a new image button.

![c6187662bb291db46a03b28c7489e44c.png](https://picua.org/images/2020/03/23/c6187662bb291db46a03b28c7489e44c.png)

2. This module represents the drawing page. The workspace is divided into numbered blocks according to the image. The numbers on the buttons correspond to the blocks on the drawing area that need to be filled in with this color. There is a placemark under each color on the palette indicating the number of unpainted pixels of this color.

![da5453378cfbb880d62cb4f6d6cf94fd.png](https://picua.org/images/2020/03/23/da5453378cfbb880d62cb4f6d6cf94fd.png)

For clarity, a monochrome version of the processed image is placed on the background of the workspace, which gradually becomes lighter when zoomed.

![39e1bab7a744ff9ecc9a68449cc7e517.png](https://picua.org/images/2020/03/23/39e1bab7a744ff9ecc9a68449cc7e517.png)
![d2ae39ebe8835aee5fbed50786976284.png](https://picua.org/images/2020/03/23/d2ae39ebe8835aee5fbed50786976284.png)

3. On this page, there are two sliders that allow you to set the block size (in pixels) and the number of colors for the image. You can also define the clustering algorithm to use, with a preview of the final image on the right side of the window. There are following options: K-means (the classic k-means method with a random selection of cluster centers), Modified K-means (a modified k-means method with a selection of cluster centers based on the most frequent colors), and K-means (ML) (the k-means method provided by the sklearn machine learning library). Clicking the Draw button at the bottom of the window opens the drawing page with the newly created image.

![498874b5f77e54422b2f700886a74f1b.png](https://picua.org/images/2020/03/23/498874b5f77e54422b2f700886a74f1b.png)
![f8eeffe72edbcb407efb24dbf10e5c96.png](https://picua.org/images/2020/03/23/f8eeffe72edbcb407efb24dbf10e5c96.png)
