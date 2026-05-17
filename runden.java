public class runden {
    public static void main(String[] args) {
        //System.out.println(runden(243));
    }

    public static int digits(int n) {
        int counter = 0;
        while (n > 1) {
            n = n / 10;
            counter++;
        }
        return counter;
    }

    public static void runden(int n) {
        // 256
        String temp = Integer.toString(n);
        int d = digits(n);
        for (int i = 0; i < temp.length(); i++) {
            // new int, aber es ist statisch...
        }
    }
}
