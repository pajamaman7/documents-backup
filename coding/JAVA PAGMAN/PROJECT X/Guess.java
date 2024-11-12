import javax.swing.*;
import java.lang.Math;

public class Guess {
    public static void main(String[] args) {
        int ans = (int) (Math.random() * 1000 + 1);
        int userAnswer = 0;
        int turns = 0;
        String response = "Guess a number betwee 1 and 1000.";

        while (userAnswer != ans) {
            try{
                userAnswer = Integer.parseInt(JOptionPane.showInputDialog(null, response));
            } catch (NumberFormatException e){
                JOptionPane.showMessageDialog(null, "Invalid input! Try again!");
            }
            turns++;
            if (userAnswer < ans) {
                response = userAnswer + " is lower than the correct answer. Try again!";
            } else if (userAnswer == ans) {
                response = userAnswer + " is the correct answer! You won in " + turns + " turns";
            } else if (userAnswer > ans) {
                response = userAnswer + " is higher than the correct answer. Try again!";
            }
        }
        JOptionPane.showMessageDialog(null, response);
    }
}