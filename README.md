# Toy Robot Simulator

## Description

The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units.

## Usage

This is a command line application. The application reads in commands of the following (textual) form:

```bash
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
Q
```
## Commands Explained

```bash
PLACE
```
This command will put the toy robot on the table in position X,Y and facing NORTH, SOUTH,
EAST or WEST.

```bash
MOVE
```
This command will move the toy robot one unit forward in the direction it is currently facing.

```bash
LEFT
```
This command will rotate the robot 90 degrees in the specified direction without changing the
position of the robot.

```bash
RIGHT
```
This command will rotate the robot 90 degrees in the specified direction without changing the
position of the robot.

```bash
REPORT
```
This command will announce the X,Y and F of the robot. This can be in any form, but
standard output is sufficient.

```bash
Q
```
This command will close the program

## TESTING

To run the automated unit tests you need to run the [unittest](https://docs.python.org/3/library/unittest.html) Unit testing framework using the following command in the project directory 

```bash
python -m unittest discover
```
You can Quit by entering "Q" to get the results of the tests

## Configuration for static analysis
[Deepsource](https://github.com/OzzyGrammer/Toy_Robot_Simulator/blob/master/.deepsource.toml)

## Coverage testing Report(html)
[coverage](https://github.com/OzzyGrammer/Toy_Robot_Simulator/blob/master/htmlcov/index.html)








