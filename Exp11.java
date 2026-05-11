

import java.util.HashMap;

public class Exp11 {

    public static void main(String[] args) {
        String text = "This is a simple WordCount application that counts the number of occurrences of each word in a given input set using the Hadoop MapReduce framework on local-standalone set-up";
        String[] words = text.split(" ");
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for (String word : words) {
            word = word.toLowerCase(); // Convert to lowercase for case-insensitive counting
            if (map.containsKey(word)) {
                map.put(word, map.get(word) + 1);
            } else {
                map.put(word, 1);
            }
        }
        
        // Print the word counts
        for (String word : map.keySet()) {
            System.out.println(word + ": " + map.get(word));
        }
    }
}