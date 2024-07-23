import java.util.*;
 
public class main{
    public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    
    // Taking an input argument
    int n = scanner.nextInt();
    List<List<Integer>> finalData = new ArrayList<>();
    
    // Reading the matrix rows
    for (int i = 0; i < n; i++) {
        List<Integer> row = new ArrayList<>();
        for (int j = 0; j < 3; j++) {
            row.add(scanner.nextInt());
        }
        finalData.add(row);
    }
    
    List<Integer> finalVal = new ArrayList<>();
    
    // Calculating the sum of columns
    for (int i = 0; i < 3; i++) {
        int sum1 = 0;
        for (int j = 0; j < n; j++) {
            sum1 += finalData.get(j).get(i);
        }
        finalVal.add(sum1);
    }
    
    // Checking if the sum of all column sums is zero
 
    for (int i: finalVal){
        if (i==0){
            continue
        }else{
             System.out.println("NO");
        }
    }
    System.out.println("YES");
    scanner.close();
        
    }
}