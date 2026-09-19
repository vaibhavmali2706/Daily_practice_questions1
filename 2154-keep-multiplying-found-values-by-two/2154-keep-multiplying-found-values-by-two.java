class Solution 
{
    public int findFinalValue(int[] arr, int original) 
    {
        
        while(search(arr,original))
        {
            original=original*2;
        }
        return original;      
    }
    public boolean search(int arr[],int data)
    {
        for(int i=0;i<arr.length;i++)
        {
            if(data==arr[i])
            {
                return true;
            }
        }
        return false;
    }
}
