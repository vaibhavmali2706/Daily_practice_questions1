class Solution {
    public int commonFactors(int a, int b) {
        int cnt=0;
        for (int i =0;i<=b;i++){
            if (i==0){
                
            }
            else if (a%i==0 && b%i ==0){
                cnt+=1;
            }
        }
        return cnt;
        
    }
}