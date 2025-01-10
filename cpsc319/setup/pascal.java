class Pascal{
  public static int factorial(int n){
    if (n==0){
      return 1;
    } else{
      return n*factorial(n-1);
    }
  }
  public static int binom(int n, int k){
    return factorial(n)/(factorial(k)*factorial(n-k));
  }
  public static String pascalRow(int row){
    String line = "";
    for (int i = 0; i<=row; i++){
      line += Integer.toString(binom(row,i))+" ";
    }
    return line;
  }

  public static void pascalTri(int n){
    for (int i =0; i<=n; i++){
      System.out.println(pascalRow(i));
    }
  }
  
  public static void main(String[] args){
    pascalTri(10);
  }
}
