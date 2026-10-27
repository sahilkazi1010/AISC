#C-XOR

#include <stdio.h>

int activation(float sum)
{
    return sum >= 0 ? 1 : 0;
}

int main()
{
    int x1, x2;

    printf("Enter x1 (0 or 1): ");
    scanf("%d", &x1);
    printf("Enter x2 (0 or 1): ");
    scanf("%d", &x2);

    // Hidden layer: OR
    int h1 = activation(x1 + x2 - 0.5);

    // Hidden layer: NAND
    int h2 = activation(-x1 - x2 + 1.5);

    // Output layer: AND
    int output = activation(h1 + h2 - 1.5);

    printf("Hidden Neuron H1 (OR) = %d\n", h1);
    printf("Hidden Neuron H2 (NAND) = %d\n", h2);
    printf("XOR Output = %d\n", output);

    return 0;
}
