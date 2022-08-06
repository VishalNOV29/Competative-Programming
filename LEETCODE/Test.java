// import java.util.ArrayList;
// import java.util.Scanner;

// interface shape {
//     void getArea();

//     void getVolume();

//     void getName();
// }

// // Implementation of point class.
// class point implements shape {
//     int x, y;
//     int arr[] = { x, y };

//     public int[] get(int x, int y) {
//         return arr;
//     }

//     public void set(int x, int y) {
//         this.x = x;
//         this.y = y;
//     }

//     // Implementation of interface methods.
//     public void getArea() {
//         System.out.println("Area is not applicable to a point.");
//     };

//     public void getVolume() {
//         System.out.println("Volume is not applicable to a point.");
//     }

//     public void getName() {
//         System.out.println("This is a point.");
//     }
// }

// // Implementation of circle class.
// class circle extends point {
//     private double radius;

//     public double get() {
//         return radius;
//     }

//     public void set(double rad) {
//         radius = rad;
//     }

//     @Override
//     public void getArea() {
//         double area = Math.PI * radius * radius;
//         System.out.println("Area of circle is: " + area);
//     }

//     @Override
//     public void getName() {
//         System.out.println("This is a circle.");
//     }

// }

// // Implementation of cylinder class.
// class cylinder extends circle {
//     private double height;
//     private double radius;

//     public double get() {
//         return height;
//     }

//     public void set(double h, double rad) {
//         height = h;
//         radius = rad;
//     }

//     @Override
//     public void getArea() {
//         double area = 2 * Math.PI * this.radius * height;
//         System.out.println("Area of cylinder is : " + area);

//     }

//     @Override
//     public void getVolume() {
//         double volume = Math.PI * radius * radius * height;
//         System.out.println("Volume of cylinder is: " + volume);
//     }

//     @Override
//     public void getName() {
//         System.out.println("This is a cylinder.");
//     }
// }

// public class Test {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.println("How many objects will be created.");
//         int num = sc.nextInt();
//         ArrayList<String> arr = new ArrayList<String>(num);
//         for (int i = 0; i < num; i++) {
//             System.out.println("For point : 1, for circle : 2, for cylinder : 3.");
//             System.out.println("Enter your choice:");
//             int ch=sc.nextInt();
//             if (ch==1){
//                 circle c1=new circle();
//                 arr.add(c1);
//             }

//         }

//     }

// }
