package com.lab.part2;

import java.util.Scanner;

public class Shape3DApp {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the number of shapes: ");
        int numberOfShapes = scan.nextInt();
        Shape[] shapes = new Shape[numberOfShapes];

        for (int i = 0; i < numberOfShapes; i++) {
            System.out.println("Shape " +  (i + 1) + " / " + numberOfShapes + " : ");
            System.out.println("Enter the shape (1 for Sphere, 2 for Cuboid, 3 for Pyramid, 4 for Cone, 5 for Cylinder): ");
            int shapeType = scan.nextInt();

            switch (shapeType) {
                case 1: 
                    System.out.println("Enter the radius: ");
                    double radius = scan.nextDouble();
                    shapes[i] = new Sphere(radius);
                    break;
                case 2:
                    System.out.println("Enter the width: ");
                    double width = scan.nextDouble();
                    System.out.println("Enter the breadth: ");
                    double breadth = scan.nextDouble();
                    System.out.println("Enter the height: ");
                    double height = scan.nextDouble();
                    shapes[i] = new Cuboid(width, breadth, height);
                    break;
                case 3:
                    System.out.println("Enter the base width: ");
                    double baseWidth = scan.nextDouble();
                    System.out.println("Enter the height: ");
                    double pyramidHeight = scan.nextDouble();
                    shapes[i] = new Pyramid(baseWidth, pyramidHeight);
                    break;
                case 4:
                    System.out.println("Enter the radius: ");
                    double coneRadius = scan.nextDouble();
                    System.out.println("Enter the height: ");
                    double coneHeight = scan.nextDouble();
                    shapes[i] = new Cone(coneRadius, coneHeight);
                    break;
                case 5:
                    System.out.println("Enter the radius: ");
                    double cylinderRadius = scan.nextDouble();
                    System.out.println("Enter the height: ");
                    double cylinderHeight = scan.nextDouble();
                    shapes[i] = new Cylinder(cylinderRadius, cylinderHeight);
                    break;
                default:
                    System.out.println("Invalid shape type, skipping");
                    break;
            }
        }

        double totalArea = 0;
        for (Shape shape : shapes) {
            totalArea += shape.area();
        }

        System.out.println("Total area of all shapes: " + totalArea);
    }
}
