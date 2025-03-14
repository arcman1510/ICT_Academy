public class EsempiStringhe {

    public int contaCarattere(String frase, char carattere) {
        if (frase == null) {
            throw new IllegalArgumentException("La frase non può essere null");
        }
        int count = 0;
        for (char c : frase.toCharArray()) {
            if (c == carattere) {
                count++;
            }
        }
        return count;
    }
    
    public boolean isPalindroma(String parola) {
        if (parola == null) {
            throw new IllegalArgumentException("La parola non può essere null");
        }
        int left = 0;
        int right = parola.length() - 1;
        while (left < right) {
            if (parola.charAt(left) != parola.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}