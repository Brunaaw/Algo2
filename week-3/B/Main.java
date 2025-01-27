import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        TreeMap<Integer, Integer> priorityMap = new TreeMap<>();

        while (true) {
            String line = scanner.nextLine();
            String[] parts = line.split(" ");
            int command = Integer.parseInt(parts[0]);

            if (command == 0) {
                break;
            } else if (command == 1) {
                int k = Integer.parseInt(parts[1]);
                int p = Integer.parseInt(parts[2]);
                priorityMap.put(p, k);
            } else if (command == 2) {
                if (priorityMap.isEmpty()) {
                    System.out.println(0);
                } else {
                    Map.Entry<Integer, Integer> highest = priorityMap.pollLastEntry();
                    System.out.println(highest.getValue());
                }
            } else if (command == 3) {
                if (priorityMap.isEmpty()) {
                    System.out.println(0);
                } else {
                    Map.Entry<Integer, Integer> lowest = priorityMap.pollFirstEntry();
                    System.out.println(lowest.getValue());
                }
            }
        }

        scanner.close();
    }
}