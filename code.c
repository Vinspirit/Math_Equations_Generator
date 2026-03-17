#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// Function to get operator character
char getOperator(int opIdx) {
    char ops[] = {'+', '-', '*', '/'};
    return ops[opIdx];
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <number_of_exercises>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    char *studentID = "2456336"; 
    
    FILE *file = fopen("result.txt", "w");
    if (file == NULL) {
        return 1;
    }

    
    srand(time(NULL));

    fprintf(file, "%s\n", studentID);

    for (int i = 0; i < n; i++) {
        int numOps = (rand() % 3) + 3; // Randomly choose 3, 4, or 5 operators
        int numbers[6];
        int ops[5];
        
        // Generate numbers and operators
        for (int j = 0; j <= numOps; j++) {
            numbers[j] = rand() % 101; // 0 to 100
            if (j < numOps) {
                ops[j] = rand() % 4; // 0:+, 1:-, 2:*, 3:/
            }
        }

        
        float result = numbers[0];
        char expression[100];
        sprintf(expression, "%d", numbers[0]);

        for (int j = 0; j < numOps; j++) {
            char op = getOperator(ops[j]);
            int nextNum = numbers[j+1];
            
            // Append to expression string
            char temp[20];
            sprintf(temp, "%c%d", op, nextNum);
            sprintf(expression + strlen(expression), "%s", temp);

            // Calculate result (Simplified left-to-right)
            if (op == '+') result += nextNum;
            else if (op == '-') result -= nextNum;
            else if (op == '*') result *= nextNum;
            else if (op == '/') {
                if (nextNum != 0) result /= nextNum;
            }
        }

        // Output to file: expression=result (as integer)
        fprintf(file, "%s=%.0f\n", expression, result);
    }

    fclose(file);
    return 0;
}