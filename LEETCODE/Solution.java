import java.util.Arrays;

// class ListNode {
//     int val;
//     ListNode next;
//     ListNode(int x) {
//         val = x;
//         next = null;
//     }
// }
// class Solution {

// }
// class Solution{
//     public static void main(String[] args){
//         int arr[]={1,2,3,4,5,6,7,1,2,3,4,5,6,7};

//         int k=5;
//         Arrays.sort(arr);
//         int i=0; 
//         int j=arr.length-1;
//         int count=0;
//         while (i<j){
//             if (arr[i]+arr[j]==k){
//                 count++;
//                 i++;
//                 j--;
//             }else if(arr[i]+arr[j]<k){
//                 i++;
//             }else{
//                 j--;
//             }

//         }
//         System.out.println("Count ="+count);
//     }
// }
// class Solution{

//     // arr: input array
//     // n: size of array
//     //Function to find the sum of contiguous subarray with maximum sum.
//     long maxSubarraySum(int arr[], int n){

//         // Your code here
//         int maxSum=0;
//         int currentSum=0;
//         for (int i=0;i<arr.length;i++){
//             currentSum=currentSum+arr[i];
//             if (currentSum>maxSum){
//                 maxSum=currentSum;
//             }
//             if (currentSum<0){
//                 currentSum=0;
//             }
//         }
//         return maxSum;

//     }
//     public static void main(String[] args){
//         Solution obj=new Solution();
//         int arr[]={-1,-1,-1,-1,-1};
//         int arr1[]=Arrays.sort(arr);
//         long res =obj.maxSubarraySum(arr, 6);
//         System.out.println(res);
//     }

// }
// class Student{
//     String name;
// }


class Solution {
    public static void bar(int[] values){
        for (int i=0;i<values.length;i++){
            values[i]=i;
        }
    }
    public static void main(String[] args){
        int [] xyz={5,123,-78,94,-1001};
        bar(xyz);
        System.out.println(xyz[3]);
    }
}