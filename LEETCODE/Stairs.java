import java.util.Scanner;
public class Stairs{
    public int factorial(int x){
        int fact=1;
        for  (int i=1;i<=x;i++){
            fact=fact*i;
        }
        return fact;
    }
    public int number_of_occurance(int x,int y){
        float z=0;
        Stairs obj1=new Stairs();
        z=obj1.factorial(x+y)/(obj1.factorial(x)*obj1.factorial(y));
        int Z=(int) z;
        return Z;

    }
    public static void main(String[] args){
        Stairs obj=new Stairs();
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter number of stairs : ");
        int n=sc.nextInt();
        int result=0;
        if (n%2==0){
            int no_of_2=Math.floorDiv(n, 2);
            int no_of_1=0;
            while (no_of_2>=0){
                int temp_result=obj.number_of_occurance(no_of_2, no_of_1);
                result+=temp_result;
                no_of_1+=2;
                no_of_2-=1;
            }
            // return result;
            System.out.println("Number of possible ways are :"+result);
        }
        else{
            int no_of_2=Math.floorDiv(n, 2);
            int no_of_1=1;
            while (no_of_2>=0){
                int temp_result=obj.number_of_occurance(no_of_1, no_of_2);
                result+=temp_result;
                no_of_1+=2;
                no_of_2-=1;
            }
            System.out.println("Number of possible ways are :"+result);
        }
        sc.close();

    }
}