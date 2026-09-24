class Solution {
    public int commonFactors(int a, int b) {
        int cnt=0;
        int low =0;
            if (a<b){
            low=a;

        }
        else{
            low =b;
        }
        for (int i =0;i<=low;i++){
            if (i==0){
                
            }
            else if (a%i==0 && b%i ==0){
                cnt+=1;
            }
        }
        return cnt;
        
    }
}