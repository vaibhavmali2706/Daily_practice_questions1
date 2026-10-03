class Solution {

    public int countSegments(String s) {

        int len = s.length();
        int count = 0;

        for (int i = 0; i < len; i++) {

            if (s.charAt(i) != ' ' &&
                (i == 0 || s.charAt(i - 1) == ' ')) {

                count++;
            }
        }

        return count;
    }
}