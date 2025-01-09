import java.util.Arrays;

class Merge{
  public static void main(String[] args){
    int[] input = {1,5,2,6,7,11,0,12};

    for (int i=0;i<input.length-1;i++){
      int k;
      for (int j =0;j<input.length-1;j++){
        if (input[j]>input[j+1]){
          k=input[j];
          input[j]=input[j+1];
          input[j+1]=k;
        }
      }
    System.out.println(Arrays.toString(input));
    }
  }
}
