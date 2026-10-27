#include <stdio.h>

int activation(float sum)
{
    if (sum >= 0)
        return 1;
    else
        return 0;
}

int main()
{
    float x1, x2;
    float w1 = 1.0;
    float w2 = 1.0;
    float bias = -1.5;

    printf("Enter Input x1 (0 or 1): ");
    scanf("%f", &x1);

    printf("Enter Input x2 (0 or 1): ");
    scanf("%f", &x2);

    float sum = (x1 * w1) + (x2 * w2) + bias;

    int output = activation(sum);

    printf("\nWeighted Sum = %.2f\n", sum);
    printf("AND Gate Output = %d\n", output);

    return 0;
}
