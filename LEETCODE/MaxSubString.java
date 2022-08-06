import java.util.Scanner;
public class MaxSubString {
    public static void main(String[] args){
        Scanner obj=new Scanner(System.in);
        String string=obj.nextLine();
        // String max="";
        for (int i=0;i<string.length();i++){
            for (int j=i;j<string.length();j++){
                String temp_str=string.substring(i, j+1);
                System.out.print(temp_str+" ");
            }
            System.out.println();
        }
        // System.out.println(string[]);
        obj.close();

    }
}
