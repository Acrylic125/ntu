package com.lab;

import java.util.Scanner;

public class Shape2DApp {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the number of shapes: ");
        int numberOfShapes = scan.nextInt();
        Shape[] shapes = new Shape[numberOfShapes];

        for (int i = 0; i < numberOfShapes; i++) {
            System.out.println("Shape " +  (i + 1) + " / " + numberOfShapes + " : ");
            System.out.println("Enter the shape (1 for Circle, 2 for Rectangle, 3 for Square, 4 for Triangle): ");
            int shapeType = scan.nextInt();

            switch (shapeType) {
                case 1:
                    System.out.println("Enter the radius: ");
                    double radius = scan.nextDouble();
                    shapes[i] = new Circle(radius);
                    break;
                case 2:
                    System.out.println("Enter the length: ");
                    double length = scan.nextDouble();
                    System.out.println("Enter the width: ");
                    double width = scan.nextDouble();
                    shapes[i] = new Rectangle(length, width);
                    break;
                case 3:
                    System.out.println("Enter the side: ");
                    double side = scan.nextDouble();
                    shapes[i] = new Square(side);
                    break;
                case 4:
                    System.out.println("Enter the width: ");
                    double widthTriangle = scan.nextDouble();
                    System.out.println("Enter the height: ");
                    double height = scan.nextDouble();
                    shapes[i] = new Triangle(widthTriangle, height);
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
