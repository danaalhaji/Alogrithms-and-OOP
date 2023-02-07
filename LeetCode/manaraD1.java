public class manaraD1{

public int solution(String s, String t) {
    int count = 0;

    for (int i = 0; i < t.length(); i++) {
        if (isDigit(t.charAt(i))) {
            String newT;
            newT = removeDigit(t, i);
            if (s.compareTo(newT) < 0) {
                count++;
            }
        }
    }

    for (int i = 0; i < s.length(); i++) {
        if (isDigit(s.charAt(i))) {
            String newS;
            newS = removeDigit(s, i);
            if (newS.compareTo(t) < 0) {
                count++;
            }
        }
    }

    return count;
}

private  boolean isDigit(char ch) {
    if (ch >= 48 && ch <= 57) {
        return true;
    }
    return false;
}

private  String removeDigit(String t, int index) {
    String newT = "";
    for (int i = 0; i < t.length(); i++) {
        if (i == index) {
            continue;
        } else {
            newT = newT + t.charAt(i);
        }
    }
    return newT;
}
}