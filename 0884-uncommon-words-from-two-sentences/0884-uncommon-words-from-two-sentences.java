class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        String[] words1 = s1.split(" ");
        String[] words2 = s2.split(" ");
        Map<String, Integer> countMap = new HashMap<>();

        for (String word : words1) {
            countMap.put(word, countMap.getOrDefault(word, 0) + 1);
        }

        for (String word : words2) {
            countMap.put(word, countMap.getOrDefault(word, 0) + 1);
        }

        List<String> uncommonWords = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() == 1) {
                uncommonWords.add(entry.getKey());
            }
        }

        return uncommonWords.toArray(new String[0]);
    }
    }
