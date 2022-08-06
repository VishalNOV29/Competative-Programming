import java.util.*;

// Solving using 0 and 1.
// class FindPrime {

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter a number: ");
//         int num = sc.nextInt();
//         int arr[] = new int[num+1];
//         System.out.println(Arrays.toString(arr));
//         int last = (int) Math.sqrt(num);
//         System.out.println(last);
//         for (int i = 2; i <= last; i++) {
//             for (int j=i+1;j<arr.length;j++){
//                 if (j%i==0){
//                     arr[j]=-1;
//                     System.out.println(Arrays.toString(arr));
//                     System.out.println("j = "+j+" i = "+i);

//                 }
//             }
//         }
//         int count=0;
//         System.out.println(Arrays.toString(arr));
//         for (int i=2;i<arr.length;i++){
//             if (arr[i]==0){
//                 System.out.println(i);
//                 count++;
//             }
//         }
//         System.out.println("Total prime = "+count);

//     }
// }

// Now I am going to implement to this concept using boolean array.
// Mark all the element initally with false. By default java boolean array stores false value.

// class FindPrime{
//     static boolean[] isPrime(int n){
//         boolean arr[]=new boolean[n];
//         Arrays.fill(arr, true);
//         arr[0]=false;
//         if (n>=1){
//             arr[1]=false;
//         }

//         for (int i=2;i*i<n;i++){
//             for (int j=2*i;j<n;j+=i){
//                 arr[j]=false;
//             }
//         }
//         System.out.println("Method is returning.");
//         return arr;
//     }
//     public static void main(String[] args){
//         Scanner sc=new Scanner(System.in);
//         System.out.println("Enter a number: ");
//         int num=sc.nextInt();
//         boolean[] arr=isPrime(num);
//         int count=0;
//         for (int i=0;i<arr.length;i++){
//             System.out.println(i+" "+arr[i]);
//             if (arr[i]==true){
//                 count+=1;
//             }
//         }
//         System.out.print("Total Prime : "+count);

//     }
// }

// class Course{
//     String name;
//     int number;
//     String instructor;
//     int[] students=new int[maxNumOfStudents];
//     static int maxNumOfStudents=60;
//     Course(String n,int num,String i,int[] s){
//         name=n;
//         instructor=i;
//         maxNumOfStudents=num;
//         if (students.length<=s.length){
//             students=s;
//         }else{
//             int newArr[]=new int[s.length];
//             for (int i=0;i<s.length;i++){
//                 newArr[i]=s[i];
//             }
//         }

//     }
// }

class Course {
    String name = "unknown";
    int number = -1;
    String instructor = "unknown";
    int[] students = new int[5];

    Course(String n, int num, String i, int[] s) {
        name = n;
        number = num;
        instructor = i;
        students = s;
        students = new int[s.length];
        if ()
        for (int j = 0; j < students.length; j++) {
            students[j] = s[j];
        }

    }

    Course() {
    }

    int getNumberOfStudents() {
        return students.length;
    }

    void printStudentsIDs() {
        for (int i = 0; i < students.length; i++) {
            System.out.print(students[i] + ", ");
        }
    }

    void addStudent(int id) {
        int[] a = new int[students.length + 1];
        for (int i = 0; i < students.length; i++)
            a[i] = students[i];
        a[a.length - 1] = id;
        students = a;
    }

    boolean removeStudent(int id) {
        int m = 0;
        for (int i = 0; i < students.length; i++) {
            if (students[i] == id) {
                m = i;
            }
        }
        if (m == 0) {
            return false;
        } else {
            int[] a = new int[students.length - 1];
            for (int i = 0; i < students.length; i++) {
                if (i < m) {
                    a[i] = students[i];
                } else if (i > m) {
                    a[i - 1] = students[i];
                }
            }
            students = a;
            return true;
        }
    }

}
