#C-OR

#include <stdio.h>

int activation(float sum)
{
    return sum >= 0 ? 1 : 0;
}

int main()
{
    float x1, x2;
    float w1 = 1.0, w2 = 1.0, bias = -0.5;

    printf("Enter x1 (0 or 1): ");
    scanf("%f", &x1);
    printf("Enter x2 (0 or 1): ");
    scanf("%f", &x2);

    float sum = x1 * w1 + x2 * w2 + bias;
    int output = activation(sum);

    printf("Weighted Sum = %.2f\n", sum);
    printf("OR Gate Output = %d\n", output);

    return 0;
}
