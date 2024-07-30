# Drawing-the-Number-Pi

Drawing the Number Pi in a Quarter Circle
This repository contains a program that illustrates the calculation of the number π (pi) using a random sampling method in a quarter circle. It utilizes the random and hypot libraries to generate random points and determine their position relative to the circle.

Project Description
The program generates a large number of random points within a square of side 1 and calculates whether these points fall within a quarter circle of radius 1 using the hypot function. By comparing the number of points inside the quarter circle to the total number of points generated, the program estimates the value of π.

Features
Random Point Generation: Utilizes the random library to generate points (x, y) within a square.
Determination of Points Inside the Circle: Uses the hypot function from the math library to check if a point falls within the quarter circle.
Estimation of π: Calculates the value of π based on the proportion of points inside the quarter circle compared to the total points.
Visualization: (Optional) May include a visualization component to display the points and the circle.
