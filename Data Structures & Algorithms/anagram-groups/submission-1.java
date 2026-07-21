class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> ana = new HashMap<>();

        for (String s: strs){
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c-'a']++;
            }
            String key = Arrays.toString(count);
            ana.putIfAbsent(key, new ArrayList<>());
            ana.get(key).add(s);
        }
        return new ArrayList<>(ana.values());
    }
}
