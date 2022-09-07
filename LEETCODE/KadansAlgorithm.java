class KAlgorithms {

    int maxSum(int arr[]) {
        int currSum = 0;
        int maxSum = Integer.MIN_VALUE;
        for (int i = 0; i < arr.length; i++) {
            currSum=currSum+arr[i];
            System.out.println("CurrentSum: "+currSum);
            if (maxSum<=currSum) {
                maxSum = currSum;
                System.out.println(maxSum);
            }
            if (currSum < 0) {
                currSum = 0;
            }
           
        }
        return maxSum;
    }

    public static void main(String[] args) {
       
        KAlgorithms obj = new KAlgorithms();
        int arr[] = { 1, 2,-9, 3, 4, 5, 6 ,-12};
        int result = obj.maxSum(arr);
        System.out.println("Maximum Sum: " + result);

    }
}